# -*- coding: utf-8 -*-
#/home/pi/temperature.py
import time
from qqweibo import APIClient

tfile = open("/sys/bus/w1/devices/28-000004f13577/w1_slave")
text = tfile.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature / 1000


qq = APIClient("801058005", "31cc09205420a004f3575467387145a7", redirect_uri="callback_uri")
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
tsp = time.mktime(time.localtime(time.time()))+100
qq.set_access_token("83d36ac2caa900ab53374903183cba06", "5FD49B7E7A810115834085C835A0B42E", tsp)
msg = '智能家居机器人提醒:目前您室内温度为 %f ℃' % temperature
qq.upload.t__add_pic(format='json', content=msg, clientip="113.12.163.144", pic=open('/home/pi/img/capture.jpg','rb'));

