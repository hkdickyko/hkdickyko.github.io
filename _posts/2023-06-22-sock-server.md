---
category: [軟件]
tags: [系統, Linux]
title: Sock Server
date: 2023-06-16 1:00:00
---

<style>
  table {
    width: 100%
    }
  td {
    vertical-align: center;
    text-align: center;
  }
  table.inputT{
    margin: 10px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
    border: none;
  }
  input{
    text-align: center;
    padding: 0px 10px;
  }
  iframe{
    width: 100%;
    display: block;
    border-style:none;
    overflow:hidden;
  }
</style>



# Dante-server





## 安裝

```
$ sudo apt-get update
$ sudo apt-get install dante-server
$ sudo systemctl status danted.service
```

## 修改配置文件

```
$ sudo vi /etc/danted.conf

# 日志
logoutput: syslog

# 用户权限
user.privileged: root
user.unprivileged: sockd
 
# 侦听网络接口或地址
internal: eth0 port=10808
 
# 代理网络接口或地址（要設置）
external: eth0
 
# socks 规则确定通过外部接口代理的内容
socksmethod: username
 
# 客户端规则决定谁可以连接到内部接口
clientmethod: none

# 客户端通行规则可多個（要設置）
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: error, connect, disconnect
}

# Socks 通行规则可多個（要設置）
socks pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: error, connect, disconnect
}

```


### 日志

設定有 log 到那檔案, default 沒有 logging 的 (除非已启用调试)

-  启用调试
   - debug: 0 - 无调试日志
   - debug: 1 - 一些调试日志
   - debug: 2 - 详细调试日志

```
debug: 1
```

### 用户权限

- user.privileged 
    - 如果需要读取 sockd.conf，写入 sockd.pid 等文件，或使用密码认证等需要特权的操作，则最好将此值设为 root，如果不需要特权操作，则可以设成 user.unprivileged 相同的用户即可。

- user.unprivileged
    - 用于运行 dante 进程的用户名，一多为 sockd。


### 侦听网络接口或地址

服务器在内部地址上接收来自 SOCKS 客户端的 SOCKS 请求

internal: <font color="#FF1000">192.168.3.1</font> port = <font color="#FF1000">1080</font>

或

internal: <font color="#FF1000">eth0</font> port = <font color="#FF1000">1080</font>

### 代理网络接口或地址

数据从 SOCKS 客户端转发到外部网络时使用外部接口

external: <font color="#FF1000">eth0</font>

### socksmethod

socksmethod 为系统用户登录，**注意**使用其它时，务必创建不能登录系统的账户，可通过命令 useradd 添加用户及 passwd 设置密码。权限可以为 /bin/false 是最严格的禁止 login 选项。

#### 控制用户认证的方法，可以是以下之一或组合。
- none 不需要认证
- username 用户名密码
- gssapi kerberos 认证
- rfc931 需要用户主机提供一个 rfc931 reply，这个reply必须匹配一个 /etc/passwd 中的用户名
- pam 通过 PAM 方式认证
- badauth 通过 BSD 认证系统

### 添加用户

```
$ useradd -r -s /bin/false dicky
$ passwd dicky

# 输入 
123456
```

### clientmethod

客户端规则决定谁可以连接到内部接口。默认值 <font color="#FF1000">none</font> 允许匿名访问。

### 查看端口

```
$ netstat -nap|grep 1080 
```

### pass / block

定义 rules，放行或者阻断。在 dante 的配置中，有两个层面的 rules，一个是 client-rules，另一个是 socks-rules。
client-rules 和 socks-rules 都由 pass 和 block 关键字组成，区别在于 client-rules 带有 client 前缀。

client-rules 会首先被检查，用来判别用户是否可以与 sockd 通讯，这些规则工作在 TCP 层。

socks-rules 是在通过 client-rules 判定，确认用户可以与 sockd 通讯以后，用来判别用户发送的连接的具体请求内容，并根据这些内容判定通过还是拒绝。

client-rules 和 socks-rules 都遵循 first match is best match 原则，即如果有多条规则匹配，则第一个匹配指定 client 或 socket 的规则会被执行。

在以上两种 rules 中，针对 IP 地址这个值，还有一套可选的关键字，其中 client-rules 中的可选关键字是 socks-rules 中的一个子集。

对于每条规则，规则中所有的条件类关键字都会被检查，如果匹配用户请求，则所有的动作都会被执行。

#### 例子

```
client pass {
  from: 0.0.0.0/0 to: 0.0.0.0/0
  log: connect disconnect error
}

socks pass {
  from: 0.0.0.0/0 to: 0.0.0.0/0
  log: connect disconnect error
}


client pass {
        from: 192.0.2.0/24 to: 0.0.0.0/0
	log: error # connect disconnect
        method: authmethod
	group: socksusers
}


```

### log 可設置值

 - error：错误信息
 - connect：接受的客户端连接的信息
 - disconnect：断开客户端连接的信息
 - ioop：每个数据传输操作
 - data：实际传输的数据
 - tcpinfo：通过 TCP_INFO 获取的信息



## 重启服务

```
# 開机自启服务
$ systemctl enable danted

# 重启一下服务
$ systemctl restart danted.service

# 查看状态
$ systemctl status danted.service
```