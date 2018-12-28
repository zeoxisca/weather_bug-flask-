import requests
import json
import area

place = '101210507'

header = {
	'Referer':'http://www.weather.com.cn/weather1d/'+place+'.shtml',
	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

a = requests.get('http://d1.weather.com.cn/sk_2d/'+place+'.html?_=1545667776749',headers=header)
a.encoding = 'utf-8'
print(a.text)