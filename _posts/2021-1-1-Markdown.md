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

\```

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

# 創建內聯鏈接

## 標題ID

為了使用CSS樣式表，所以添加ID到相關標籤。

```
### My Great Heading {#custom-id}
```

### My Great Heading {#custom-id}

## 鏈接標題
將顯示的文字寫在方括號[]內，然後將互聯網鏈接寫在括號（）內。

```
[GitHub Pages](https://hkdickyko.github.io)
```
[GitHub Pages](https://hkdickyko.github.io)


## 鏈接標籤
```

I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

[Google]: http://google.com/      "Google"
[Yahoo]: http://search.yahoo.com/ "Yahoo Search"
[MSN]: http://search.msn.com/     "MSN Search"
```
I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

[Google]:   http://google.com/          "Google"
[Yahoo]:    http://search.yahoo.com/    "Yahoo Search"
[MSN]:      http://search.msn.com/      "MSN Search"

# 內聯圖片
```
![Alt text](../assets/img/me.png)
```
![Alt text]({{ '/assets/img/me.png' | relative_url }})

# 創建表格

| 符號 | 說明 |
|:---:|:---:|
|-: |設置內容和標題欄居右對齊|
|:- |設置內容和標題欄居左對齊|
|:-:|設置內容和標題欄居中對齊|

```
| 名稱| 符號 | 符號 |
|---|:---:|---:|
|left|center|right|
```

| 名稱| 符號 | 符號 |
|---|:---:|---:|
|left|center|right|


# 使用表情符號
```
pushpin :pushpin:
pencil  :pencil:
```


| 名稱| 符號 | 名稱| 符號 |
|:---:|:---:|:---:|:---:|
|grimacing|:grimacing:|sleeping|:sleeping:|
|sweat_smile|:sweat_smile:|sweat|:sweat:|
|cold_sweat|:cold_sweat:|fearful|:fearful:|
|sob|:sob:|cry|:cry:|
|joy|:joy:|triumph|:triumph:|
|scream|:scream:|angry|:angry:|
|yum|:yum:|mask|:mask:|
|pushpin|:pushpin:|pencil|:pencil:|
|thumbsup|:thumbsup:|thumbsdown|:thumbsdown:|
|point_up|:point_up:|point_down|:point_down:|
|point_left|:point_left:|point_right|:point_right:|
|pray|:pray:|ok_hand|:ok_hand:|
|muscle|:muscle:|v|:v:|
|computer|:computer:|iphone|:iphone:|
|lock|:lock:|unlock|:unlock:|
|bulb|:bulb:|moneybag|:moneybag:|
|sound|:sound:|mute|:mute:|
|calendar|:calendar:|dart|:dart:|
|signal_strength|:signal_strength:|cinema|:cinema:|
|u6e80|:u6e80:|u7a7a|:u7a7a:|
|u7981|:u7981:|secret|:secret:|
|no_entry_sign|:no_entry_sign:|warning|:warning:|
|heavy_check_mark|:heavy_check_mark:|x|:x:|
|link|:link:|o|:o:|
|exclamation|:exclamation:|question|:question:|
|100|:100:|beers|:beers:|
|trophy|:trophy:|confetti_ball|:confetti_ball:|
|key|:key:|hourglass|:hourglass:|
|star|:star:|sparkles|:sparkles:|
|hotsprings|:hotsprings:|cool|:cool:|
|shower|:shower:|toilet|:toilet:|
|ok|:ok:|free|:free:|
|id|:id:|sos|:sos:|
|one|:one:|two|:two:|
|three|:three:|four|:four:|
|five|:five:|six|:six:|
|seven|:seven:|eight|:eight:|
|nine|:nine:|keycap_ten|:keycap_ten:|
|zero|:zero:|hash|:hash:|


# 創建新段落

您可以通過在文本行之間留空行來創建新段落。

# 創建ID
 

# 忽略格式

您可以在字符之前使用 `\` 來忽略格式。

```
Let's rename \*our-new-project\* to \*our-old-project\*.
```
Let's rename \*our-new-project\* to \*our-old-project\*.

# 創建腳註

```
Here's a simple footnote,[^1] and 

here's a longer one.[^bignote]

[^1]: footnote 1.

[^bignote]: footnote 2.
```

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.
