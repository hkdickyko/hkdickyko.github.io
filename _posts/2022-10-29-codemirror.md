---
category: [網頁]
tags: [編程, JS]
title: CodeMirror
date: 2022-10-29 1:00:00
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
</style>

# Code Mirror

Code Mirror 是由 javascript 寫的一款插件，其功能非常強大。不僅提供了高亮功能，其豐富的方法屬性也封裝了縮進、自動換行、獲取編輯文本、設置編輯文本、回退功能等多種實用效果。用來實現網頁端代碼編輯器非常方便。

Code Mirror 提供了很多種主題，在 lib/codemirror/theme/seti.css 可以看到所有主題，如準備使用 seti 這個主題先需將其引入。

其他功能的實現方法與之類似，稍微註意的是需要引入的文件不同，將實現各個功能所需的文件均寫在瞭如下代碼中：

```html
<!-- Code Mirror需要基本代碼 -->
<link rel="stylesheet" type="text/css" href="lib/codemirror/codemirror.css">
<script type="text/javascript" src="lib/codemirror/codemirror.js"></script>

<!-- Java 代碼高亮必須引入 -->
<script type="text/javascript" src="lib/codemirror/mode/clike/clike.js"></script>

<!-- 引入 css 文件，用以支持主題 -->
<link rel="stylesheet" type="text/css" href="lib/codemirror/theme/eclipse.css">
<link rel="stylesheet" type="text/css" href="lib/codemirror/theme/seti.css">
<link rel="stylesheet" type="text/css" href="lib/codemirror/theme/dracula.css">

<!-- 支持代碼摺疊 -->
<link rel="stylesheet" type="text/css" href="lib/codemirror/addon/fold/foldgutter.css"/>
<script type="text/javascript" src="lib/codemirror/addon/fold/foldcode.js"></script>
<script type="text/javascript" src="lib/codemirror/addon/fold/foldgutter.js"></script>
<script type="text/javascript" src="lib/codemirror/addon/fold/brace-fold.js"></script>
<script type="text/javascript" src="lib/codemirror/addon/fold/comment-fold.js"></script>

<!-- 全屏模式 -->
<link rel="stylesheet" type="text/css" href="lib/codemirror/addon/display/fullscreen.css">
<script type="text/javascript" src="lib/codemirror/addon/display/fullscreen.js"></script>

<!-- 括弧匹配 -->
<script type="text/javascript" src="lib/codemirror/addon/edit/matchbrackets.js"></script>

<!-- 自動補全 -->
<link rel="stylesheet" type="text/css" href="lib/codemirror/addon/hint/show-hint.css">
<script type="text/javascript" src="lib/codemirror/addon/hint/show-hint.js"></script>
<script type="text/javascript" src="lib/codemirror/addon/hint/anyword-hint.js"></script>

</html>
```

其他說明：

在構造 editor 時相關的屬性大多數都可以動態的指定。

## 動態的指定

### 設置顯示行號

可以不在構造editor時指出，只需構造出editor之後，調用

```js
editor.setOption("lineNumbers", true)
```

### 更改主題

```js
editor.setOption("theme","seti")
```

### 獲取屬性的值

```js
editor.getOption("屬性名")
```

以下例中將返回 "seti"

```js
editor.getOption("theme")
```

無法用 js 的 DOM 操作獲取編輯器中的值，但可以用

```js
editor.getValue()
```

**獲得其中的值**

```js
editor.getValue("value")
```

## CodeMirror 的配置說明

## 屬性說明

|函數|描述|
|:---:|:---:|
|value|設置編輯器的初始編輯值|
|mode|指定編輯的模式，text/html，javascript 等|
|theme|設定主題樣式|
|indentUnit|設置縮進值，默認為 2|
|smartIndent|是否使用上下文智能縮進，默認為 true。默認為 4|
|tabSize|tab字符的寬度，默認為 4|
|dragDrop|是否允許拖放，默認為true|
|readOnly|編輯器是否只讀。|
|indentWithTabs|在縮進時，是否需要把 tab 寬度個空格替換成字符，默認為false|
|electricChars|是否在當前行輸入時適當改變其縮進，默認為 true|
|lineWrapping|是否可以滾動，默認為 false|
|lineNumbers|是否顯示編輯器行數，默認為 false|
|firstlineNumber|開始計數的行數，默認為 1|
|lineNumberFormatter|function(line:Integer),通過行號返回該行的字符串|
|fixedGutter|內容是否水平滾動，默認為 true|


