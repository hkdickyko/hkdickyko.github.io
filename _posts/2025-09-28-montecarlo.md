---
category: [数学]
tags: [数学, 编程]
title: Monte Carlo Algorithm (蒙地卡罗算法)
date: 2025-09-28 00:00:01
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

# 蒙地卡罗算法


蒙特卡洛算法的核心原理是利用随机数和概率统计方法来模拟问题，通过大量随机样本的采样，得到问题的概率分布或期望值。这种方法特别适用于那些无法用精确数学公式求解的问题，或者公式求解非常困难的问题。它非常强大和灵活，很容易实现。对于许多问题来说，它往往是最简单的计算方法，有时甚至是唯一可行的方法。

蒙地卡罗实际上是一种很广泛的称呼，只要**透过大量取样来逼近某真实状况的方式**，精神是「随机抽样，统计逼近」。都可以称作蒙地卡罗算法。

在解决实际问题的时候应用蒙地卡罗方法主要有两部分工作：

 - 用蒙地卡罗方法类比某一过程时，需要产生各种机率分布的随机变数
 - 用统计方法把模型的数字特征估计出来，从而得到实际问题的数值解


蒙特卡洛算法的具体实现步骤如下：

 1. **定义问题**：首先需要明确问题的数学模型和目标函数，以及待求解的变量或参数。
 2. **随机采样**：生成随机样本，一般是均匀分布或正态分布的随机数，根据采样规则，将随机数映射到问题的定义域内，得到一组采样点。
 3. **模拟计算**：将采样点代入目标函数中，得到目标函数的函数值，根据函数值的大小关系，统计满足条件的样本数目，得到目标函数在采样区域内的估计值。
 4. **统计分析**：根据大数定律和中心极限定理，利用采样得到的数据，计算问题的期望值、方差、置信区间等统计量，并根据结果进行进一步的分析和推断。

## 算法的优点
 - 是简单易懂
 - 不需要对问题的具体结构做出太多的假设
 - 可直接利用计算机生成大量随机数进行计算

解决了许多传统方法难以解决的问题。

## 算法的缺点
 - 收敛速度较慢
 - 计算量较大
 - 精度不高等问题

需要根据具体问题的特点来选择合适的方法和技巧。

需要注意的是，蒙特卡洛算法的计算结果可能存在一定的误差，因为估计值是通过随机样本计算得到的。因此，在实际应用中需要考虑样本数量、采样方式、计算精度等因素，以得到可靠的计算结果。


例子如下：

工作原理就是两件事：
 - 不断抽样
 - 逐渐逼近

用以下例子来理解一下这个方法的思路


## 基本应用例子 (圆周率)


有一个半径为 $r=1$ 的圆和边长为 1 的正方形，圆的面积为，则正方形内部的相切圆的面积为整个圆的 1/4，也就是 ，正方形的面积为 1。然后向正方形中随机打点，就会有一定的概率落在圆中：


![Alt X](../assets/img/math/pi-30k_orig.gif)


这样就可以得到

$$
落在圆中的概率就是 = \frac {圆的面积}{正方形面积} = \frac {\pi}{4} 
$$
，那么就可以推出圆周率的计算公式：

$$
\pi = 4 \times 落在圆中的概率  = 4 \times \frac {红色点数}{总点数}
$$

随机点数的增加，近似度逐渐增大。


```py
import random
import math

def estimate_pi_monte_carlo(num_points):
  inside_circle = 0
  for _ in range(num_points):
    # 生成介于 0 和 1 之间的随机 x 和 y 坐标
    x = random.uniform(0, 1)
    y = random.uniform(0, 1) 
    distance = x**2 + y**2
    if distance <= 1: # 检查点是否落在单位圆内 (半径 = 1)
      inside_circle += 1
  # 四分之一圆内点数与总点数之比近似于圆面积与正方形面积之比。
  # 四分之一圆面积 = πr²/4。当 r=1，圆面积 = π/4。正方形面积 = 1。
  # 圆内点数/总点数 约为 π/4，所以 π 约为 4*(圆内点数/总点数)。
  pi_estimate = 4 * (inside_circle / num_points)
  return pi_estimate

num_simulations = 1000000
estimated_pi = estimate_pi_monte_carlo(num_simulations)
print(f"用 {num_simulations} 点估计的 π 值：{estimated_pi}")
delta = 100 - estimated_pi *100 / math.pi
print(f"估计的 π 值相差：{delta:.3f}%")
```

# 采样方法（中央极限定理）

