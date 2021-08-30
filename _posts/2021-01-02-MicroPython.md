---
category: 編程 
tags: [IoT]
---

# MircoPython

MicroPython是2013年在Kickstarter上募資開始建立的小型硬體編程，因為資源有限，而將Python濃縮成一款小型包，載入硬體微控制器的一項開源專案。

MicroPython怎麼寫？跟Python一模一樣。MicroPython除了留有Python的許多迷你化的標準函式庫，也有例如 machine、network等硬體相關的專屬函式庫用於控制硬體相關功能。

詳細可參考[官方文件](https://docs.python.org/zh-tw)。

源代碼下載地址 : [MicroPython](https://micropython.org/download/)

MicroPython的出現讓許多畏懼低階語言的開發者有機會以高階語言玩玩硬體端，也能加快原本物聯網開發者的開發速度。

但目前MicroPython包含的函式庫還十分有限，所以s太複雜的專案難以完成。

## 主要由以下構成：

  - py/-- 核心python實現，包括編譯器、運行時和核心庫。

  - mpy cross/--用於將腳本轉換為預編譯字節碼的Micropyhon交叉編譯器。

  - extmod/--在C中實現的附加（非核心）模塊。

  - tools/--各種工具

  - docs/--sphinx格式的用戶文檔。呈現的HTML文檔可在http://docs.tpyboard.com上找到。

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

  - ports/minimal/--最小的Micropython端口。

  - tests/--測試框架和測試腳本。

  - example/--幾個Python腳本示例。

MicroPython包含了諸如交互式提示，任意精度整數，關閉，列表解析，生成器，異常處理等高級功能。適合運行在只有256k的代碼空間和16k的RAM的芯片上。 

MicroPython旨在盡可能與普通Python兼容，讓您輕鬆將代碼從桌面傳輸到微控制器或嵌入式。

# Micropython標準庫

- Builtin -- 內建函數和異常
- array -- 數值數組
- gc -- 回收內存碎片
- math -- 數學運算函數
- sys -- 系統特定功能
- ubinascii -- 二進制/ ASCII互轉
- ucollections -- 容器數據類型
- uerrno -- 系統錯誤代碼
- uhashlib -- 散列算法
- uheapq -- 堆隊列算法
- uio -- 輸入/輸出流
- ujson -- JSON 編碼和解碼
- os -- 基本的操作系統
- ure -- 正則表達式
- select -- 高效地等待I/O
- usocket -- socket 模塊
- ussl -- SSL/TLS module
- ustruct -- 打包和解壓縮原始數據類型
- time -- 時間相關函數
- uzlib -- zlib解壓縮

# MicroPython C Stub Generator

> 使用C Stub Generator創建C代碼模板用於「extmod」中提供附加「非核心」模塊。
![]({{ '/assets/img/esp/c_stub.png' | relative_url }})
