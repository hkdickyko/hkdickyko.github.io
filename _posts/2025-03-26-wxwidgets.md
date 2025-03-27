---
category: [編程]
tags: [IoT, 電子]
title: wxWidgets
date: 2025-03-26 1:00:00
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
  }
</style>

# wxWidgets 

## 下载

[wxWidgets - 网路资源](https://www.wxwidgets.org/downloads/)


## 安装方法

[wxWidgets - 安装方法](https://wiki.wxwidgets.org/Compiling_and_getting_started)

wxWidgets 是一个跨平台系统，它不会隐藏平台。当在不同系统中从源代码编译 wxWidgets 时，安装在不同的操作系统之间会略有不同。这在 Linux 衍生平台和 Windows 平台之间处理编译库的方式上尤为明显。以下是并排的不同结构。请注意，使用的是相同的源。以下是库结构作为示例（它仅显示相关文件夹）。

![Alt X](../assets/img/linux/wxroadmap.png)

可以使用上面的 wxWidgets 框图来了解编程细节

安装所有必要的构建工具，包括 g++ 和 autotools。在许多发行版中，执行此操作的一种简单方法是安装 **build-essential** 包。

```sh
sudo apt install build-essential
sudo apt install libgtk2.0-dev             
sudo apt install libgtk-3-dev
```

## 编译构建库

将压缩文件解压到 **~/Desktop/wxWidgets-3.2.7** 文件夹中

```
cd ~/Desktop/wxWidgets-3.2.7
mkdir gtk-build              
cd gtk-build
../configure                # 构建 unicode、共享库
make -j3                    
sudo make install          
sudo ldconfig               # 并非每个系统都要求
```

## 测试安装

```sh
wx-config --version  # 3.2.7
wx-config --list     # gtk3-unicode-3.21
```

## wxWidgets 类层次

![Alt X](../assets/img/linux/wxposter.png)