根据中央极限定理(Central Limit Theorem，CLT)，无论总体分布如何，只要随机独立样本量够多，这些相互独立的随机变数会依照分布收敛成<font color="#FF1000">常态分布</font>。

![Alt X](../assets/img/math/ndistribution.png)

若随机变量X服从一个位置参数为 $\mu$ 、变异数 (尺度参数) 为 $\sigma$ 的机率分布，

$$ X \sim N(\mu,\sigma^2) $$

![Alt X](../assets/img/math/nd_pdf.png)

如下需要计算 $a$ 到 $b$ 的面积


$$
F = \int ^b _a f(x)dx
$$


![Alt X](../assets/img/math/mcintegration.png)

# 蒙地卡罗积分

蒙地卡罗积分（Monte Carlo integration）是一种使用乱数进行数值积分的技术。它是一种特殊的蒙地卡罗方法，可对定积分进行数值计算。其他演算法通常在规则网格上评估被积函数，而蒙地卡罗随机选择被积函数评估的点。该方法对于高维积分特别有用。

以下例子介绍蒙地卡罗积分方法，换算成数学的概念可以写成：

$$
F = \int ^b _a f(x)dx \approx \frac {1}{N} \sum ^N _{i=1} \frac {f(x_i)}{pdf(x_i)}
$$

$pdf$ 为函数的机率密度函数，当然先以<font color="#FF1000">均匀分布</font>为主，也就是 


$$
pdf(x_i) = \frac {1}{(b-a)}
$$


$$
F \approx \frac {1}{N} \sum ^N _{i=1} \frac {f(x_i)}{\frac {1}{(b-a)}} \approx
\frac {(b-a)}{N} \sum ^N _{i=1} f(x_i)
$$


$$
常态分布下的常数 = C = \frac {(b-a)}{N}
$$

$$
函数积分总和 = X= \sum ^N _{i=1} f(x_i)
$$

## 应用例子

### 积分公式

以下例子是透过蒙地卡罗积分来估计一下指数分布在闭区间 0~5 的积分值是多少。

$$
\lambda \cdot e^{-\lambda \cdot x}
$$

```py
# 估計指數分布 (λ=1) 於閉區間 0 ~ 5 積分
# 指數分布公式 : λ * e^(-λx)
# 積分公式解 ： 1-e^(-λx) | (0~5) : 0.993262053

import numpy as np
    
def target_exp_function(x, lb=1):
  return lb*np.exp(-lb*x)  

def simple_monte_carlo(a, b, N=100000):
  C = (b-a) / N
  X = np.random.uniform(low=a, high=b, size=N)
  return C * sum(target_exp_function(X))

if __name__ == "__main__":
  for m in (100, 1000, 10000, 100000):
    answer = simple_monte_carlo(0, 5, N=m)
    print('估计样本数量 : ', m)
    print('蒙特卡罗计算的答案 : ', answer)
    delta = (answer-0.993262053)*100/0.993262053
    print(f'积分相差的百分比(%) : {delta:.3f}%')
```

注意：当然可以不用**常态分布**作为取样分布，而是选择认为比较合适的分布，但一般以简单原因，<font color="#FF1000">常态分布</font>的模拟还是很常见使用。但如不使用**常态分布**， $pdf$ 函数的机率密度函数需要作出相应调整。


### 圆周率

以下例子用积分方法，计算圆周率用作比较之前部份介紹的基本蒙地卡罗算法。随著以下的 **Python** 代码，能看到蒙地卡罗算法代码基本步骤是固定不变。


```py
import numpy as np
import math
    
def target_exp_function(x):
   return np.sqrt(1-x*x)

def simple_monte_carlo(N=100000):
  C = 1/ N
  X = np.random.uniform(low=0, high=1, size=N)
  return C * sum(target_exp_function(X))

if __name__ == "__main__":
  for m in (100, 10000, 1000000):
    answer = 4*simple_monte_carlo(N=m)
    print('估计样本数量 : ', m)
    print('蒙特卡罗计算的答案 : ', answer)
    delta = (answer-math.pi)*100/math.pi
    print(f'积分相差的百分比(%) : {delta:.3f}%\n')
```

# 統計誤差（抽樣誤差）

蒙特卡羅模擬中最常見的誤差類型是統計誤差。它的產生是因為結果是基於有限數量的隨機樣本。根據中心極限定理，此誤差通常隨樣本數 $N$ 的平方根減小，這意味著要將誤差減半，需要將樣本數增加四倍。

$$
 抽樣誤差 \quad \alpha \quad \frac{1}{\sqrt{N}}
$$ 