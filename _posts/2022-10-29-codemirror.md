---
category: [Android]
tags: [編程]
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

Code Mirror 提供了很多種主題，在 codemirror-5.12/theme/seti.css 可以看到所有主題，如準備使用 seti 這個主題先需將其引入。

其他功能的實現方法與之類似，稍微註意的是需要引入的文件不同，將實現各個功能所需的文件均寫在瞭如下代碼中：

```html
<!-- Code Mirror需要基本代碼 -->
<link rel="stylesheet" href="codemirror-5.12/lib/codemirror.css">
<script src="codemirror-5.12/lib/codemirror.js"></script>

<!-- Java 代碼高亮必須引入 -->
<script src="codemirror-5.12/clike.js"></script>

<!-- 引入 css 文件，用以支持主題 -->
<link rel="stylesheet" href="codemirror-5.12/theme/eclipse.css">
<link rel="stylesheet" href="codemirror-5.12/theme/seti.css">
<link rel="stylesheet" href="codemirror-5.12/theme/dracula.css">

<!-- 支持代碼摺疊 -->
<link rel="stylesheet" href="codemirror-5.12/addon/fold/foldgutter.css"/>
<script src="codemirror-5.12/addon/fold/foldcode.js"></script>
<script src="codemirror-5.12/addon/fold/foldgutter.js"></script>
<script src="codemirror-5.12/addon/fold/brace-fold.js"></script>
<script src="codemirror-5.12/addon/fold/comment-fold.js"></script>

<!-- 全屏模式 -->
<link rel="stylesheet" href="codemirror-5.12/addon/display/fullscreen.css">
<script src="codemirror-5.12/addon/display/fullscreen.js"></script>

<!-- 括弧匹配 -->
<script src="codemirror-5.12/addon/edit/matchbrackets.js"></script>

<!-- 自動補全 -->
<link rel="stylesheet" href="codemirror-5.12/addon/hint/show-hint.css">
<script src="codemirror-5.12/addon/hint/show-hint.js"></script>
<script src="codemirror-5.12/addon/hint/anyword-hint.js"></script>

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
  <link rel="stylesheet" href="codemirror-5.12/lib/codemirror.css">
  <script src="codemirror-5.12/lib/codemirror.js"></script>
  <script src="codemirror-5.12/clike.js"></script>
  <link rel="stylesheet" href="codemirror-5.12/theme/seti.css">

  <script src="/js/codemirror/mode/xml/xml.js"></script>
  <script src="/js/codemirror/mode/javascript/javascript.js"></script>
  <script src="/js/codemirror/mode/css/css.js"></script>
  <script src="/js/codemirror/mode/htmlmixed/htmlmixed.js"></script>

  <link rel="stylesheet" href="codemirror-5.12/addon/fold/foldgutter.css"/>
  <script src="codemirror-5.12/addon/fold/foldcode.js"></script>
  <script src="codemirror-5.12/addon/fold/foldgutter.js"></script>

  <script src="codemirror-5.12/addon/fold/brace-fold.js"></script>
  <script src="codemirror-5.12/addon/fold/comment-fold.js"></script>

  <link rel="stylesheet" href="codemirror-5.12/addon/display/fullscreen.css">
  <script src="codemirror-5.12/addon/display/fullscreen.js"></script>
  <script src="codemirror-5.12/addon/edit/matchbrackets.js"></script>

  <link rel="stylesheet" href="codemirror-5.12/addon/hint/show-hint.css">
  <script src="codemirror-5.12/addon/hint/show-hint.js"></script>
  <script src="codemirror-5.12/addon/hint/anyword-hint.js"></script>
<head>
<title>Code Mirror Test</title>
</head>
<body>
<textarea id="code"></textarea>
</body>
<script type="text/javascript">
  var editor=CodeMirror.fromTextArea(document.getElementById("code"),{
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
```