---
category: [ Android]
tags: [Android]
title: Android 命令行编程
date: 2023-10-14 1:00:00
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

## 安装 ubuntu 平台

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
apt update
apt upgrade
apt install aapt

# 以下 jdk 版本可能需要更新
apt install openjdk-19-jre
apt install openjdk-19-jdk
```


## 下载 Android 命令行工具


从 [Android 网站](https://developer.android.com/studio) 下载适用于 Linux 的 Android 命令行工具


将**命令行工具**解压到硬盘，它将被移动到下面命令中的相关位置

## 安装命令行工具

```
cd ~
export ANDROID_HOME=$HOME/android/sdk

# 移动 cmdline-tools 目录中的文件到下面命令中的相关位置及设置链接
mkdir -p $ANDROID_HOME/cmdline-tools
mv cmdline-tools $ANDROID_HOME/cmdline-tools/latest
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin

# 修复相关的依赖关系
JAVA_OPTS=-Dos.arch=amd64 sdkmanager emulator

# 安装目标编译平台
sdkmanager 'platforms;android-26'
```