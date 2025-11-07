---
category: [软件]
tags: [Android]
title: Androidide
date: 2023-11-19 1:00:00
---

<style>
  table {
    width: 100%git clone https://github.com/hkdickyko/hkdickyko.github.io
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

# Androidide

从 [Androidide 网站](https://androidide.com/docs/installation) 下载 Android ide 工具

## 安装更正

位置错误 '
/data/data/com.itsaky.androidide/files/home/android-sdk/cmdline-tools/latest' (Expected '
/data/data/com.itsaky.androidide/files/home/android-sdk/tools')

cmdline-tools/latest 改为 tools 大至方法如下:

```
cd android-sdk/cmdline-tools
mv latest ../
cd ..
mv latest tools
rm -rf cmdline-tools
```

## 使用 Gradle 创建发布签名的 apk 文件

signingConfigs 加 <font color="#FF1000">release</font> 内容及 buildTypes 加上 <font color="#FF1000">signingConfig signingConfigs.release</font> 这句

```
android {
  signingConfigs {    
    release {
      storeFile file('/storage/emulated/0/AndroidIDEProjects/mdnotes/keystore.jks')
      storePassword 'password'
      keyPassword 'password'
      keyAlias 'mdnotes'
  }
}

buildTypes {
  release {
    signingConfig signingConfigs.release
    minifyEnabled true
    proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    debuggable false
    multiDexEnabled true
  }
}
```

## Android 项目的一般目录结构

![Alt x](../assets/img/misc/androidide.png)

## 创建 debug apk

:app:assembleDebug

## 创建 release apk

:app:assembleRelease

## 创建 AAB

:app:bundle

## 全部删除

:app:clean

## 製作报告

:app:check