---
category: [系統]
tags: [編程]
title: 開放麒麟 (Open Kylin) 使用技巧
date: 2022-07-29 06:00:00
---

# 開放麒麟

下載並安裝至電腦如網站所述: 

[開放麒麟下載](https://www.openkylin.top/downloads/)


安裝其它軟件的方法

<font color="#FF1000">apt-get</font> 但在開放麒麟不能直接使用。有如下錯誤:

```shell
> sudo apt-get update
> [sudo] password for dickyko: 

Get:1 file:/cdrom yangtze InRelease
Ign:1 file:/cdrom yangtze InRelease
Get:2 file:/cdrom yangtze Release
Err:2 file:/cdrom yangtze Release
  File not found - /cdrom/dists/yangtze/Release (2: No such file or directory)
Reading package lists... Done
E: The repository 'file:/cdrom yangtze Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details. 
```
注意: <font color="#FF1000">sudo</font> 是將指今改為 root 指令
以是問題是因為 /etc/apt/sources.list 這檔案係設定。

```shell
> cd /etc/apt
// 保存原檔案
> sudo cp sources.list sources.list.bak
// 列出原檔案內容
> cat sources.list
// 原內容如下
deb http://ppa.build.openkylin.top/packaging/ppa2/openkylin yangtze main
#deb file:/cdrom yangtze main
```
更改 sources.list 內容 (第一行加上 <font color="#FF1000">#</font>)為以下內容，加入更多網上軟件倉庫

```shell
#deb http://ppa.build.openkylin.top/packaging/ppa2/openkylin yangtze main
#deb file:/cdrom yangtze main

deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse

deb http://archive.canonical.com/ubuntu focal partner
deb-src http://archive.canonical.com/ubuntu focal partner
```

加入後會發現仍然有錯誤。原因是<font color="#FF1000">沒有公共金匙</font>來下載倉庫軟件如下


```shell
> sudo apt update
Get:1 http://archive.canonical.com/ubuntu focal InRelease [12.1 kB]
Err:1 http://archive.canonical.com/ubuntu focal InRelease 
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
Get:2 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Err:2 http://archive.ubuntu.com/ubuntu focal InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
Get:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Err:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
Get:4 http://archive.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Err:4 http://archive.ubuntu.com/ubuntu focal-security InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
Get:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Err:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
Reading package lists... Done
W: GPG error: http://archive.canonical.com/ubuntu focal InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
E: The repository 'http://archive.canonical.com/ubuntu focal InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://archive.ubuntu.com/ubuntu focal InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
E: The repository 'http://archive.ubuntu.com/ubuntu focal InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://archive.ubuntu.com/ubuntu focal-updates InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
E: The repository 'http://archive.ubuntu.com/ubuntu focal-updates InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://archive.ubuntu.com/ubuntu focal-security InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
E: The repository 'http://archive.ubuntu.com/ubuntu focal-security InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://archive.ubuntu.com/ubuntu focal-backports InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3B4FE6ACC0B21F32 NO_PUBKEY 871920D1991BC93C
E: The repository 'http://archive.ubuntu.com/ubuntu focal-backports InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

在以上資訊中你會發覺 NO_PUBKEY <font color="#FF1000">3B4FE6ACC0B21F32</font> NO_PUBKEY <font color="#FF1000">871920D1991BC93C</font>

在以上出現的金匙可能會不同。請自尋找顯示的金匙。並用以下指令生成金匙。


```shell
> sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32

Executing: /tmp/apt-key-gpghome.h4o7D1rBQf/gpg.1.sh --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
gpg: key 3B4FE6ACC0B21F32: public key "Ubuntu Archive Automatic Signing Key (2012) <ftpmaster@ubuntu.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1

> sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C
> 
Executing: /tmp/apt-key-gpghome.Fr7e23ni5Y/gpg.1.sh --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C
gpg: key 871920D1991BC93C: "Ubuntu Archive Automatic Signing Key (2018) <ftpmaster@ubuntu.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
```

用以下指令測試是否設定未完成

```
> sudo apt update

Hit:1 http://archive.canonical.com/ubuntu focal InRelease                      
Hit:2 http://archive.ubuntu.com/ubuntu focal InRelease                         
Hit:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:4 http://archive.ubuntu.com/ubuntu focal-security InRelease
Hit:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease
Reading package lists... Done
Building dependency tree       
Reading state information... Done
All packages are up to date.
```

根據以上。列出的資訊已能在網上尋找到適當的軟件倉庫。


















