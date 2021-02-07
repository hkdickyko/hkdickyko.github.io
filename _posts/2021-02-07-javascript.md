---
category: 編程
tags: [Javascript]
---

# JavaScript

[JavaScript](https://developer.mozilla.org/zh-TW/docs/Glossary/JavaScript) 是一個成熟的動態程式語言，應用於 [HTML](https://developer.mozilla.org/zh-TW/docs/Glossary/HTML) 文件上時，可以為網頁提供動態的互動功能。

變數（[Variables](https://developer.mozilla.org/en-US/docs/Glossary/Variable)）是可以用來儲存數值的容器。要宣告一個變數，
全域變數將使用 `var`，區域變數使用 `let`，若你需要固定不變的常數則是使用 `const`。並在後面輸入您想要用來呼叫她的名字如下：
```
var myVariable;
```
**備註**：JavaScript 是會區分大小寫字母的，所以`myVariable` 跟 `myvariable` 是不相同！

請記得這些變數有著不同的[資料型態](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Data_structures)：

|變數|說明|
|---|---|
|[String](https://developer.mozilla.org/en-US/docs/Glossary/String)|字串，一段文字。如果要將字串指定給一個變數，需要用引號將字串框起來。|
|[Number](https://developer.mozilla.org/zh-TW/docs/Glossary/Number)|數值，一個數字。|
|[Boolean](https://developer.mozilla.org/zh-TW/docs/Glossary/Boolean)|布林值，一個 True（真）/False（假）數值。`true`/`false`  是 JavaScript 內的特殊關鍵字。|
|[Array](https://developer.mozilla.org/zh-TW/docs/Glossary/array)|陣列，一個可以儲存多個數值在單一結構。|可以用這個方式來呼叫陣列的每一個成員。|
|[Object](https://developer.mozilla.org/zh-TW/docs/Glossary/Object)|物件。JavaScript 內的所有東西都可以視為一個物件，而且可以被存放在變數裡。|

# 流程控制（flow control）

在 JavaScript 中如許多程式語言一樣有  `if...else`、`switch`  條件判斷以及在處理陣列上很常使用的迴圈。

另外要注意的是在 JavaScript 中的 false 值：`undefined`、`null`、`NaN`、`0`、`""`（空字串）和  `false`，以上幾種情況在邏輯判斷時會轉換成 false

1.  if...else
    
    ```
    // 可以投票
    if(age > 18) {
    console.log('可以投票！');
    }
    
    ```
    
2.  switch：當條件很多時可以善用 switch 判斷，記得要在每個 case 後寫 break，不然會全部都執行
    
    ```
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
    
3.  for：當你知道程式需要重複執行幾次時可以使用 for 迴圈
    
    ```
    const arr = ['Mark', 'Zuck', 'Jack'];
    for(let i = 0; i < arr.length; arrr++) {
         console.log(arr[i]);
    }
    ```
    
4.  while：當你程式不知道需要重複執行幾次時可以使用 while 迴圈
    
    ```
    // 從 1 累加到 10
    const num = 1;
    while(num <= 10) {
       let sum += num; // sum = sum + num
       num += 1;
    }
    ```
    
5.  do...while：當迴圈次數不明確時，可以使用 while，而 do while 會至少執行一次
    
    ```
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
    

# 函式/函數（function）
函數是一段程式區塊重複使用的程式撰寫方式，在 JavaScript 中可以將函數當參數或變數傳遞，也讓 JavaScript 在函數式程式設計上更容易發揮。  
函數可傳入參數。也可用 return 回傳數值或物件。

```
function sum(a, b) {
   return a + b;
}
sum(12, 20);
```

在 ES6中，簡化了函數的使用出現了箭頭函數（arrow function）如：

```
const sum = (a, b) => {
    return a + b;
};
sum(1, 2);
```

# 物件（object）

物件是儲存資料的結構，具有屬性及方法。有三種建立方式如下：

1.  使用  `new Object`
    
    ```
    var obj = new Object();
    ```
    
2.  使用  `{}`
    
    ```
    var obj = {
       name: 'Mark',
       age: 23
    }
    ```
    
3.  使用建構函數
    
    雖然 JavaScript 並非是類別為基編程的物件導向程式語言，而是基於原型編程的物件導向程式語言。
    ```
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
    

# DOM & BOM


