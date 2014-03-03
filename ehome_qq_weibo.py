#! /usr/bin/python
# -*- coding: cp936 -*-
# coding = utf-8

import time
from qqweibo import APIClient
import urllib2
import json
import sys

def get_room_temperature():
    return 0
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
    temp = u'���У�%s' % weatherInfo['city']
    msg.append(temp)
    temp = u'ʱ�䣺%s' % weatherInfo['date_y']
    msg.append(temp)
    temp = u'24Сʱ������'
    msg.append(temp)
    temp = u'�¶ȣ�%s' % weatherInfo['temp1']
    msg.append(temp)
    temp = u'������%s' % weatherInfo['weather1']
    msg.append(temp)
    temp = u'���٣�%s' % weatherInfo['wind1']
    msg.append(temp)

    temp = u'�����ߣ�%s' % weatherInfo['index_uv']
    msg.append(temp)

    temp = '����ָ����%s' % weatherInfo['index_d']
    msg.append(temp)
    return '\r\n'.join(msg)

def say_hello(type):
    msg = ""
    if type=="normal":
        return msg
    if type=="morning":
        return "��һ�쿪ʼ����λ���Ϻã�"
    if type=="noon":
        return "�����������Ǹգ�ͬ־�Ƿ��㵽�ˣ�"
    if type=="evening":
        return "ͬ־��Ҫ֪�������Ǹ��³��ĵط������°������ʱ��"
    if type=="night":
        return "�����������غ��ţ��������"
    return msg
        
        



qq = APIClient("801058005", "31cc09205420a004f3575467387145a7", redirect_uri="callback_uri")
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
tsp = time.mktime(time.localtime(time.time()))+100
qq.set_access_token("83d36ac2caa900ab53374903183cba06", "5FD49B7E7A810115834085C835A0B42E", tsp)

msg = ""
if sys.argv[1]=="normal":
    #msg = u'���ܼҾӻ���������:Ŀǰ�������¶�Ϊ %f �� %s' % (get_room_temperature(),get_day_weather())
    msg = u'���ܼҾӻ���������:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="morning":
    #msg = u'���ܼҾӻ���������:%s %s' % (say_hello(sys.argv[1]),get_room_temperature())
    msg = u'���ܼҾӻ���������:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="noon":
    msg = u'���ܼҾӻ���������:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="evening":
    msg = u'���ܼҾӻ���������:%s' % say_hello(sys.argv[1])
if sys.argv[1]=="night":
    msg = u'���ܼҾӻ���������:%s' % say_hello(sys.argv[1])
    
qq.upload.t__add_pic(format='json', content=msg, clientip="113.12.163.144", pic=open('/home/pi/img/capture.jpg','rb'));

