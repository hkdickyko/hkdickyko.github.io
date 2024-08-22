---
category: 電子
tags: [IoT,電子]
title: 电容 和 火牛
date: 2024-06-22 00:34:36
---

<style>
  table {
    width: 100%
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


# 电容

## 滤波电容设计

假设变压器输出端的额定值为 12 V 和 4 A（直流值），假设电网频率为 50 Hz，因此周期为 T=20 ms，假设纹波为 10%。在这种情况下 $$ \Delta V = 1.2V $$，则 C 的表达式及其值为：


$$ C = \frac {Q}{U} = \frac {I \times \Delta t}{\Delta V} = \frac {P_{in}} {V_{max} - \frac {\Delta V}{2}} \times {\frac {\Delta t}{\Delta V} }
$$

即

$$
V = \frac {4 \times 0.01}{1.2} = 0.0333 F = 
$$


因为在带有电容器的全波桥式整流器中，它会放电约半个周期 $$ \Delta t = \frac {T}{2} $$，然后在下一个交流峰值时重新充电。