---
category: [Docker]
tags: [Linux, 系統]
title: Docker 應用
date: 2022-08-20 1:00:00
---

<style>
  table {
    width: 100%
    }
  td {
    vertical-align: center;
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
  }
</style>

# 容器基本要素

## 容器管理命令

|命令|解釋|
|:---|:---|
|docker create 影像档案 [ command ]| 創建容器|
|docker run 影像档案 [ command ] | 執行用器|
|docker rename 容器名 新容器名| 重钟命名容器|
|docker update 容器名|更新容器設置| 
|docker start 容器名|開啟容器進程||
|docker stop 容器名|停止容器進程| 
|docker kill 容器名|摧毁容器進程| 
|docker restart 容器名|重啟容器進程|
|docker pause 容器名|暂停容器進程|
|docker unpause 容器名|恢复容器進程| 
|docker rm [-f] 容器名|删除容器|


## 检查容器

|命令|解釋|
|:---|:---|
|docker ps| 列出正在運行的容器|
|docker ps -a| 列出所有容器| 
|docker logs [-f] 容器名| 顯示容器輸出 (stdout+stderr)|
|docker top 容器名 [ps options] |列出容器內運行的進程|
|docker stats [容器名]| 顯示實時使用統計數據|
|docker diff 容器名| 顯示與圖像的差異（修改後的文件）|
|docker port 容器名| 列出端口映射| 
|docker inspect 容器名|顯示低級信息（json 格式）|
|docker attach 容器名 |附加到正在運行的容器 (stdin/stdout/stderr) |
|docker cp 容器目录 本機目录|- 容器目录下所有檔案復製到本機目录| 
|docker cp 本機目录 容器目录| 本機目录下所有檔案復製到容器目录| 
|docker export 容器名| 以 tar 壓縮黨案形式導出容器內容|
|docker exec 容器名 參數 . . .| 在現有容器中運行命令，在對於調試用| 
|docker wait 容器名|等待容器終止並返回退出代碼|
|docker commit 容器名 |影像擋提交一個新的 docker 快照|





**注意**： <font color="#FF1000">[  ]</font>  內为，選擇性資料。不加即代表全部。








