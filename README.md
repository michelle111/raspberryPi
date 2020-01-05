# Iot Project 風扇小車
做一個能用手機或網頁操控移動的風扇小車。在四輪小車上面加上風扇，以溫度感測器感測溫度，依據溫度的不同有不同的轉速，節省能源，並可操控移動至期望的位置去吹風，幫忙散熱。

DEMO影片

## 材料清單：

* 電池*12
* 行動電源
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
組裝說明書https://drive.google.com/file/d/0B2qc-F3WpYxWcGtRbk5VdFBiTUU/view  
馬達的銅片朝內組裝


## Step3 安裝馬達
參考網站https://casual-relaxed.blogspot.com/2016/02/raspberry-pi-wifi-car-note_11.html  
使用GPIO.BCM  
接上  
BCM 17  
BCM 18  
BCM 27  
BCM 23  

## Step4 安裝dht22 
參考網站https://www.itread01.com/content/1546191734.html

### 線路接法：  
使用GPIO.BCM  
    VCC --> 3.3V  
    GND --> GND  
    DAT --> BCM 4  
    
安裝套件步驟：  
`sudo apt-get update`  

`sudo apt-get install build-essential python-dev`  

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`  

`cd Adafruit_Python_DHT`  

`sudo python setup.py install`  

## Step5 安裝風扇  
風扇安裝一顆馬達  
一邊接上GND，一邊接上BCM 12  

## Step6 程式碼部分

在新創的環境中新增一個資料夾  
`mkdir webapp`  
進入資料夾中  
`cd webapp`  

在webapp裡新增一個app.py檔案  
`nano app.py`  
app.py檔案內容  
```python
# success
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from flask import Flask, render_template


# 設定GPIO相關設定
# 車子部分
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


# 風扇部分
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

p12 = GPIO.PWM(12, 38)


app = Flask(__name__)

# 連結到樹梅派的時候會打開網頁
@app.route('/')
def index():
    return render_template('index.html')

# 定義三種風速


def fanL():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(20)

    p12.ChangeFrequency(500)


def fanM():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(60)

    p12.ChangeFrequency(500)


def fanH():

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    p12.start(90)

    p12.ChangeFrequency(500)

# 由dht22取得溫度


def getDHTdata():
    DHT22Sensor = Adafruit_DHT.DHT22
    DHTpin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
    return temp

# 對於不同溫度執行不同的風速


def DHTdata():
    i = 1
    while i == 1:
        temp = getDHTdata()
        print("temp=%f" % temp)

        if temp < 20:
            fanL()

        elif temp >= 21 and temp < 23.2:
            fanM()

        elif temp > 23.5:
            fanH()

        time.sleep(1)


# 車子行進方向設定
# 左轉
@app.route('/left', methods=['GET', 'POST'])
def left():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    DHTdata()
    return render_template('index.html')
# 每次下完指令，就會再回到首頁，下同


@app.route("/back", methods=['GET', 'POST'])
# 後退
def back():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    # DHTdata()
    return render_template('index.html')


# 停止
@app.route("/stop", methods=['GET', 'POST'])
def stop():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    # DHTdata()
    return render_template('index.html')


# 前進
@app.route("/forward", methods=['GET', 'POST'])
def forward():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    # DHTdata()

    return render_template('index.html')

# 右轉
@app.route("/right", methods=['GET', 'POST'])
def right():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    # DHTdata()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

```

接著存檔離開，並在剛剛的位置再新增一個templates資料夾  
*注意一定要叫templates，才能執行等等要新增的html檔*  
`mkdir templates`  
進入資料夾裡  
`cd templates`  
新增index.html檔  
`nano index.html`  
內容打上  
```
<!Document html>
	<html>

	<head>
		<!--宣告此網頁為繁體中文-->
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>樹莓派小車控制介面</title>
	</head>

	<body>
		<!--參考http://blog.csdn.net/embbnux/article/details/40001129-->
		<table border="0">
			　<tr>
				　<td></td>
				　<td>
					<form action="/forward" method=post>
						<input type=submit value="前進" style="width:300px;height:300px;font-size:150px;">
					</form>
				</td>
				<td></td>
				　
			</tr>
			　<tr>
				　<td>
					<form action="/left" method=post>
						<input type=submit value="左邊" style="width:300px;height:300px;font-size:150px;">
					</form>
				</td>
				　<td>
					<form action="/stop" method=post>
						<input type=submit value="停止" style="width:300px;height:300px;font-size:150px;">
					</form>
				</td>
				<td>
					<form action="/right" method=post>
						<input type=submit value="右邊" style="width:300px;height:300px;font-size:150px;">
					</form>
				</td>
				　
			</tr>　
			<tr>
				　<td></td>
				　<td>
					<form action="/back" method=post>
						<input type=submit value="後退" style="width:300px;height:300px;font-size:150px;">
					</form>
				</td>
				<td></td>
				　
			</tr>
		</table>
	</body>

	</html>
```

## Step7 執行程式
接著退出templates資料夾  
`cd ..`  
再來就可以執行程式囉！  
`python3 app.py`  
*在終端機跑出的網址中*  
*把0.0.0.0改成自己樹莓派的位址，就可以手機網頁操控車子囉！*  
