---
category: [積體電路]
tags: [IoT, 電子]
title: IMU 芯片校正
date: 2024-11-03 1:00:00
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

# IMU 芯片校正 (I<sup>2</sup>C 接口)

## 工具

僅 I<sup>2</sup>C 驱动程序链接 : [allanbian1017/i2c-ch341-usb](https://github.com/allanbian1017/i2c-ch341-usb) 

用以下方法编译及安装

```
make
sudo insmod i2c-ch341-usb.ko
sudo chmod 777 /dev/i2c-x
```
注 **x** 为 I<sup>2</sup>C 接口编号

## USB 连接电脑 CH341A

![Alt X](../assets/img/esp/usbch341a.png)


## Python (Visual Studio Code)

[网上安装资讯](https://code.visualstudio.com/docs/languages/python)

### 简短叙述

#### 需要安装插件

![Alt X](../assets/img/esp/python.png)

![Alt X](../assets/img/esp/pylint.png)

![Alt X](../assets/img/esp/bformat.png)

![Alt X](../assets/img/esp/pydebug.png)

![Alt X](../assets/img/esp/jupyter.png)


#### 自动完成和 IntelliSense

**Python** 扩展使用当前选定的解释器支持代码完成和 IntelliSense。 IntelliSense 是许多功能的统称，包括跨所有文件以及内置和第三方模块的智能代码完成（上下文方法和变量建议）。

IntelliSense 可在键入时快速显示方法、类成员和文档。还可以随时使用 **Ctrl+Space** 触发完成。将鼠标悬停在标识符上将显示有关它们的更多信息。

### 安装 **Python** 虚拟环境

**Python** 扩展会自动检测安装在标准位置的 Python 解释器。它还会检测工作区文件夹中的 conda 环境以及虚拟环境。

当前环境显示在 VS Code 状态栏的右侧：

![Alt X](../assets/img/esp/environsbar.png)

状态栏还会指示是否未选择解释器：

![Alt X](../assets/img/esp/interpretersbar.png)

所选环境用于 IntelliSense、自动完成、linting、格式化和任何其他与语言相关的功能。当在终端中运行或调试 Python 时，或者当使用终端：创建新终端命令创建新终端时，也会激活它。

要更改当前解释器（包括切换到 conda 或虚拟环境），请在状态栏上选择解释器名称或使用 Python：选择解释器命令。

![Alt X](../assets/img/esp/selintep.png)


## 虚拟环境

虚拟环境是创建环境的内置方式。虚拟环境会创建一个文件夹，其中包含指向特定解释器的副本（或符号链接）。当将软件包安装到虚拟环境中时，它将最终位于这个新文件夹中，从而与其他工作区使用的其他软件包隔离。

注意：虽然可以将虚拟环境文件夹作为工作区打开，但不建议这样做，并且可能会导致使用 Python 扩展时出现问题。

Conda 环境

conda 环境是使用 conda 软件包管理器管理的 Python 环境（请参阅 conda 入门）。在 conda 和虚拟环境之间进行选择取决于的打包需求、团队标准等。

Python 环境工具

下表列出了与 Python 环境相关的各种工具：


|工具|定义和目的|
|:---:|:---:|
|pip|安装和更新软件包的 Python 包管理器。默认情况下，它与 Python 3.9+ 一起安装。如使用 Debian 的操作系统；请安装 python3-pip|
|venv|允许管理不同项目的单独软件包安装，并且默认与 Python 3 一起安装，如使用 Debian 的操作系统；请安装 python3-venv|
|conda| 与 Miniconda 一起安装。它可用于管理软件包和虚拟环境。通常用于数据科学项目。|

 - 显示命令面板 <font color="#FF1000">Ctrl + Shift + p</font> 
 - 快捷格式化代码 <font color="#FF1000">Alt + Shift + F</font>

## 安装虚拟环境

在 vs code 创建一个空文件夹，选择该文件夹将成为“工作区”。然后打开 **命令面板** <font color="#FF1000">Ctrl + Shift + p</font>，键入 <font color="#FF1000">Create Environment</font> 命令进行搜索，然后选择该命令。该命令显示环境类型列表，Venv 或 Conda。

![Alt X](../assets/img/esp/createpy.png)

下面以 venv 为例，展示创建虚拟环境的过程，Venv 与 Conda 的过程基本一样：

![Alt X](../assets/img/esp/venv.png)

然后选择需要的解释器版本如下：

![Alt X](../assets/img/esp/pyversion.png)


## 安装套件

回到 VS Code 命令面板。开启一个新的 Python Terminal。

```
pip install [package]
```

## 備份已安裝套件版本

```
pip freeze > requirements.txt
```

使用 pip 安装新的 library 前把现有的 libraries 列表汇出到 requirements.txt，那么如果新的 library 不兼容于现专案，可以使用 requirements.txt 还原专案


## 还原已安裝套件版本

```
pip install -r requirements.txt
```

requirements.txt 就是一個橋樑。透過先前匯出的 requirements.txt，可以用於還原所有在該虛擬環境已安裝的 Python library。

## 更新已安裝套件

```
pip install --upgrade [package]
```

留意當更新一個 Library 的時候，其實會同時把它的 dependencies 也更新至 Library 最新版的要求。


## pylint

打开 **命令面板** <font color="#FF1000">Ctrl + Shift + p</font>，启用 pylint:

![Alt X](../assets/img/esp/pylint-1.png)

![Alt X](../assets/img/esp/pylint-2.png)

以上步骤相等于直接更改 setting.json 如下:

![Alt X](../assets/img/esp/pylint-3.png)

## Black formatter

打开 **命令面板** <font color="#FF1000">Ctrl + Shift + p</font>，直接修改 **setting.json**

![Alt X](../assets/img/esp/vscsetting.png)
 
```
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
```

## Schema 

- Schema 描述文档的结构。XML Schema 语言也称为 XML Schema Definition（XSD）

![Alt X](../assets/img/esp/schema.png)

主要目的是定义资料结构。方便观察资料是否正确。例子如下。

![Alt X](../assets/img/esp/schema-sample.png)


## Python

### Python中 ()，[]，{}

小括号（）：
 - 代表 **tuple** 元祖数据类型，元祖是一种不可变序列。

中括号 []：
 - 代表 **list** 列表数据类型，列表是一种可变序列。
    - 关于 [:j] 或者 [:i]：这是切片操作，在下标 i 或者 j 之前的元素都保留。
    - 关于 [:,j] 或者 [:,i] ：这也是切片操作，不同的是：保留第一个维度所有元素，第二维度元素保留到j；只适用 **numpy** 的科学数据结构。
    - 关于 [::]，[start: end : step ] 操作（高阶用法，可看可不看，一般出现在矩阵数据替换运算）。在 list 中可以用在元素层面，在 **numpy** 的数学数据中可以用在任何层面。

花括号 {}：
 - 代表 **dict** 字典数据类型，字典是Python中唯一内建的映射类型。字典中的值没有特殊的顺序，但都是存储在一个特定的键（key）下。键可以是数字、字符串甚至是元祖。

## Python 组件

![Alt X](../assets/img/esp/pypackage.png)

![Alt X](../assets/img/esp/pylib.png)

![Alt X](../assets/img/esp/pyframework.png)

## Python 循环

![Alt X](../assets/img/esp/pyloop-1.png)

- for

![Alt X](../assets/img/esp/pylistc-1.png)

-for 及 if

![Alt X](../assets/img/esp/pylistc-2.png)

- for 及 for

![Alt X](../assets/img/esp/pylistc-3.png)

- break

![Alt X](../assets/img/esp/pybreak.png)

## Python Array

![Alt X](../assets/img/esp/pyarray.png)

- find():

```py
let numbers = [4, 9, 16, 25];
let firstSquareGreaterThan10 = numbers.find((number) => number > 10);
console.log(firstSquareGreaterThan10); // Output: 16
```

 - filter():

```py
let ages = [18, 22, 15, 30];
let adults = ages.filter((age) => age >= 18);
console.log(adults); // Output: [18, 22, 30]
```

 - map():

```py
let numbers = [1, 2, 3, 4];
let squares = numbers.map((number) => number * number);
console.log(squares); // Output: [1, 4, 9, 16]
```

 - reduce():

```py
let numbers = [1, 2, 3, 4];
let sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum); // Output: 10
```

- forEach():

```py
let fruits = ['apple', 'banana', 'orange'];
fruits.forEach((fruit) => {
    console.log(fruit);
});
// Output: apple, banana, orange
```

注意事项

 - 使用 map() 转换数组
 - 链式数组方法让代码更简洁
 - 对于单元素搜索，优先使用 find 而不是 filter
 - 使用 reduce() 聚合数据
 

常见错误

 - 修改 map() 中的原始数组
 - 使用 forEach() 返回新数组
 - 滥用 find() 查找多个元素
 