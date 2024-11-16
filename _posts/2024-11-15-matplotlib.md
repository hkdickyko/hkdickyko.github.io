---
category: [編程]
tags: [IoT, 電子]
title: Python Matplotlib
date: 2024-11-10 3:00:00
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


def setText(plt, title, xlabel, ylabel, fontsize＝18):
    font1 = {"color": "blue", "size": fontsize}
    font2 = {"size": fontsize * 4 / 5}
    font3 = {"size": fontsize * 4 / 5}
    plt.title(title, fontdict=font1)
    plt.xlabel(xlabel, fontdict=font2)
    plt.ylabel(ylabel, fontdict=font3)


def plot(plt, x, y, legend, lwidth＝1, lstyle＝"-"):
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
setText(plt, "Sample plot", "X axis", "Y axis")

plot(plt, x, y, "data-1", 1)
plot(plt, x, y1, "data-2", 2, "--")
plot(plt, x, y2, "data-3", 3, "-.")
plot(plt, x, y3, "data-4", 1, ":")

plt.legend(bbox_to_anchor=(1, 1), fancybox=True, shadow=True)
plt.grid()
plt.show()
```

![Alt X](../assets/img/python/matplot-1.png)

![Alt X](../assets/img/python/mplotlinestyle.png)

[Matplotlib 网上资源](https://medium.com/@hi-sushanta/master-matplotlib-a-step-by-step-guide-for-beginners-to-experts-e76195edff1f)