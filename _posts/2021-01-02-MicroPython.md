---
category: 編程 
tags: [IoT]
title: MicroPython
date: 2021-01-02 22:34:36
---

# MicroPython

MicroPython是2013年在Kickstarter上募資開始建立的小型硬體編程，因為資源有限，而將Python濃縮成一款小型包，載入硬體微控制器的一項開源專案。

MicroPython怎麼寫？跟Python一模一樣。MicroPython除了留有Python的許多迷你化的標準函式庫，也有例如 machine、network等硬體相關的專屬函式庫用於控制硬體相關功能。

詳細可參考 : [官方文件](https://docs.python.org/zh-tw)

源代碼下載地址 : [MicroPython](https://micropython.org/download/)

MicroPython的出現讓許多畏懼低階語言的開發者有機會以高階語言玩玩硬體端，也能加快原本物聯網開發者的開發速度。

但目前MicroPython包含的函式庫還十分有限，所以太複雜的專案難以完成。

## 核心庫

  - py/-- 核心python實現，包括編譯器、運行時和核心庫。

  - mpy cross/--用於將腳本轉換為預編譯字節碼的 *Micropyhon* 交叉編譯器。 該程序用於將 *MicroPython* 腳本預編譯為 .mpy 文件，然後可將其包含到固件或可執行文件中。讓這程序在 *MicroPython* 中使用。

  - extmod/--在 *C* 中實現的附加（非核心）模塊用以提供一些額外的功能。

  - tools/--各種工具

  - docs/--sphinx格式的用戶文檔。呈現的HTML文檔可在[http://docs.tpyboard.com](http://docs.tpyboard.com)上找到。

## 其他組件

  - ports/teensy/--運行在teensy 3.1上的MicroPython版本（初步但功能正常）。

  - ports/pic16bit/--16位pic微控制器的MicroPython版本。

  - ports/cc3200/--在TI的cc3200上運行的Micropython版本。

  - ports/esp8266/--運行在espressf的esp8266 soc上的MicroPython版本。

  - ports/esp32/--運行在espressf的esp32 soc上的MicroPython版本。

  - ports/nrf/--在nrf51和nrf52 mcu上運行的MicroPython版本。

  - ports/unix/--在unix上運行的微星版本。

  - ports/bare-arm/--用於ARM MCU的最小MicroPython版本。主要用於控制代碼大小。

  - ports/stm32/--運行在Pyboard和類似的stm32板上的Micropyhon版本（使用st的cube-hal驅動程序）。

  - ports/minimal/--最小的Micropython內核檔案。用以移植其他開發版。

  - tests/--測試框架和測試腳本。

  - example/--幾個Python腳本示例。

MicroPython包含了諸如交互式提示，任意精度整數，關閉，列表解析，生成器，異常處理等高級功能。適合運行在只有256k的代碼空間和16k的RAM的芯片上。 

MicroPython旨在盡可能與普通Python兼容，讓您輕鬆將代碼從桌面傳輸到微控制器或嵌入式。

## 網上相關程式庫

```
make submodules
```
這將獲取移植所需的所有相關儲存在git內的程式庫子模塊。 使用這命令獲取更新的子模塊的最新版本。

```
make deplibs
```

這將構建所有可用的相關程式庫（無論是否使用它們）。 如果使用其他選項（例如交叉編譯）構建 MicroPython，則應將相同的選項集傳遞給 make deplibs。 要啟用或禁用相關程式庫，需要編輯 mpconfigport.mk 文件，其中包含選項的開關設定。  
例如:
要構建 SSL 模塊（上述 upip 工具需要，因此默認啟用），*MICROPY_PY_USSL* 應設置為 *1*。
但是仍需要使用以上的 make submodules 命令來獲取相關程式庫。

## 標準庫

- Builtin -- 內建函數和異常
- array -- 數值數組 

```python
import array
# unsigned byte
arr = array.array('B') 
# integer
arr = array.array('i', [11, 22, 33, 44, 55])
# float
arr = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
```

- gc -- 回收內存碎片

```python
import gc
gc.mem_free()
gc.mem_alloc()
# 強制對堆中未引用的對象進行垃圾回收
gc.collect() 		
```

- math -- 數學運算函數
- sys -- 系統特定功能
- ubinascii -- 二進制/ ASCII互轉

```python
import ubinascii
# 轉換二進制數據為16進製字符串
ubinascii.hexlify(data[, sep])
# 轉換HEX數據為二進製字符串
ubinascii.unhexlify('313233')
# 轉換 Base64 編碼數據為二進製字符串
ubinascii.a2b_base64(data)			
```

- ucollections -- 容器數據類型
- uerrno -- 系統錯誤代碼
- uhashlib -- 散列算法
- uheapq -- 堆隊列算法
- uio -- 輸入/輸出流
- ujson -- JSON 編碼和解碼

```python
import ujson
obj = {1:2, 3:4, "a":6}
# 將dict類型轉換為字符串
jsObj = ujson.dumps(obj)
# 將字符串轉換為dict類型 			
parsed = ujson.loads(jsObj) 		

```

- os -- 基本的操作系統
- ure -- 正則表達式

```python
import re
# 比較以$開頭的string字符串
re.match(r'\$', string)	
regex = ure.compile("[\r\n]")
regex.split("line1\rline2\nline3\r\n")

['line1', 'line2', 'line3', '', '']

```

- select -- 高效地等待I/O
- usocket -- socket 模塊
- ussl -- SSL/TLS module
- ustruct -- 打包和解壓縮原始數據類型

```python
import ustruct
ustruct.pack('HH', 1, 2)
b'\x01\x00\x02\x00'
ustruct.unpack('HH', b'\x01\x00\x02\x00')
b' \x01,\x01
(1,2)

import struct
id, tag, version, count = struct.unpack("!H4s2I", s)
ss = struct.pack("!H4s2I", id, tag, version, count);

C 中的類似結構
struct Header
{
    unsigned short id;
    char[4] tag;
    unsigned int version;
    unsigned int count;
}

```
- time -- 時間相關函數

```python
import time
time.sleep(1)			# 1秒
time.sleep_ms(1)		# 0.001秒
time.sleep_us(1)		# 0.000001秒

tStart = time.ticks_ms()
tStop = time.ticks_ms()
# 測量微分時間
tElapse = (tStop - tStart) / 1000.0 	

```
- uzlib -- zlib解壓縮

###MicroPython 的數據類型

MicroPython中支持的格式

|代表字符|C 格式|Python 格式|字節數|
|:---:|:---:|:---:|:---:|
|b|signed char|integer|1|
|B|unsigned char|integer|1|
|h|short|integer|2|
|H|unsigned short|integer|2|
|i|int|integer|4|
|I|unsigned int|integer or long|	4|
|l|long|integer|4|
|L|unsigned long|long|4|
|q|long long|long|8|
|Q|unsigned long long|long|8|
|s|char[]|string|1|
|P|void *|long||
|f|float|float|4|
|d|double|float|8|

注意：(<font color="#FF0010">f</font> 和 <font color="#FF0010">d</font> 取決於浮點支持)

struct根據本地機器字節順序轉換.可以用格式中的第一個字符來改變對齊方式.定義如下

|代表字符|字節順序|大小和對齊方式|
|:---:|:---:|:---:|
|@|native|湊夠4個字節|
|=|native|按原字節數|
|<|little-endian|按原字節數|
|>|big-endian|按原字節數|
|!|network (<font color="#FF0010">></font>)|按原字節數|

# 最小的 MicroPython 固件移植

將 *MicroPython* 移植到新開發板的集成最小固件。
首先，我們將最小目錄複製到新目錄 *example_port* 下，然後看下該目錄下的各個文件，功能如下

```shell
cd ports
mkdir example_port
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

## 將新增模塊功能移植到開發板

在文件 modulexx.c 中添加模塊定義。

```c
#include "py/mpconfig.h"
#include "py/obj.h"

STATIC const mp_map_elem_t pyb_module_globals_table[] = {
    { MP_OBJ_NEW_QSTR(MP_QSTR___name__), MP_OBJ_NEW_QSTR(MP_QSTR_pyb) },
};

STATIC MP_DEFINE_CONST_DICT(pyb_module_globals, pyb_module_globals_table);

const mp_obj_module_t pyb_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&pyb_module_globals,
};
```

相應地修改配置文件 <font color="#FF0010">mpconfigport.h</font>

```c
// extra built-in modules to add to the list of known ones
extern const struct _mp_obj_module_t pyb_module;

#define MICROPY_PORT_BUILTIN_MODULES \
    { MP_OBJ_NEW_QSTR(MP_QSTR_pyb), (mp_obj_t)&pyb_module },
```

如果移植正確，那麼應標準的命令行解釋器如下

```
>>> 2
2
>>> print(“Hello!”)
Hello!
>>>
```

# MicroPython C 函數庫生成器

使用 **C** 函數庫生成器，創建 **C** 代碼模板用於「extmod」中提供附加「非核心」模塊。這功能也可修改已有的 **C** 程式庫，使其能成為 **MicroPython** 的程式庫。

![](../assets/img/python/c_stub.png)

**Core** 是函數庫名稱, **Sum** 是函數名稱。 橙色區域是一個新的創建函數, 綠色區域是存儲所有新創建函數的函數庫。

![](../assets/img/python/mpy-sample.png) 

# 將構建映像刻錄到板上 (WeAct Studio STM32F411CEU)

[樣板 WeAct Studio STM32F411CEU6 Core Board](https://github.com/WeActTC)

[下載已編譯 Hex 檔案](https://github.com/WeActTC/WeAct_F411CE-MicroPython/releases)

```shell
sudo apt-get build-dep dfu-util
sudo apt-get install libusb-1.0-0-dev
```

下載固件 : firmware_internal_rom_stm32f411_v1.12-35.hex
將固件從十六進制 (HEX) 轉換為二進制 (BIN)

```shell
sudo apt-get update
sudo apt-get install binutils
objcopy --input-target=ihex --output-target=binary firmware_internal_rom_stm32f411_v1.12-35.hex stm32f411.bin
sudo dfu-util -a 0 -s 0x08000000:leave -t 0 -D stm32f411.bin

```

安裝工具 **Screen** 用於訪問開發板

```shell
sudo apt install screen
sudo apt purge modemmanager
sudo chmod 666 /dev/ttyACM0
screen /dev/ttyACM0

```

由源代碼構建 MicroPython

源代碼下載地址 : [MicroPython](https://micropython.org/resources/micropython-master.zip)

將Git文件下載到所需的目錄位置及安裝相關編譯器


# 移植到 **STM32** 開發板 (WeAct_F411CE-MicroPython)

```shell
sudo apt-get update -y
sudo apt-get install -y gcc-arm-none-eabi
sudo apt-get install -y binutils-arm-none-eabi
sudo apt-get install -y libnewlib-arm-none-eabi
cd ~/MicroPython
git clone https://github.com/micropython/micropython
cd ~/MicroPython/micropython/ports/stm32
make submodules update
make
cd ~/MicroPython/micropython/mpy-cross
make -j4
cd ~/MicroPython/micropython/ports/stm32/boards
git clone https://github.com/WeActTC/WeAct_F411CE-MicroPython.git WeAct_F411CE
cd ~/MicroPython/micropython/ports/stm32
make BOARD=WeAct_F411CE -j
cd ~/MicroPython/micropython/ports/stm32/build-WeAct_F411CE
```

編譯文件是存儲在 *build-WeAct_F411CE* 文件夾內，安裝 *dfu-util* 工具來刻錄 firmware.dfu 檔案

```shell
sudo apt-get install dfu-util
sudo dfu-util --list

```

![](../assets/img/python/dfu-util.png)

數據將刻錄到 *Intrenal Flash* 內部存儲位置如上屏幕截圖

```shell
sudo dfu-util -i 0 -a 0 -d 0483:df11 -D firmware.dfu

```

```c
#define MICROPY_HW_SPIFLASH_ENABLE_CACHE (1)
```


erase firmware 

```shell
dd if=/dev/zero of=zeroes bs=330000 count=1
dfu-util -a 0 -s 0x0801f000 -D zeroes

```