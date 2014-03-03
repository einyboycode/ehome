# -*- coding: utf-8 -*-
#/home/pi/temperature.py
import time
from qqweibo import APIClient
import urllib2
import json
import sys

def get_room_temperature():
    tfile = open("/sys/bus/w1/devices/28-000004f13577/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature

def get_day_weather():
    # get weather html and parse to json
    weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/101300101.html').read()
    weatherJSON = json.JSONDecoder().decode(weatherHtml)
    weatherInfo = weatherJSON['weatherinfo']

    # print weather info
    msg = []
    temp = u'城市：%s' % weatherInfo['city']
    msg.append(temp)
    temp = u'时间：%s' % weatherInfo['date_y']
    msg.append(temp)
    temp = u'24小时天气：'
    msg.append(temp)
    temp = u'温度：%s' % weatherInfo['temp1']
    msg.append(temp)
    temp = u'天气：%s' % weatherInfo['weather1']
    msg.append(temp)
    temp = u'风速：%s' % weatherInfo['wind1']
    msg.append(temp)

    print '紫外线：\t', weatherInfo['index_uv']
    temp = u'紫外线：%s' % weatherInfo['index_uv']
    msg.append(temp)

    print '穿衣指数：\t', weatherInfo['index_d']
    temp = u'穿衣指数：%s' % weatherInfo['index_d']
    msg.append(temp)
    return '\r\n'.join(msg)

def say_hello(type):
    msg = ""
    if type=="normal":
        return msg
    if type=="morning":
        return "新一天开始，各位早上好！"
    if type=="noon":
        return "人是铁，饭是刚，同志们饭点到了！"
    if type=="evening":
        return "同志们要知道南宁是个堵车的地方，不下班更待何时！"
    if type=="night":
        return "别忘记晾，关好门，大家晚安！"
    return msg
        
        



qq = APIClient("801058005", "31cc09205420a004f3575467387145a7", redirect_uri="callback_uri")
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
tsp = time.mktime(time.localtime(time.time()))+100
qq.set_access_token("83d36ac2caa900ab53374903183cba06", "5FD49B7E7A810115834085C835A0B42E", tsp)

msg = ""
if sys.argv[1]=="normal":
    msg = '智能家居机器人提醒:目前您室内温度为 %f ℃ %s' % (get_room_temperature(),get_day_weather())
if sys.argv[1]=="morning":
    msg = '智能家居机器人提醒:%s %s' % (say_hello(sys.argv[1]), get_day_weather())
if sys.argv[1]=="noon":
    msg = '智能家居机器人提醒:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="evening":
    msg = '智能家居机器人提醒:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="night":
    msg = '智能家居机器人提醒:%s' % say_hello(sys.argv[1])
    
qq.upload.t__add_pic(format='json', content=msg, clientip="113.12.163.144", pic=open('/home/pi/img/capture.jpg','rb'));

