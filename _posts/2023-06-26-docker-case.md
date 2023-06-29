---
category: [Docker]
tags: [系統, Linux]
title: Docker 應用
date: 2023-06-26 1:00:00
---

<style>
  table {
    width: 100%
    }
  td {
    vertical-align: center;
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
  }
</style>

# 容器基本要素

容器是一種標準軟件單元，它打包代碼及其所有依賴項，以便應用程序從一個計算環境快速可靠地運行到另一個計算環境。 

  容器化軟件可用於基於 Linux 和 Windows 的應用程序，無論基礎設施如何，都將始終以相同的方式運行。 容器將軟件與其環境隔離，並確保其統一工作，儘管開發和登台之間存在差異。 


## 容器管理命令

|命令|解釋|
|:---|:---|
|docker create 影像档案 [command]| 創建容器|
|docker run 影像档案 [command] | 執行用器|
|docker rename 容器名 新容器名| 重钟命名容器|
|docker update 容器名|更新容器設置|
|docker start 容器名|開啟容器進程|
|docker stop 容器名|停止容器進程|
|docker kill 容器名|摧毁容器進程|
|docker restart 容器名|重啟容器進程|
|docker pause 容器名|暂停容器進程|
|docker unpause 容器名|恢复容器進程|
|docker rm [-f] 容器名|删除容器|

### 应用

```
$ docker create debian

# -d 是分离模式，執行後立即分离
$ docker run -d debian true ; echo $?

# -t 为伪终端，-i 为容許輸入。一般 -it 联用
$ docker run -t -i debian bash

# -u 設置用戶
$ docker run -u nobody debian whoami
nobody

# -w 設置當前目錄
$ docker run -w /opt debian pwd
/opt

# -e 設置當前環境參數， sh -c 为在 shell 內執行指今
$ docker run -e FOO=foo -e BAR=bar debian sh -c 'echo $FOO $BAR'
foo bar

# -h 設置當前本机名稱
$ docker run -h my-nice-container debian hostname
my-nice-container

# 为容器设置名称。默认生成随机名称。
$ docker run --name blahblah debian true

# 删除容器
$ docker rm blahblah

# 删除容器已关闭， ps -a -q 是只列出容器 ID 部分，-a 是加到列表。-f 为过滤规则。-q 为只列出 ID 部分
$ docker rm $(docker ps -a -f status=exited -q)

# 加載硬碟位置
$ docker run -ti -v /home/dicky/tmp:/storage/tmp debian

# 加載设备位置
$ docker run -ti --device /dev/sda debian
$ sudo fdisk -l /dev/sda

# -link 是导出服务的最基本方式，my-server 为网站接口。
$ docker run -ti --link my-server:srv debian

ping srv

# -p 为加 IP 地址及端口，如沒有加 IP 地址即为 0.0.0.0（所有接口），80 为本机端口，8080 为相對容器端口。
$ docker run -p 127.0.0.1:80:8080 nginx
```

## 检查容器

|命令|解釋|
|:---|:---|
|docker ps| 列出正在運行的容器|
|docker ps -a| 列出所有容器| 
|docker logs [-f] 容器名| 顯示容器輸出 (stdout+stderr)|
|docker top 容器名 [ps options] |列出容器內運行的進程|
|docker stats [容器名]| 顯示實時使用統計數據|
|docker diff 容器名| 顯示與圖像的差異（修改後的文件）|
|docker port 容器名| 列出端口映射| 
|docker inspect 容器名|顯示低級信息（json 格式）|
|docker attach 容器名 |附加到正在運行的容器 (stdin/stdout/stderr) |
|docker cp 容器目录 本機目录|- 容器目录下所有檔案復製到本機目录| 
|docker cp 本機目录 容器目录| 本機目录下所有檔案復製到容器目录| 
|docker export 容器名| 以 tar 壓縮黨案形式導出容器內容|
|docker exec 容器名 參數 . . .| 在現有容器中運行命令，在對於調試用| 
|docker wait 容器名|等待容器終止並返回退出代碼|
|docker commit 容器名 |影像擋提交一個新的 docker 快照|


**注意**： <font color="#FF1000">[  ]</font>  內为，選擇性資料。不加即代表全部。


### 应用

```
$ docker ps -a

CONTAINER ID   IMAGE        COMMAND      CREATED              STATUS 
2b291251a415   debian:7.5   "hostname"   About a minute ago   Exited (0) 1 minutes 
6d36a2f07e18   debian:7.5   "false"      2 minutes ago        Up 2 minutes 

# 執行中的容器要先停止
$ docker stop 6d36a2f07e18

# 删除所有僵尸容器
$ docker container prune

WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y 
Deleted Containers:
2b291251a415
6d36a2f07e18
0f563f110328
```



