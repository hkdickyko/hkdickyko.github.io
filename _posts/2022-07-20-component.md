---
category: [編程]
tags: [編程]
title: 前端元件
date: 2022-07-19 06:00:00
---

<style>
    table {
        width: 100%;
    }
</style>

# 前端元件代碼

## 開關按鈕 (只使用 CSS)

```css
* {
    box-shadow: none;
}

body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    width: 100%;
    height: 100vh;
    background-color: #d1dad3;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 17px;
}

.container {
    max-width: 1000px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.switch-holder {
    display: flex;
    padding: 10px 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    box-shadow: -8px -8px 15px rgba(255,255,255,.7),
                10px 10px 10px rgba(0,0,0, .3),
                inset 8px 8px 15px rgba(255,255,255,.7),
                inset 10px 10px 10px rgba(0,0,0, .3);
    justify-content: space-between;
    align-items: center;
}

.switch-label {
    width: 150px;
}

.switch-label i {
    margin-right: 5px;
}

.switch-toggle {
    height: 40px;
}

.switch-toggle input[type="checkbox"] {
    position: absolute;
    opacity: 0;
    z-index: -2;
}

.switch-toggle input[type="checkbox"] + label {
    position: relative;
    display: inline-block;
    width: 100px;
    height: 40px;
    border-radius: 20px;
    margin: 0;
    cursor: pointer;
    box-shadow: inset -8px -8px 15px rgba(255,255,255,.6),
                inset 10px 10px 10px rgba(0,0,0, .25);
}

.switch-toggle input[type="checkbox"] + label::before {
    position: absolute;
    content: '關';
    font-size: 18px;
    text-align: center;
    line-height: 25px;
    top: 8px;
    left: 8px;
    width: 45px;
    height: 25px;
    border-radius: 20px;
    background-color: #d1dad3;
    box-shadow: -3px -3px 5px rgba(255,255,255,.5),
                3px 3px 5px rgba(0,0,0, .25);
    transition: .3s ease-in-out;
}

.switch-toggle input[type="checkbox"]:checked + label::before {
    left: 50%;
    content: '開';
    color: #fff;
    background-color: #00b33c;
    box-shadow: -2px -2px 3px rgba(255,255,255,.2),
                2px 2px 3px #006600;
}

.switch-button{
    background-image: -webkit-linear-gradient(top, #dfdfd0, #fff);
    background-image: linear-gradient(top, #dfdfd0, #fff);
    border-radius: 20px;
    box-shadow: 0px 8px 10px 0px rgba(0, 0, 0, .3), inset 0px 4px 1px 1px white, inset 0px -3px 1px 1px rgba(204,198,197,.5);
    float:left;
    position: relative;
    -webkit-transition: all .1s linear;
    transition: all .1s linear;
    height: 40px;
    width: 100px;
    text-align: center;
    vertical-align: middle;
    display:table;
}

.switch-button:active{
    background-image: linear-gradient(top, #efedec, #f7f4f4);
    box-shadow: 0 1px 1px 0 rgba(0,0,0,.4), inset 0px 1px 1px 1px rgba(104,108,107,.5);
}

.switch-button span {
    display:table-cell;
    vertical-align:middle;
    margin : auto;
    font-family: "LiGothic", "PMingLiU", Arial, serif;
    font-weight: bold;
    font-size: 20px;
}

.switch-button span:hover {
    color: blue;
}

.switch-button span:active {
    color: rgb(0,0,0,0);
    text-shadow: 1px 1px #CC0000;
}
```

## 前端元件的網頁示例

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="./switch.css">

<div class="container">
  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-bluetooth-b"></i><span>藍牙</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="bluetooth">
      <label for="bluetooth"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-wifi"></i><span>無線上網</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="wifi">
      <label for="wifi"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-map-marker"></i></i><span>定位</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="location">
      <label for="location"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-lightbulb-o"></i></i><span>照明控制</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="lighting">
      <label for="lighting"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-refresh"></i></i><span>更新</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="refresh">
      <label for="refresh"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-power-off"></i></i><span>關機</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="poweroff">
      <label for="poweroff"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-thermometer-half"></i><i class="fa fa-tint"></i><span>溫度和濕度</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="thermometer">
      <label for="thermometer"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-camera"></i></i><span>拍照</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="camera">
      <label for="camera"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-trash"></i></i><span>刪除</span>
    </div>
    <div class="switch-toggle">
      <input type="checkbox" id="trash">
      <label for="trash"></label>
    </div>
  </div>

  <div class="switch-holder">
    <div class="switch-label">
      <i class="fa fa-trash"></i></i><span>刪除</span>
    </div>
      <div class="switch-button"><span>刪除</span></div>
  </div>
</div>
```
## 前端元件輸出結果

![Alt text](../assets/img/misc/frontend.gif)
