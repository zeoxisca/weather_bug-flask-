 # coding: utf8
import requests
import json
import area
import time


def getAimWeather(place):
    millis = int(round(time.time() * 1000))
    header = {
        'Referer':'http://www.weather.com.cn/weather1d/'+str(place)+'.shtml',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }

    a = requests.get('http://d1.weather.com.cn/sk_2d/'+str(place)+'.html?_='+str(millis),headers=header)
    a.encoding = 'utf-8'
    weatherinfo = json.loads(a.text[13:])

    return weatherinfo  



