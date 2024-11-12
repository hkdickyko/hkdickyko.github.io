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

[Python 相关资料](https://hkdickyko.github.io/%E7%B7%A8%E7%A8%8B/python)


## 检查 IMU 连接

```py
import time, sys
sys.path.append("../")
t0 = time.time()
start_bool = False  # 如果 IMU 启动失败 - 停止校准
while time.time() - t0 < 5:
    try:
        from mpu9250_i2c import *
        start_bool = True
        break
    except:
        continue
```

在虚拟环境安装 smbus : **pip install smbus**, 否则 IMU 不能连接成功

## mpu9250_i2c.py

```py
def MPU6050_start():
  # 重置所有传感器
  bus.write_byte_data(MPU6050_ADDR,PWR_MGMT_1,0x80)
  time.sleep(0.1)
  bus.write_byte_data(MPU6050_ADDR,PWR_MGMT_1,0x00)
  time.sleep(0.1)
  # 电源管理和振动设置
  bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0x01)
  time.sleep(0.1)
  # 改变样本率（稳定性）
  samp_rate_div = 0 # sample rate = 8 kHz/(1+samp_rate_div)
  bus.write_byte_data(MPU6050_ADDR, SMPLRT_DIV, samp_rate_div)
  time.sleep(0.1)
  # 写入配置寄存器
  bus.write_byte_data(MPU6050_ADDR, CONFIG, 0)
  time.sleep(0.1)
  # 写入陀螺式配置寄存器
  gyro_config_sel = [0b00000,0b01000,0b10000,0b11000] # byte registers
  gyro_config_vals = [250.0,500.0,1000.0,2000.0] # degrees/sec
  gyro_indx = 0
  bus.write_byte_data(MPU6050_ADDR, GYRO_CONFIG, int(gyro_config_sel[gyro_indx]))
  time.sleep(0.1)
  # 写入加速配置寄存器
  accel_config_sel = [0b00000,0b01000,0b10000,0b11000] # byte registers
  accel_config_vals = [2.0,4.0,8.0,16.0] # g (g = 9.81 m/s^2)
  accel_indx = 0
  bus.write_byte_data(MPU6050_ADDR, ACCEL_CONFIG, int(accel_config_sel[accel_indx]))
  time.sleep(0.1)
  # 中断寄存器（与数据溢出有关[FIFO]）
  bus.write_byte_data(MPU6050_ADDR,INT_PIN_CFG,0x22)
  time.sleep(0.1)
  # 在通过模式下启用 AK8963 磁力计
  bus.write_byte_data(MPU6050_ADDR, INT_ENABLE, 1)
  time.sleep(0.1)
  return gyro_config_vals[gyro_indx],accel_config_vals[accel_indx]


def read_raw_bits(register):
  # 读取 ACCEL 和 陀螺仪值
  high = bus.read_byte_data(MPU6050_ADDR, register)
  low = bus.read_byte_data(MPU6050_ADDR, register+1)
  # 结合高和低点以获得没有符号值
  value = ((high << 8) | low)
  # 转换为 + - 值
  if(value > 32768):
    value -= 65536
  return value

def mpu6050_conv():
  # 原始加速位
  acc_x = read_raw_bits(ACCEL_XOUT_H)
  acc_y = read_raw_bits(ACCEL_YOUT_H)
  acc_z = read_raw_bits(ACCEL_ZOUT_H)
  # 原始陀螺仪位
  gyro_x = read_raw_bits(GYRO_XOUT_H)
  gyro_y = read_raw_bits(GYRO_YOUT_H)
  gyro_z = read_raw_bits(GYRO_ZOUT_H)
  # 转换为 G 和陀螺仪 DPS 的加速度
  a_x = (acc_x/(2.0**15.0))*accel_sens
  a_y = (acc_y/(2.0**15.0))*accel_sens
  a_z = (acc_z/(2.0**15.0))*accel_sens
  w_x = (gyro_x/(2.0**15.0))*gyro_sens
  w_y = (gyro_y/(2.0**15.0))*gyro_sens
  w_z = (gyro_z/(2.0**15.0))*gyro_sens
  return a_x,a_y,a_z,w_x,w_y,w_z

def AK8963_start():
  bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,0x00)
  time.sleep(0.1)
  bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,0x0F)
  time.sleep(0.1)
  coeff_data = bus.read_i2c_block_data(AK8963_ADDR,AK8963_ASAX,3)
  AK8963_coeffx = (0.5*(coeff_data[0]-128)) / 256.0 + 1.0
  AK8963_coeffy = (0.5*(coeff_data[1]-128)) / 256.0 + 1.0
  AK8963_coeffz = (0.5*(coeff_data[2]-128)) / 256.0 + 1.0
  time.sleep(0.1)
  bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,0x00)
  time.sleep(0.1)
  AK8963_bit_res = 0b0001     # 0b0001 = 16-bit
  AK8963_samp_rate = 0b0110   # 0b0010 = 8 Hz, 0b0110 = 100 Hz
  AK8963_mode = (AK8963_bit_res <<4) + AK8963_samp_rate # 位转换
  bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,AK8963_mode)
  time.sleep(0.1)
  return [AK8963_coeffx,AK8963_coeffy,AK8963_coeffz] 

def AK8963_reader(register):
  # 读取磁力计值
  low = bus.read_byte_data(AK8963_ADDR, register-1)
  high = bus.read_byte_data(AK8963_ADDR, register)
  # 将高和低点结合起
  value = ((high << 8) | low)
  # 转换为 + - 值
  if(value > 32768):
    value -= 65536
  return value

def AK8963_conv():
  # 原始磁力计位
  while 1:
    mag_x = AK8963_reader(HXH)
    mag_y = AK8963_reader(HYH)
    mag_z = AK8963_reader(HZH)
    if (bus.read_byte_data(AK8963_ADDR,AK8963_ST2)) & 0x08!=0x08:
      break
  m_x = (mag_x/(2.0**15.0))*mag_sens
  m_y = (mag_y/(2.0**15.0))*mag_sens
  m_z = (mag_z/(2.0**15.0))*mag_sens
  return m_x,m_y,m_z
     
# MPU6050 寄存器
MPU6050_ADDR = 0x68
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
ACCEL_CONFIG = 0x1C
INT_PIN_CFG  = 0x37
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
TEMP_OUT_H   = 0x41
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
# AK8963 寄存器
AK8963_ADDR  = 0x0C
AK8963_ST1   = 0x02
HXH          = 0x04
HYH          = 0x06
HZH          = 0x08
AK8963_ST1   = 0x02
AK8963_ST2   = 0x09
AK8963_CNTL  = 0x0A
AK8963_ASAX  = 0x10

mag_sens = 4800.0    # 磁力计灵敏度：4800 UT
# 启动 I2C 驱动程序
bus = smbus.SMBus(6) # 使用I2C总线开始通信，应将其更改为实际连接端口ID
time.sleep(0.1)
gyro_sens,accel_sens = MPU6050_start()  # 实例化 陀螺仪/加速计
time.sleep(0.1)
AK8963_coeffs = AK8963_start()          # 实例化磁力计
time.sleep(0.1)
```


## 陀螺仪校准图

```py
def get_gyro():
  _, _, _, wx, wy, wz = mpu6050_conv()        # 阅读并转换陀螺数据
  return wx, wy, wz

def gyro_cal():
  print("-" * 50)
  print("陀螺仪校准 - 保持IMU稳定")
  [get_gyro() for ii in range(0, cal_size)]   # 校准前清除缓冲
  mpu_array = []
  gyro_offsets = [0.0, 0.0, 0.0]
  while True:
    try:
      wx, wy, wz = get_gyro()             # 获取陀螺仪值
    except:
      continue
    mpu_array.append([wx, wy, wz])
    if np.shape(mpu_array)[0] == cal_size:
      for qq in range(0, 3):
        gyro_offsets[qq] = np.mean(np.array(mpu_array)[:, qq])  # 平均的
      break
  print("陀螺仪校准完成")
  return gyro_offsets


# 陀螺仪抵消计算
cal_size = 500  # points to use for calibration
gyro_offsets = gyro_cal()  # 计算陀螺仪偏移
# 记录新数据
data = np.array([get_gyro() for ii in range(0, cal_size)])  # 新值

# 用偏移和无偏移打印图形
plt.style.use("ggplot")
fig, axs = plt.subplots(2, 1, figsize=(12, 9))
for ii in range(0, 3):
  axs[0].plot(data[:, ii], label="${}$, Uncalibrated".format(gyro_labels[ii]))
  axs[1].plot(
    data[:, ii] - gyro_offsets[ii],
    label="${}$, Calibrated".format(gyro_labels[ii]),
  )
axs[0].legend(fontsize=14)
axs[1].legend(fontsize=14)
axs[0].set_ylabel("$w_{x,y,z}$ [$^{circ}/s$]", fontsize=18)
axs[1].set_ylabel("$w_{x,y,z}$ [$^{circ}/s$]", fontsize=18)
axs[1].set_xlabel("Sample", fontsize=18)
axs[0].set_ylim([-2, 2])
axs[1].set_ylim([-2, 2])
axs[0].set_title("Gyroscope Calibration Offset Correction", fontsize=22)
fig.savefig(
  "gyro_calibration_output.png",
  dpi=300,
  bbox_inches="tight",
  facecolor="#FCFCFC",
)
fig.show()
```