## 方法說明


|函數|描述|
|:---:|:---:|
|getEditor()|獲取 CodeMirror 對像|
|getOption(name)|設置選項變量|
|getValue()|獲取編輯器文本|
|setValue(textString)|設置編輯器文本|
|setSize(width,height)|設置編輯框的尺寸|
|toTextArea()|該方法得到的結果是未經過轉義的數據|
|undo()|撤銷一個編輯器|
|redo()|重做一個編輯器|


### 標選行數

|函數|描述|
|:---:|:---:|
|lineCount()|獲取編輯器總行數|
|firstLine()|獲取第一行行數，默認為0，從開始計數|
|lastLine()|獲取最後一行行數|
|getLine(Integer)|獲取第 n 行的文本內容|
|getLineHandle(line)|根據行號獲取行句柄|

### 標選區域

|函數|描述|
|:---:|:---:|
|getSelection()|獲取鼠標選中區域的代碼|
|getRange({line,ch},{line,ch})|獲取指定範圍內的文本內容第一個對像是起始坐標，第二個是結束坐標|
|setSelection({line:num,ch:num1},{line:num2,ch:num3})|設置一個區域被選中|
|replaceRange(str1,{line,ch},{line,ch},str2)|替換 str1 中一部分代碼為 str2|
|somethingSelected()|判斷是否被選擇|
|replaceSelection(str1,str2)|替換所選內容|


## 基本應用例子

### 程式碼加色

```html
<html>
  <link rel="stylesheet" type="text/css" href="lib/codemirror/codemirror.css">
  <script src="lib/codemirror/codemirror.js"></script>
  <script src="lib/codemirror/mode/clike/clike.js"></script>
  <link rel="stylesheet" type="text/css" href="lib/codemirror/theme/seti.css">

  <script src="/js/codemirror/mode/xml/xml.js"></script>
  <script src="/js/codemirror/mode/javascript/javascript.js"></script>
  <script src="/js/codemirror/mode/css/css.js"></script>
  <script src="/js/codemirror/mode/htmlmixed/htmlmixed.js"></script>

  <link rel="stylesheet" type="text/css" href="lib/codemirror/addon/fold/foldgutter.css"/>
  <script src="lib/codemirror/addon/fold/foldcode.js"></script>
  <script src="lib/codemirror/addon/fold/foldgutter.js"></script>

  <script src="lib/codemirror/addon/fold/brace-fold.js"></script>
  <script src="lib/codemirror/addon/fold/comment-fold.js"></script>

  <link rel="stylesheet" type="text/css" href="lib/codemirror/addon/display/fullscreen.css">
  <script src="lib/codemirror/addon/display/fullscreen.js"></script>
  <script src="lib/codemirror/addon/edit/matchbrackets.js"></script>

  <link rel="stylesheet" type="text/css" href="lib/codemirror/addon/hint/show-hint.css">
  <script src="lib/codemirror/addon/hint/show-hint.js"></script>
  <script src="lib/codemirror/addon/hint/anyword-hint.js"></script>
<head>
<title>Code Mirror Test</title>
</head>
<body>
<textarea id="code"></textarea>
</body>
<script type="text/javascript">
  let editor=CodeMirror.fromTextArea(document.getElementById("code"),{
    // Html, javascript css 高亮顯示
    mode:"htmlmixed",
    // 設置主題
    theme:"seti",
    // 顯示行號
    lineNumbers:true,
    // 代碼摺疊
    lineWrapping:true,
      foldGutter: true,
      gutters:["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
    // 全屏模式
    fullScreen:true,
    // 括弧匹配
    matchBrackets:true,
    // 智能提示 ctrl-space喚起智能提示
    extraKeys:{"Ctrl-Space":"autocomplete"}
  });
</script>
</html>
<<<<<<< HEAD
=======
```


## 有用的函數

### 在所選字符串的兩端添加字符

```js
function containSelect(cm, strValue) {
  let cursor = cm.getCursor();
  let selection = cm.getSelection();
  cm.replaceSelection(strValue + selection + strValue);
  if (selection === "") {
    cm.setCursor(cursor.line, cursor.ch + 1);
  }
}
```

### 在每行的所選字符串的開頭添加字符

