---
category: 積體電路 
tags: [IoT]
---

# I<sup>2</sup>C bus 的 pull-up 電阻設計

![Alt i2C](../assets/img/i2c/i2cpr.png)

I<sup>2</sup>C bus 的 pull-up 電阻設計，是一個兩難的局面：

 - R<sub>p</sub> 很小：low-to-high 的變化速度會很快，clock速度沒有限制，但影響 low 的位準。
 - R<sub>p</sub> 很大：low-to-high 的變化速度會太慢，low 的位準沒有問題，但限制 clock 速度。


I<sup>2</sup>C 規格中定義的 V<sub>IL</sub>，也就是 0.3 V<sub>CC</sub>，才能讓其它裝置覺得 bus 的狀態是 low。

根據 I<sup>2</sup>C 的規範，在 100 KH<sub>z</sub> 的 standard mode 和 400 KH<sub>z</sub> 的 fast mode 下，I<sup>2</sup>C 裝置最少要能驅動 3 mA 的電流。

首先計算 V<sub>IL</sub>：

 > <center>V<sub>IL</sub> = V<sub>CC</sub> * 0.3 </center>
 > <center>= 3.3V * 0.3</center>
 > <center>= 0.99 V</center>

因此最少要將訊號線拉到 0.99 V。此時 R<sub>p</sub> 上的電位差就是：3.3 – 0.99 =2.31 V

如果 output driver 最大可以流過 3 mA 的電流，用 3 mA 的電流要造出 2.31 V 的壓差，電阻就是：

 > <center>V = IR</center>
 > <center>2.31 = 0.003 * R</center>
 > <center>R = 770(Ω)</center>

如果將 SCL 或 SDA 拉到 0 V，就要在 R<sub>p</sub> 上造出完整的 3.3 V 壓差，這時的電阻值就是：

 > <center>V = IR</center>
 > <center>3.3 = 0.003 * R</center>
 > <center>R = 1100(Ω)</center>

T<sub>R</sub>上升時間受總線的寄生電容和上拉電阻影響

![Alt i2C](../assets/img/i2c/i2c.png)

# 寄生電容問題

寄生電容，也稱為`雜散電容`，是電路中電子元件之間或電路模塊之間，由於相互靠近所形成的電容，寄生電容是寄生元件，是不可避免的。在任意兩段導體之間均有非零的電容，這種電容在高頻情況中體現得尤為突出。

這個電路中，電容器上的電壓可以用一個看起來很恐怖但其實很簡單的數學式來表示：

 ![](https://latex.codecogs.com/svg.latex?\Large&space;V_{(t)}=V_{cc}\times(1-e^{\frac{-t}{RC}}))

## 電阻與頻率的關係如下圖

![Alt i2C_RC](../assets/img/i2c/fRcgx.png)

# 結論

上升時間(T<sub>r</sub>)和下降時間T<sub>f</sub>直接受到上拉電阻和總線寄生電容的影響。 如果上拉電阻太高，則T<sub>r</sub>和T<sub>f</sub>會很大；反之， 降低總線速度，如果上拉電阻太小，則會導致功耗過大。

如果總線上只有一個從機（走線長度較短），則可以使用內部上拉電阻（〜30K），更優的方案是使用外部電阻。

一般而言，在 3.3 V、400 KH<sub>z</sub> 以下，且裝置數量少於 10 個、電路板又不大的狀況下，2.2 KΩ 到 4.7 KΩ 這樣的數值幾乎可以滿足大部分的設計，但經過以上說明，希望讀者可以更加了解 pull-up 電阻與 I<sup>2</sup>C bus 電路設計之間的關係，在需要時知道如何計算。