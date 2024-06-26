---
category: [編程]
tags: [編程, IoT, Python]
title: MicroPython 移植
date: 2022-02-12 18:00:00
---

<style>
    table {
        width: 100%;
    }
</style>

# MicroPython 移植細節

[MicroPython 移植互聯網資源](https://docs.micropython.org/en/latest/develop/porting.html)

MicroPython 項目包含多個用於不同微控制器系列和架構的端口。項目存儲庫有一個 ports 目錄，其中包含每個支持的移植的子目錄。

[可看以下鏈接介紹](https://hkdickyko.github.io/編程/MicroPython)

# MicroPython 最小固件移植

將 *MicroPython* 移植到新開發板的集成最小固件。首先，我們將最小目錄複製到新目錄 *port1* 下，然後看下該目錄下的各個文件，功能如下

```shell
mkdir ~/python_ports
cd ~/python_ports
mkdir port1
cd port1
```

  - frozentest.py -- 測試用的源代碼文件
  - frozentest.mpy -- 利用micropython自帶的編譯工具mpy-cross對frozentest.py編譯出的字節碼文件
  - main.c -- c代碼入口
  - uart_core.c -- 串口驅動文件
  - mpconfigport.h -- 主要的配置文件
  - mphalport.h -- hal層的配置文件
  - qstrdefsport.h -- 外部符號的定義
  - stm32f405.ld -- 默認的鏈接腳本
  - Makefile -- 如下介紹
  - README.md -- 說明的md文件

其中，需要修改的文件包括：<font color="#FF0010"> Makefile</font>，<font color="#FF0010">stm32f405.ld</font>，<font color="#FF0010">uart_core.c</font>，<font color="#FF0010">main.c</font>，<font color="#FF0010">mpconfigport.h </font>

另外，还需要增加如下文件：

 - start.S -- 初始化代碼，也就是最終編譯出bin文件的入口，用於初始化棧，sram，nand flash以及復制代碼到sram等，並最終跳轉到main.c文件中的主要函數
 - nand.c / nand.h -- nand flash 驅動文件
 - uart.h -- 串口驅動頭文件
 - libgcc.a -- 從編譯工具鏈獲得，用於提供除法相關的符號定義
 - mylibc.a -- 增加對printf函數以及字符串庫的支持，這裡沒有使用工程自帶的printf函數，原因是自帶的printf函數打印整形數據會出現錯誤

最小的 *MicroPython* 固件移植例子:

```c
#include "py/compile.h"
#include "py/runtime.h"
#include "py/repl.h"
#include "py/gc.h"
#include "lib/utils/pyexec.h"

#include <stdio.h>

static char heap[2048];

int main (int argc, char **argv) {
    gc_init(heap, heap + sizeof(heap));

    mp_init();

    pyexec_friendly_repl();

    mp_deinit();
    return 0;
}

void nlr_jump_fail(void *val) {
    while (1) {
        ;
    }
}

void NORETURN __fatal_error(const char *msg) {
    while (1) {
        ;
    }
}

mp_lexer_t *mp_lexer_new_from_file(const char *filename) {
    mp_raise_OSError(MP_ENOENT);
}

mp_import_stat_t mp_import_stat(const char *path) {
    return MP_IMPORT_STAT_NO_EXIST;
}

mp_obj_t mp_builtin_open(uint n_args, const mp_obj_t *args, mp_map_t *kwargs) {
    return mp_const_none;
}

MP_DEFINE_CONST_FUN_OBJ_KW(mp_builtin_open_obj, 1, mp_builtin_open);

```

## 相關編譯 make 檔案

```
include ../../py/mkenv.mk

CROSS = 0

# Include py core make definitions
include $(TOP)/py/py.mk

LIBS =

SRC_C = \
    main.c \

$(BUILD)/firmware.elf: $(OBJ)
    $(ECHO) "LINK $@"
    $(Q)$(LD) $(LDFLAGS) -o $@ $^ $(LIBS)
    $(Q)$(SIZE) $@

$(BUILD)/firmware.bin: $(BUILD)/firmware.elf
    $(Q)$(OBJCOPY) -O binary $^ $@

$(BUILD)/firmware.hex: $(BUILD)/firmware.elf
    $(Q)$(OBJCOPY) -O ihex -R .eeprom $< $@

include $(TOP)/py/mkrules.mk
```

## 配置 *MicroPython* 文件  

這些配置在名為 mpconfigport.h 和 mphalport.h 檔案內。

<font color="#FF0010">mpconfigport.h</font> 配置文件包含特定於機器的配置，包括是否啟用不同的 *MicroPython* 功能等方面。  
<font color="#FF0010">mphalport.h</font> 配置包括類型定義、根指針、電路板名稱、微控制器名稱等。

## USB 端口配置程序

將內核映像刻錄到控制板，需要修改 WINE USB 端口配置，請在運行 HiBurn 後使用的以下命令，然後再將控制板插入到電腦USB端口 (不能在 Python 虛擬環境中運行)。com33 應根據實際情況更改。

```shell
$ ls -l ~/.PlayOnLinux/wineprefix/c_driver/dosdevices
lrwxrwxrwx 1 xxxx xxxx 12 Feb 13 16:57 com33 -> /dev/ttyUSB0

# 尋找 /dev/ttyUSB 設備如上，在這個例子是 com33 
$ rm -rf ~/.PlayOnLinux/wineprefix/C_driver/dosdevices/com33
$ ln -s /dev/ttyUSB0 ~/.PlayOnLinux/wineprefix/c_driver/dosdevices/com33

```

## ELF 轉換成 HEX / BIN

一些交叉編譯器將創建一個輸出 *ELF* 文件, 假設文件名是 *firmware.elf* 從 ELF 到 HEX 的轉換方法如下。文件名 *output.hex* 將根據需要更改。

```shell
# 安裝轉換工具 *objcopy* 如果之前沒有安裝
$ sudo apt-get install binutils-multiarch 

# 轉換指令 HEX
$ objcopy -O ihex firmware.elf output.hex

# 轉換指令 BIN
$ objcopy -O binary firmware.elf output.bin
```

## 將映像刻錄到 STM32 控制板

```shell
$ objcopy -O binary firmware.elf output.bin
$ sudo apt-get install dfu-util
$ sudo dfu-util -a 0 -s 0x08000000:leave -t 0 -D output.bin

```

## 列表將是設備 tty 的連接順序資料
```shell
$ dmesg | grep tty

[ 4033.421847] cdc_acm 1-1.4:1.1: ttyACM0: USB ACM device
[ 6380.194805] usb 1-1.4: ch341-uart converter now attached to ttyUSB0
[ 6563.406395] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
[ 6567.325537] usb 1-1.4: ch341-uart converter now attached to ttyUSB0


ampy --port /dev/ttyACM0 --baud 115200 ls

```