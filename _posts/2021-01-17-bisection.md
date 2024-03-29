---
category: 編程 
tags: [編程, 數學]
title: 二等分法
date: 2021-01-17 22:34:36
---

# 算法 - 二等分法

二等分法是一種流行的數學和數值方法求根方法。 

該方法適用於查找任何多項式方程f(x）= 0的根，
只要該根位於區間[a，b]內並且f(x）在該區間內是連續的即可。

此方法為封閉括號類型，需要兩個初始猜測。 收斂是線性的，
並且總體上具有良好的準確性。 

與其它根查找方法相比，對分方法由於收斂速度緩慢且穩定，
因此被認為相對較慢。但是對於電腦計算機迭代。 
一般工作中的計算速度不是一個很大的問題。

如下圖所示，

![](https://latex.codecogs.com/svg.latex?\Large&space;x_{2}=\frac{x_{0}+x_{1}}{2})

因當x<sub>0</sub>時的求值為負。，x<sub>1</sub>時的求值為正。
而我們所需要求的數值為零。

而當代入x<sub>2</sub>計算出來的數值為負。
所以x<sub>2</sub>用以代替x<sub>0</sub>。

![](https://latex.codecogs.com/svg.latex?\Large&space;x_{3}=\frac{x_{2}+x_{1}}{2})

而當代入x<sub>3</sub>計算出來的數值為正。
所以x<sub>3</sub>用以代替x<sub>1</sub>。

用以上的計算原理。繼續尋找直到找到 &alpha;，
一般來說我們會設計一個可接受的誤差 &epsilon;。用於減少計算時間。


![](../assets/img/bisection/bisection.png)