# 映像基本要素

Docker 容器映像是一個輕量級、獨立的可執行軟件包，其中包括運行應用程序所需的一切：代碼、運行時、系統工具、系統庫和設置。 容器鏡像在 docker 運行時即成為容器。


## 映像管理命令

|命令|解釋|
|:---|:---|
|docker images| 列出所有本地圖像 |
|docker history 映像名|顯示圖像歷史列表| 
|docker inspect 映像名|以 json 格式顯示低級信息|
|docker tag 映像名 标记名 |映像加标记| 
|docker commit container 映像名|从容器创建图像|
|docker import url - [tag] | 从 tarball 创建图像|
|docker rmi 映像名|删除图像|


### 应用


```
# 列出 Volume 在实体主机的真实路径
$ docker inspect -f '{{.Mounts}}' 4c2a9ef663c2


# 拆除所有未被执行的映像档， images -a -q 是只列出映像 ID 部分，-a 是加到列表。-q 为只列出 ID 部分
$ docker rmi $(docker images -a -q)



```

**注意**：4c2a9ef666c2 为容器 ID。为开启容器後能看的如：root@4c2a9ef666c2。

## 映像传输命令

### 使用注册表 API

|命令|解釋|
|:---|:---|
|docker pull repo[:tag] |从注册表中提取映像或存储库 |
|docker push repo[:tag]|从注册表推送映像或存储库|
|docker search 搜索字段| 在官方注册表中搜索映像|
|docker login |登入注册表| 
|docker logout |登出注册表|

### 应用

```
# is-offical=true 搜寻官方网站有关ubuntu 的映像文件
$ docker search ubuntu -f is-offical=true

# 下载 ubuntu
$ docker pull ubuntu

# 显示所有已下载的文件
$ docker images

# 執行 ubuntu 外壳
$ docker run -it ubuntu /bin/bash
```

### 手动轉移

|命令|解釋|
|:---|:---|
|docker save repo[:tag]|将映像或存储库导出為 tarball |
|docker load|从 tarball 加载映像|
|docker-ssh |用脚本通过 ssh 进程之间传输映像|


### 应用


```
# 将映像 hello 儲存為 hello.tar， -o 为输出档案
$ docker save -o hello.tar hello

# 将映像 hello.tar 解压为映像， -i 为解压档案
$ docker load -i hello.tar
```


## 建構工具

|命令|解釋|
|:---|:---|
|FROM 映像名 |构建的基础映像|
|MAINTAINER 名稱|維護人名稱成 E-mail|
|COPY path dst |将上下文中的路径复制到位置目標的容器中|
|ADD src dst |与 COPY 相同，但会解压相关文档，并接受网络文件|
|RUN|放 Linux 指令，用来执行安装和设定这个 Image 需要的东西|
|ARG|编译的过程中，引入的参数作为后续的环境变数使用|
|ENV|設定環境變數|
|ENTRYPOINT|启动容器时最先执行的指令|
|CMD|在 docker run 内執行的指令|
|VOLUME|在容器內定义匿名数据卷|
|WORKDIR|应用程式执行位置|
|LABEL|在映像中以键值形式添加元素|

### Dockerfile

```
# 基础映像：最新的 Debian 版本
FROM debian

# 创建 storage 目錄到映像內
VOLUME ["/storage"]

# 維護人名稱
MAINTAINER hkdickyko@gmail.com

# 键值形式添加元素
LABEL Owner="dicky"
LABEL Version="1.0"

# 安装最新的升级
RUN apt-get update && apt-get -qqy dist-upgrade

# 安装 nginx
RUN apt-get -qqy install nginx

# 设置默认容器命令 # -> 在前台运行 nginx
CMD ["nginx", "-g", "daemon off;"]

# 告诉将会监听 tcp 端口 80
EXPOSE 80

# RUN apt-get -qqy install nginx
# 相当于 RUN [”/bin/sh”, ”−c”, ”apt-get -y install nginx”]

```


- 注释以 <font color="#FF1000">#</font> 开头
- 命令可以用 <font color="#FF1000">＼</font> 继续換行
- 第一句開始必须是 <font color="#FF1000">FROM</font>



#### 使用 scratch 创建一个简单镜像

- 用最少的资源制作一个可执行的文件，在 docker 下執行。

[网上资源](https://github.com/docker-library/hello-world)

```
# dockerfile
FROM scratch
ADD hello /
CMD ["/hello"]
```

- 例子

```
# 编译目前档案为映像 hello
$ docker build --tag hello .

# 在编译是不用快取文件
$ docker build --tag hello . --no-cache

# 查阅映象文件内容
$ docker inspect hello

# 执行已编译的映像
$ docker run hello
```