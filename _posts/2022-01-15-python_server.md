---
category: [編程]
tags: [IoT, 編程]
title: Python 網絡服務器
date: 2022-01-13 12:00:00
---

<style>
    table {
        width: 100%;
    }
</style>

# 在 Linux 下的 Python 網絡服務器

Flask 是一個使用 Python 撰寫的輕量級 Web 應用程式框架。Flask 核心十分簡單，主要是由 Werkzeug WSGI 工具箱和 Jinja2 模板引擎所組成。Flask 給予開發者非常大的彈性。可以選用不同的用的 extension 來增加其功能。以下是 Flask 簡易運行的程式，啟動測試伺服器後，可以在瀏覽器中 http://127.0.0.1:5000/ 印出 *歡迎來到 Flask!*。

```python
# 導入 Flask 工具包
from flask import Flask
# 初始化 Flask 類別成為 instance
app = Flask(__name__)

@app.route("/")
def main():
    return "歡迎來到 Flask!"

@app.route("/file")
def file():
    return "歡迎來到 Flask 文件控制環境!"

# 選擇要正確執行的功能模塊
if __name__ == "__main__":
    app.run()
```
網頁由網絡定位器地址控制，如下所示

http://127.0.0.1:5000/

![Alt flask](../assets/img/misc/flask_base.png)

http://127.0.0.1:5000/<font color='red'>file</font> 主要的不同是地址的結尾轉移到不同的功能模塊

![Alt flask](../assets/img/misc/flask_file.png)