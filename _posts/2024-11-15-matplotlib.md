---
category: [編程]
tags: [IoT, 電子]
title: Python Matplotlib
date: 2024-11-15 20:00:00
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

# Python Matplotlib 介绍

```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname="./SimHei.ttf", size=18)
font1 = FontProperties(fname="./SimHei.ttf", size=12)

def setText(plt, title, xlabel, ylabel, fontsize=18):
    plt.title(title, fontproperties=font, color="blue")
    plt.xlabel(xlabel, fontproperties=font1)
    plt.ylabel(ylabel, fontproperties=font1)

def plot(plt, x, y, legend, lwidth=1, lstyle="-"):
    plt.plot(x, y, linewidth=lwidth, ls=lstyle, label=legend)

def setPlotView(plt, width, height):
    plt.figure().set_figwidth(width)
    plt.figure().set_figheight(height)

x = [1, 2, 3, 4, 5, 6]
y = [7, 8, 9, 10, 11, 12]
y1 = [3, 7, 2, 1, 8, 3]
y2 = [2, 5, 8, 6, 2, 5]
y3 = [4, 6, 7, 5, 7, 10]

setPlotView(plt, 5, 3)
setText(plt, "樣品圖", "X-軸", "Y-軸")
plot(plt, x, y, "數據-1", 1)
plot(plt, x, y1, "數據-2", 2, "--")
plot(plt, x, y2, "數據-3", 1, "-.")
plot(plt, x, y3, "數據-4", 3, ":")
plt.legend(bbox_to_anchor=(1, 1), fancybox=True, shadow=True, prop=font1)
plt.grid(linestyle=":")
plt.show()
```

![Alt X](../assets/img/python/matplot-1.png)

![Alt X](../assets/img/python/mplotlinestyle.png)

[Matplotlib 网上资源](https://medium.com/@hi-sushanta/master-matplotlib-a-step-by-step-guide-for-beginners-to-experts-e76195edff1f)