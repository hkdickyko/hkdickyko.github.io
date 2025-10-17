---
category: [編程]
tags: [IoT, 電子]
title: Python AutoCAD
date: 2025-10-05 20:00:00
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

# PyAutoCAD 介绍

利用 Python 实现自动 AutoCAD 绘制图是利用 Python 实现自动操作 Autocad 库，把 AutoCAD 操作技巧指令化。pyautocad 封装了一下接口，加入了一些迭代方式和 table 操作，可以导入导出 excel 等文本数据。

 - 以下是最基本的例子

```py
# 导入模块
from pyautocad import Autocad
# 创建cad实例
acad = Autocad(create_if_not_exists=True)
# 在 AutoCad 控制面板中输出
acad.prompt("Autocad 基本 Python 操作模块\n")
```

## 基本了解的 Python 技巧


### F 或 f 字符串

F 字符串提供了一种更简洁易读的字符串格式化方法，于 Python 3.6 中引入以 f 或 F 为前缀，允许直接在花括号中嵌入表达式。


```py
city ​​= "香港"
greeting = f"欢迎来到 {city}！"
print(greeting)
```

### 字符串.format()

对包含这些占位符的字符串调用 str.format() 方法。要插入的值将作为参数传递给 format() 方法。


```py
city ​​= "香港"
greeting = "欢迎来到 {}！".format(city)
print(greeting)
```

 - 还可以使用位置参数，用参数输出需要的顺序。


```py
city ​​= "香港"
tutor = "旅游"
greeting = "欢迎来到 {1}{0}！".format(tutor, city)
print(greeting)
```

### Python 格式化小数点

可以使用 f 字符串 (f'{x:.nf}')、str.format() 方法 ('{:.nf}'.format(x)) 或 format()。 

 - **:** 为显示开始格式
 - **.n** 为指定保留 n 位小数
 - **f** 为小数字变发化为浮点数

### 总结 

f-string 和 format() 的用法有以下几个优点：

 - 字串更清楚易读，不需要使用 **+** 号来连接字串和变数
 - 多种格式化选项，如指定对齐方式如小数、位数、进位制等
 - 字串中可用任何有效的 Python 表达式，如算术运算、函数呼叫等



## SendCommand 方法

  在个别情况下，采用常规方式很难实现某一功能，如设定预设视图、定义永久标注样式等。这时可尝试采用 **SendCommand** 方式来实作。 具体方法是先在AutoCAD 软体介面操作一遍，然后记录在此过程中的步骤，将这步骤稍加改动以 pyhon 字符串形式输入到 SendCommand 内，即可得到对应的 Python 程式码。

注意 SendCommand 可以用 ' ' 空格或者 \n 作为输入 **Enter** 的功能键。   


以下例子供参考

**注意**：等候时间。是为了避免太多电脑指令，使电脑应对错误，不同的硬件设置需要作出调整。

```py
def main():
  # 导入相关 AutoCAD 设置资料，及需要列印 AutoCAD 图名称
  lines = []
  with open('d:/acad.dat', 'r') as file:
    for line in file:
      lines.append(line.strip())
  inpath = lines[0]
  outpath = lines[1]
  filename = lines[2]
  plotname = lines[3]
  print(f"原图 DWG 目录 = {inpath}")
  print(f"输出 PDF 目录 = {outpath}")
  print(f"已设定 Named Plot 图 = {filename}")
  print(f"Name plot 名称 = {plotname}")
  lines = lines[4:]
  print(lines)
  
  acad = Autocad() # 加载 pyautocad
  file_path = inpath + filename + ".dwg"
  for curfilename in lines:
    cfile_path =  inpath + curfilename + ".dwg"
    acad.app.Documents.Open(cfile_path)
    doc = acad.doc
    doc.SetVariable('REGENMODE', 0) # 关闭重新绘图模式
    doc.SetVariable('PROXYNOTICE', 0) # 关闭重新绘图模式
    doc.SendCommand('filedia\n0\n') # 禁用弹出式对话框
    # 在图中载入巳设定的 Named Plot 资料
    doc.SendCommand(f'_-PSETUPIN\n{file_path}\n{plotname}\n\n')
    plotset = "DWG To PDF.pc3"
    for layout in doc.Layouts:
      if layout.Name != "Model" :
        lname = outpath + layout.Name
        acad.doc.SetVariable('BACKGROUNDPLOT', 0)
        acad.doc.SendCommand("\n")
        acad.doc.SendCommand(f'_-PLOT\nN\n{layout.Name}\n{plotname}\n{plotset}\n{lname}\nN\nY\n')
        print(f"------\n{lname} is printing to pdf.")
        time.sleep(10) # 等候时间使 AutoCAD 有时间操作列印 pdf 档案
        print(f"{lname} was printed to pdf.")      
        time.sleep(1)  # 等候时间使 AutoCAD 有时间操作，关闭档案
    doc.Close(False)
```