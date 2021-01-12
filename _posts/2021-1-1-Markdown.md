---
category: 編程 
tags: [Markdown]
---

# Markdown

Markdown是一種方便記憶、書寫的純文本標記語言，用戶可以使用這些標記符號以最小的輸入代價生成極富表現力的文檔：譬如您正在閱讀的這份文檔。它使用簡單的符號標記不同的標題，分割不同的段落，

# 字體樣式

```
**粗體** 或 __粗體__
```
**粗體** 或 __粗體__

```
*斜體* 或 _斜體_
```
*斜體* 或 _斜體_
```
***粗斜體***
```
***粗斜體***

```
`突顯文字`
```
`突顯文字`

```
~~刪除線~~
```
~~刪除線~~

# 標題樣式
```
 # Header 1
```
# Header 1

```
## Header 2
```
## Header 2

```
### Header 3
```
### Header 3

# 引用文字
```
> Quoting Text
>> Quoting Text
>>> Quoting Text
```
> Quoting Text
>> Quoting Text
>>> Quoting Text

# 引用代碼
\```<br>
git Status<br>
git add<br>
git commit<br>
\```
```
git Status
git add
git commit
```

# 清單
```
 - Item 1
    - item 1.1
        - item 1.1.1
 - Item 2
 - Item 3
```
 - Item 1
    - item 1.1
        - item 1.1.1
 - Item 2
 - Item 3
  
```
 1. Item 1
    - item 1.1
        - item 1.1.1
 2. Item 2
 3. Item 3
```

 1. Item 1
    - item 1.1
        - item 1.1.1
 2. Item 2
 3. Item 3
   
# 複選框
```
- [ ] 未選複選框
- [x] 選中複選框
```
- [ ] 未選複選框
- [x] 選中複選框

# 鏈接
將顯示的文字寫在方括號[]內，然後將互聯網鏈接寫在括號（）內。

```
[GitHub Pages](https://hkdickyko.github.io)
```
[GitHub Pages](https://hkdickyko.github.io)

# 使用表情符號
```
pushpin :pushpin:
memo :pencil:

```
pushpin :pushpin:

memo :pencil:

```gantt
    title 项目开发流程
    section 项目确定
        需求分析       :a1, 2016-06-22, 3d
        可行性报告     :after a1, 5d
        概念验证       : 5d
    section 项目实施
        概要设计      :2016-07-05  , 5d
        详细设计      :2016-07-08, 10d
        编码          :2016-07-15, 10d
        测试          :2016-07-22, 5d
    section 发布验收
        发布: 2d
        验收: 3d
```