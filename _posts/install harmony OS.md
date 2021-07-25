
## Check Linux update

- sudo apt update


## Install Python in your linux

- sudo apt install python*3.9*
- sudo apt-get install python3-pip
- python3 --version

## Install Node.js

- sudo apt install curl
- curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
- source ~/.bashrc
- nvm --version *(List current version)*
- nvm ls-remote *(List all available version)*
- nvm install 10.15.2 *(install version 10.15.2 into your linux system)*
  
## Remove Node.js (*if necessary*)

- sudo apt-get remove nodejsinstall harmony OS.mk

## Install OpenJDK

 - sudo apt-get install openjdk-8-jre
 - java -version

## Install DevEco Device Tool

- Download the file from https://device.harmonyos.com/cn/ide#download_release
- Extract it and chmod 777
- run the extract file in command prompt (*./deveco-device-tool-2.1.0279451.b672a187.run*)


## Installation hpm (HarmonyOS Package Manager)
 - npm i -g core-js@\^3
 - npm cache clean -f
 - npm i

## LLVM (Low Level Virtual Machine)

![](../git/hkdickyko.github.io/assets/img/harmonyOS/LLVM.png)

## create hpm 

- mkdir neptune (*create a project directory name: neptune*)
- cd neptune
- hpm init -t dist (*init the environment*)
- hpm i @hihope/neptune_iot
- hpm dist (*complier the source*)
