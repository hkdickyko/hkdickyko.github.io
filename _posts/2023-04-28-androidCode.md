---
category: [ Android]
tags: [Android]
title: Android 代碼技巧
date: 2023-04-28 1:00:00
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
  iframe{
    width: 100%;
    display: block;
    border-style:none;
    overflow:hidden;
  }
</style>

# Android 代碼

## 双击退出程序

```java
boolean doubleBackToExitPressedOnce = false;

@Override
public void onBackPressed(){
  if (doubleBackToExitPressedOnce)	{
    //super.onBackPressed();
    this.exitProgram();
    return;
  }
  this.doubleBackToExitPressedOnce = true;
  Toast.makeText(this, "双击退出程序!", Toast.LENGTH_SHORT).show();
  new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
    @Override
    public void run(){
      doubleBackToExitPressedOnce = false;
    }
  }, 2000);
}
```

## 呼叫 Javascript 程序

fName:程序名稱，cmd:程序代碼，index: 回调序号。

```java
public void javascriptCall(final String fName, final String cmd, final int index)
{
  if (index > 0){
    runOnUiThread(new Runnable() {
      @Override
      public void run(){
        contentView.evaluateJavascript("javascript:" + fName + "(" + cmd + ");",
          new ValueCallback<String>() {
            @Override
            public void onReceiveValue(String s){
              contentView.evaluateJavascript("javascript:callback(" + index + " )", null);
            }
          }
        );
       }
    });
  } else {
    runOnUiThread(new Runnable() {
      @Override
      public void run(){
        contentView.evaluateJavascript("javascript:" + fName + "(" + cmd + ");", null);
      }
    });
  }
}
```

## 加载文件

```java
private byte[] loadData(InputStream stream)
{
  try {
    int size = stream.available();
    byte[] buffer = new byte[size];
    stream.read(buffer);
    stream.close();
    return buffer;
  }
  catch (IOException e) {
    Log.e("ERROR", "loadData", e);
  }
  return null;
}
```