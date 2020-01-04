# Iot Project 風扇小車
做一個能用手機或網頁操控移動的風扇小車。在四輪小車上面加上風扇，以溫度感測器感測溫度，依據溫度的不同有不同的轉速，節省能源，並可操控移動至期望的位置去吹風，幫忙散熱。

## 材料清單：

* 電池電源
* 麵包板
* 杜邦線數根
* 小型風扇
* 單層自走車底盤(含四輪跑車胎+四馬達)
* 直流馬達
* L298N 馬達驅動板
* DHT22溫濕度感測器模組

## Step1 安裝Flask

參考網站 
https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/4
https://medium.com/@ronm333/virtual-environments-on-the-raspberry-pi-ead158a72cd5

找到python 3.5路徑
`which python 3.5`

在隱藏文件.profile中，設置VIRTUALENVWRAPPER_PYTHON的值
`sudo nano ~/.profile`

在檔案最底下打上
`VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7`

運行.profile
`source ~/.profile`

安裝virtualenv
`sudo pip3 install virtualenv`

安裝virtualenvwrapper
`sudo pip3 install virtualenvwrapper`

編輯.profile文件
`nano ~/.profile`

在檔案最底下打上
`export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh`

運行.profile
`source ~/.profile`

命令mkvirtualenv現在可用於創建python虛擬環境
`mkvirtualenv whatever -p /usr/bin/python3.7`

創建進入虛擬環境
`source ~/.profile`
`workon whatever`

安裝flask
`pip3 install flask`


## Step2 安裝四輪小車
參考網站

## Step3 安裝馬達
參考網站

## Step4 安裝dht22 

### 線路接法：
    VCC --> 3.3V
    GND --> GND
    DAT --> BCM 4

## Step5 安裝風扇

## Step6 執行程式
