---
category: 編程
tags: [JavaScript]
---

# JavaScript

[JavaScript](https://developer.mozilla.org/zh-TW/docs/Glossary/JavaScript) 是動態程式語言，應用於 [HTML](https://developer.mozilla.org/zh-TW/docs/Glossary/HTML) 文件，可以為網頁提供動態的互動功能。

變數（[Variables](https://developer.mozilla.org/en-US/docs/Glossary/Variable)）用來儲存數值。要宣告一個變數，
* 全域變數用 `var`；
* 區域變數用 `let`；
* 常數則用 `const`。
並在後面輸入想要用來呼的名字如下：
```javascript
var xVariable;
let iVariable;
const jVariable;
```
**備註**：JavaScript 是會區分大小寫字母的，所以`myVariable` 跟 `myvariable` 是不相同！

請記得這些變數有著不同的[資料型態](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Data_structures)：

|變數|說明|
|---|---|
|[String](https://developer.mozilla.org/en-US/docs/Glossary/String)|字串，一段文字。如果要將字串指定給一個變數，需要用引號將字串框起來。|
|[Number](https://developer.mozilla.org/zh-TW/docs/Glossary/Number)|數值，一個數字。|
|[Boolean](https://developer.mozilla.org/zh-TW/docs/Glossary/Boolean)|布林值，一個 True（真）/False（假）數值。`true`/`false`  是 JavaScript 內的特殊關鍵字。|
|[Array](https://developer.mozilla.org/zh-TW/docs/Glossary/array)|陣列，一個可以儲存多個數值在單一結構。可以用這個方式來呼叫陣列的每一個成員。|
|[Object](https://developer.mozilla.org/zh-TW/docs/Glossary/Object)|物件。JavaScript 內的所有東西都可以視為一個物件，而且可以被存放在變數裡。|

## 流程控制（flow control）

在 JavaScript 中如許多程式語言一樣有
* `if...else`
* `switch`
* `for`
* `while`
* `do...while`

 條件判斷以及在處理陣列上很常使用的迴圈。

**備註**：JavaScript 中的 false 值：`undefined`、`null`、`NaN`、`0`、`""`（空字串）和  `false`，以上幾種情況在邏輯判斷時會轉換成 false。

1.  if...else
    
    ```javascript
    // 可以投票
    if(age > 18) {
       console.log('可以投票！');
    }
    ```
    
2.  switch：當條件很多時可以善用 switch 判斷，記得要在每個 case 後寫 break，不然會全部都執行。
    
    ```javascript
    const country = 'Taiwan';
    switch(grade) {
      case 'Taiwan':
          console.log('hello' + country);
          break;
      case 'Japan':
          console.log('hello' + country);
          break;
      default:
          console.log('hello' + country);  
    }
    ```
    
3.  for：當你知道程式需要重複執行幾次時可以使用 for 迴圈。
    
    ```javascript
    const arr = ['Mark', 'Zuck', 'Jack'];
    for(let i = 0; i < arr.length; arrr++) {
         console.log(arr[i]);
    }
    ```
    
4.  while：當你程式不知道需要重複執行幾次時可以使用 while 迴圈。
    
    ```javascript
    // 從 1 累加到 10
    const num = 1;
    while(num <= 10) {
       let sum += num; // sum = sum + num
       num += 1;
    }
    ```
    
5.  do...while：當迴圈次數不明確時，可以使用 while，而 do while 會至少執行一次。
    
    ```javascript
    let x = 0;
    while(x < 10) {
       console.log(x);
       x++;
    }
    
    let y = 0;
    do {
       console.log(y);
       y++; 
    } while(i < 10);
    ```
    

## 函式/函數（function）
函數是一段程式區塊重複使用的程式撰寫方法，在 JavaScript 中可以將函數當參數或變數傳遞，讓 JavaScript 在函數式程式設計上更容易發揮。  
函數也可傳入參數。及可用 return 回傳數值，陣列或物件。

```javascript
function sum(a, b) {
   return a + b;
}
sum(12, 20);
```

在 ES6中，簡化了函數，而出現了箭頭函數（arrow function）如下：

```javascript
const sum = (a, b) => {
    return a + b;
};
sum(1, 2);
```

## 物件（object）

物件是儲存資料的結構，具有屬性及方法。有三種建立方式如下：

1.  使用  `new Object`
    
    ```javascript
    var obj = new Object();
    ```
    
2.  使用  `{}`
    
    ```javascript
    var obj = {
       name: 'Mark',
       age: 23
    }
    ```
    
3.  使用建構函數
    
    雖然 JavaScript 並非是類別為基編程的物件導向程式語言，而是基於原型編程的物件導向程式語言。
    ```javascript
    // 實務上建構函數命名採單字首字大寫。
    function Dog(name, age) {
    // 屬性值
       this.name = name;
       this.age = age;
    // 每個實例都會有一份方法副本
       this.wow = function() {
          console.log('wow!wow');
       }
    }
    // 多個實例共用，可以減少記憶體等資源運用
    Dog.prototype.cry = 
       function() {
         console.log('QQQ');
       }
    const dog = new Dog('lucky', 2);
    // wow!wow!
    dog.wow();
    ```
    
## DOM & BOM

DOM 提供 HTML 網頁一種存取的方式，可以將 HTML 元素轉換成一棵節點樹，每一個標籤和文字內容是為一個節點，讓我們可以走訪節點 (Nodes) 來存取 HTML 元素。

```html
<!doctype html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>My title</title>
</head>
<body>
   <h1>My header</h1>
   <a href="">Sample link</a>
</body>
</html>
```
## 操作 DOM 元素的方法如下:
-   用ID名稱選取  
`document.getElementById(elementId)`
-   用元素名稱選取  
 `document.getElementsByTagName(tagName)`  
-   用名稱選取  
 `document.getElementsByName(name)`
-   用Class 名稱選取  
 `document.getElementsByClassName(classname)`
    
有很多元素回傳的是  `NodeList`  物件集合。可用 item() 存取，或用迭代forEach操作。

Document 物件有提供使用「CSS」選擇器來選取元素，效能較好
-   `document.querySelectorAll()`  方法  
    Document 物件的  `querySelectorAll()`  方法可以取得 HTML 的節點陣列或清單，為一個  `NodeList`  物件。
    
-   `document.querySelector()`  方法  
    只會回傳一個符合的元素，沒有就回傳 null。

### 範例：   
  ```javascript
<div class="obj"></div>
<div class="obj"></div>
<div id="baseID"></div>
<script type="text/javascript">                 document.querySelector('#baseID').innerHTML = '<h1>單個操作！</h1>';
  document.querySelectorAll('.obj').forEach((value, index) => {
     value.innerHTML = '<h1>迭代forEach操作！</h1>';
    });
</script>
```
## 事件處理（event handler）
事件處理就是當一個事件發生時如網頁載入、按下右鍵等等，程式會相對應做出怎樣的處理。

### 事件處理機制

```
事件處理 = 事件種類 + 事件處理方法
```
-   事件種類（Event Type）為一個字串，說明發生了什麼事件，例如：click (點擊)、mousemove (滑鼠滑過)。
    
-   事件處理（Event Handlers）為處理事件的函數名稱，當事件發生時要呼叫哪個函數進行處理。
``` javascript
// 當發生 click 事件，會發出 alert 
btn.addEventListener('click', function() {
   alert('被點擊!');
});
```

範例：

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport"         content="width=device-width">
  <title>JS Bin</title>
</head>
<body>
  <button id="btn">點我點我</button>
  <script type="text/javascript">
 const btn = document.querySelector('#btn');

   btn.addEventListener('click', function() {
   alert('被點了!');
 });   
  </script>
</body>
</html>
```

## JSON（JavaScript Object Notation）
JSON 是個以純文字為儲存和傳送簡單結構資料，你可以透過特定的格式去儲存任何資料如字串,數字,陣列,物件等，也可以透過物件或陣列來傳送較複雜的資料。一旦建立了您的 JSON 資料，就可以非常簡單的跟其他程式溝通或交換資料。

**備註** 以下規則用來建立 JSON 字串:

1.  JSON 字串可以包含陣列 Array 資料或者是物件 Object 資料；
2.  陣列可以用  **[ ]**  來寫入資料；
3.  物件可以用  **{ }**  來寫入資料；
4.  name / value 是成對的，中間透過 (**:**) 來區隔。

**備註** 物件或陣列的數值限制如下:

1.  數字 (整數或浮點數)
2.  字串 (請用 "" 括號)
3.  布林函數 (boolean) (true 或 false)
4.  陣列 (請用 [ ] )
5.  物件 (請用 { } )
6.  NULL

## JavaScript 處理 JSON 資料
* `JSON.stringify` 用來轉換JavaScript變數至JSON文本。
* `JSON.parse` 用來轉換JSON文本至JavaScript變數。

