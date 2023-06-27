---
category: [Docker]
tags: [Linux, 系統]
title: Docker 應用
date: 2023-06-26 1:00:00
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

容器是一種標準軟件單元，它打包代碼及其所有依賴項，以便應用程序從一個計算環境快速可靠地運行到另一個計算環境。 

  容器化軟件可用於基於 Linux 和 Windows 的應用程序，無論基礎設施如何，都將始終以相同的方式運行。 容器將軟件與其環境隔離，並確保其統一工作，儘管開發和登台之間存在差異。 


## 容器管理命令

|命令|解釋|
|:---|:---|
|docker create 影像档案 [command]| 創建容器|
|docker run 影像档案 [command] | 執行用器|
|docker rename 容器名 新容器名| 重钟命名容器|
|docker update 容器名|更新容器設置|
|docker start 容器名|開啟容器進程|
|docker stop 容器名|停止容器進程|
|docker kill 容器名|摧毁容器進程|
|docker restart 容器名|重啟容器進程|
|docker pause 容器名|暂停容器進程|
|docker unpause 容器名|恢复容器進程|
|docker rm [-f] 容器名|删除容器|

```
$ docker create debian
$ docker start debian 

# -d 是分离模式，執行後立即分离
$ docker run -d debian true ; echo $?

# -t 为伪终端，-i 为容許輸入。一般 -it 联用
$ docker run -t -i debian bash

# -u 設置用戶
$ docker run -u nobody debian whoami
nobody

# -w 設置當前目錄
$ docker run -w /opt debian pwd

# -e 設置當前環境參數， sh -c 为在 shell 內執行指今
$ docker run -e FOO=foo -e BAR=bar debian sh -c 'echo $FOO $BAR'
foo bar

# -h 設置當前本机名稱
$ docker run -h my-nice-container debian hostname
my-nice-container

# 为容器设置名称。默认生成随机名称。
$ docker run --name blahblah debian true

# 删除容器
$ docker rm blahblah
```

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


```
# 加載硬碟位置
$ docker run -ti -v /tmp:/container/tmp debian

# 加載设备位置
$ docker run -ti --device /dev/sda debian 

# -link 是导出服务的最基本方式
$ docker run -ti --link my-server:srv debian

ping srv

# -p 为加 IP 地址及端口，如沒有加 IP 地址即为 0.0.0.0（所有接口），80 为本机端口，8080 为相對容器端口。
$ docker run -p 127.0.0.1:80:8080 nginx


```



# 映像基本要素

Docker 容器映像是一個輕量級、獨立的可執行軟件包，其中包括運行應用程序所需的一切：代碼、運行時、系統工具、系統庫和設置。 容器鏡像在 docker 運行時即成為容器。


## 映像管理命令

|命令|解釋|
|:---|:---|
|docker images| 列出所有本地圖像 |
|docker history 映像名|顯示圖像歷史列表| 
|docker inspect 映像名|以 json 格式顯示低級信息|
|docker tag 映像名 标记名 |映像加标记| 
|docker commit container 映像名|从容器创建图像|
|docker import url - [tag] | 从 tarball 创建图像|
|docker rmi 映像名|删除图像|


## 映像传输命令

### 使用注册表 API

|命令|解釋|
|:---|:---|
|docker pull repo[:tag] |从注册表中提取映像或存储库 |
|docker push repo[:tag]|从注册表推送映像或存储库|
|docker search 搜索字段| 在官方注册表中搜索映像|
|docker login |登入注册表| 
|docker logout |登出注册表|


### 手动轉移

|命令|解釋|
|:---|:---|
|docker save repo[:tag]|将映像或存储库导出為 tarball |
|docker load|从 tarball 加载映像|
|docker-ssh |用脚本通过 ssh 进程之间传输映像


## 建構工具

|命令|解釋|
|:---|:---|
|FROM image scratch |构建的基础镜像|
|COPY path dst |将上下文中的路径复制到位置目標的容器中|
|ADD src dst |与 COPY 相同，但解压存档并接受 http urls|
|RUN |在容器内运行命令|