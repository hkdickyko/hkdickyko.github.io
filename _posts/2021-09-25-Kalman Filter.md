---
category: [編程]
tags: [Kalman Filter]
title: Kalman Filter
date: 2021-09-25 22:34:36
---
# Kalman Filter (卡爾曼濾波)

是一種利用線性系統狀態，通過系統輸入及輸出數據，它能夠從不完全及包含雜訊的測量中，估計動態系統的狀態。

![Alt Filter](../assets/img/kalman/estimation.png)

## 初始估值 

只執行一次，它提供兩個參數，即使初始化參數不精確，卡爾曼濾波器也能收斂到接近真實值。如果我們用更準確的值初始化，卡爾曼濾波器更快的收斂到近真實值。


### 初始系統狀態值
	
![](https://latex.codecogs.com/svg.latex?\Large&space;X_{0,0})
	
### 初始狀態測量設備誤差

![](https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{0,0})

### 初始化的估計不確定性是誤差方差 
	
![](https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{0,0}^{2})  
	
## 預測估值 (測量值位置從  `1` 開始)

![](https://latex.codecogs.com/svg.latex?\Large&space;X_{index,{\color{Red}status}})

 - index = 測量值編號 (測量值位置) 
 - status = 計算值狀態 (0:初始值或估計值, 1:計算修正估值)
 
### 由於模型具有恆定動態，因此預測估計等於當前初始估值。

![](https://latex.codecogs.com/svg.latex?\Large&space;X_{i,{\color{Red}0}}=X_{i-1,{\color{Red}0}})
	 
![](https://latex.codecogs.com/svg.latex?\Large&space;X_{1,{\color{Red}0}}=X_{0,{\color{Red}0}})

### 延伸估值的不確定性方差 + 估計系統噪聲方差 (R) 在整個估計過程中是固定不變的

![](https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{i,{\color{Red}0}}^{2}=\sigma_{i-1,{\color{Red}0}}^{2}+{\color{blue}\mathbf{R}})

![](https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{1,{\color{Red}0}}^{2}=\sigma_{0,{\color{Red}0}}^{2}+{\color{blue}\mathbf{R}})
	 
## *反復計算*

### 測量值
<hr/>

#### 來自測量設備的測量值
 
![](https://latex.codecogs.com/svg.latex?\Large&space;{\color{DarkGreen}Z_{i}})

#### 來自測量設備誤差為 (測量設備誤差在整個估計過程中是固定不變的)

![](https://latex.codecogs.com/svg.latex?\Large&space;{\color{blue}\sigma_{r}}) 

#### 來自測量設備誤差方差為 (測量設備誤差方差在整個估計過程中是固定不變的)  

![](https://latex.codecogs.com/svg.latex?\Large&space;{\color{blue}\sigma_{r}^{2}})

例如，如果如果設備準確誤差為 0.1 誤差方差為 

![](https://latex.codecogs.com/svg.latex?\Large&space;{\color{blue}0.1}^{2}={\color{blue}0.01})

### 計算卡爾曼增益 (卡爾曼增益介於 `0` 到 `1` 之間)
<hr/>

#### 測量設備誤差在整個估計過程中是固定不變的
 
![](https://latex.codecogs.com/svg.latex?\Large&space;{\color{blue}\sigma_{r}}) 

#### 卡爾曼增益

![](https://latex.codecogs.com/svg.latex?\Large&space;K_{i}=\frac{\sigma_{i,\color{Red}0}^{2}}{\sigma_{i,\color{Red}0}^{2}+{\color{blue}\sigma_{r}}^{2}})

### 更新估值 
<hr/>

#### 新估值 : 增量之間的距離 = (測量值 - 預測估值)

![](https://latex.codecogs.com/svg.latex?\Large&space;X_{i,1}=X_{i,\color{Red}0}+K_{i}\times{({\color{DarkGreen}Z_{i}}-X_{i,\color{Red}0}))
   
#### 更新誤差方差估值 

![](https://latex.codecogs.com/svg.latex?\Large&space;\sigma_{i,1}^{2}={(1-K_{i})}\times\sigma_{i,\color{Red}0}^{2})
   
  
	 
### 預測估值 (下一輪預測開始初始估值)

- 系統噪聲方差 (R) 在整個估計過程中是固定不變的

![](https://latex.codecogs.com/svg.latex?\Large&space;X_{i+1,\color{Red}0}=X_{i,1})

![](https://latex.codecogs.com/svg.latex?\Large&space;{\sigma_{i+1,\color{Red}0}^{2}}={\sigma_{i,1}^{2}+{\color{blue}\mathbf{R}})

#### 如在第一輪計算

![](https://latex.codecogs.com/svg.latex?\Large&space;X_{2,\color{Red}0}=X_{1,1})

![](https://latex.codecogs.com/svg.latex?\Large&space;{\sigma_{2,\color{Red}0}^{2}}={\sigma_{1,1}^{2}+{\color{blue}\mathbf{R}})

## 重複以上 (*反復計算*) 過程