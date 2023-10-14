---
category: [ Android]
tags: [Android]
title: Android 命令行编程
date: 2023-04-28 1:00:00
---


# Android 命令行编程

## 安裝 termux

从 F-Droid 或 goole playstore 安装 termux。

## 更新 termux

```
apt update
apt upgrade
apt update
termux-setup-storage
```

## 安装 ubuntu

```
apt install git wget proot
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
cd ubuntu-in-termux
bash ubuntu.sh -y
sed -Ei 's|(:/bin)(:/usr/bin):|\2\1:|' startubuntu.sh
./startubuntu.sh
```

## 安装 Android SDK 构建工具

```
pkg install aapt2
pkg install apksigner
```

## 下载 Android 命令行工具


从 [Android 网站](https://developer.android.com/studio) 下载适用于 Linux 的 Android 命令行工具