```js
function frontSelect(cm, strValue) {
  let selection = cm.getSelection();
  if (selection === "") {
    cm.replaceSelection(strValue + " " + selection);
  } else {
    let selectionText = selection.split("\n");
    for (let i = 0, len = selectionText.length; i < len; i++) {
      selectionText[i] =
        selectionText[i] === "" ? "" : strValue + " " + selectionText[i];
    }
    cm.replaceSelection(selectionText.join("\n"));
  }
}
```

### 在所選字符串的開頭和結尾添加不同的字符

```js
function bothSelect(cm, frontStr, endStr) {
  let selection = cm.getSelection();
  cm.replaceSelection(frontStr + selection + endStr);
  if (selection === "") {
    cm.setCursor(cursor.line, cursor.ch + 1);
  }
}
```

### 將字符串插入光標位置

```js
function placeString(cm, strValue) {
  cm.replaceSelection(strValue);
}
```

### 生成日期時間插入光標位置

```js
function getDate(cm, format) {
  format = format || "";
  let addZero = function (d) {
    return d < 10 ? "0" + d : d;
  };
  let date = new Date();
  let year = date.getFullYear();
  let year2 = year.toString().slice(2, 4);
  let month = addZero(date.getMonth() + 1);
  let day = addZero(date.getDate());
  let weekDay = date.getDay();
  let hour = addZero(date.getHours());
  let min = addZero(date.getMinutes());
  let second = addZero(date.getSeconds());
  let ms = addZero(date.getMilliseconds());
  let datefmt = "";

  let ymd = year2 + "-" + month + "-" + day;
  let fymd = year + "-" + month + "-" + day;
  let hms = hour + ":" + min + ":" + second;

  switch (format) {
    case "UNIX Time":
      datefmt = date.getTime();
      break;

    case "UTC":
      datefmt = date.toUTCString();
      break;

    case "yy":
      datefmt = year2;
      break;

    case "year":
    case "yyyy":
      datefmt = year;
      break;

    case "month":
    case "mm":
      datefmt = month;
      break;

    case "cn-week-day":
    case "cn-wd":
      let cnWeekDays = ["日", "一", "二", "三", "四", "五", "六"];
      datefmt = "星期" + cnWeekDays[weekDay];
      break;

    case "week-day":
    case "wd":
      let weekDays = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      datefmt = weekDays[weekDay];
      break;

    case "day":
    case "dd":
      datefmt = day;
      break;

    case "hour":
    case "hh":
      datefmt = hour;
      break;

    case "min":
    case "ii":
      datefmt = min;
      break;

    case "second":
    case "ss":
      datefmt = second;
      break;

    case "ms":
      datefmt = ms;
      break;

    case "yy-mm-dd":
      datefmt = ymd;
      break;

    case "yyyy-mm-dd":
      datefmt = fymd;
      break;

    case "yyyy-mm-dd h:i:s ms":
    case "full + ms":
      datefmt = fymd + " " + hms + " " + ms;
      break;

    case "full":
    case "yyyy-mm-dd h:i:s":
    default:
      datefmt = fymd + " " + hms;
      break;
  }
  cm.replaceSelection(datefmt);
}
```

### 句子中的第一個字母轉大寫

```js
function ucfirst(cm) {
  let selection = cm.getSelection();
  let selections = cm.listSelections();
  cm.replaceSelection(editormd.firstUpperCase(selection));
  cm.setSelections(selections);
}
```

### 文字中的第一個字母轉大寫

```js
function ucwords(cm) {
  let selection = cm.getSelection();
  let selections = cm.listSelections();
  cm.replaceSelection(editormd.wordsFirstUpperCase(selection));
  cm.setSelections(selections);
}
```

### 轉大寫

```js
function uppercase(cm) {
  let selection = cm.getSelection();
  let selections = cm.listSelections();
  cm.replaceSelection(selection.toUpperCase());
  cm.setSelections(selections);
}
```

### 轉小寫

```js
function lowercase() {
  let cursor = cm.getCursor();
  let selection = cm.getSelection();
  let selections = cm.listSelections();
  cm.replaceSelection(selection.toLowerCase());
  cm.setSelections(selections);
}
```

### 清除前後多餘的空格

```js
function trim(str) {
  return !String.prototype.trim
    ? str.replace(/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, "")
    : str.trim();
}
```