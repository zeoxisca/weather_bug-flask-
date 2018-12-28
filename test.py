import flask
from flask import Flask
from flask import request, redirect, url_for
from flask import render_template
import requests
import json
import area
import weather
import random
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
	local = area.getLocalCode()
	weatherinfo = weather.getAimWeather(local)
	weatherinfo['pic'] = getPic(area.getLocalName())
	print(weatherinfo['pic'])
	print(weatherinfo)
	return render_template('index.html', weather=weatherinfo)


@app.route('/weather/<string:cityname>')
def weatherinfo(cityname):

	city_code = area.getAreaCode(cityname)
	if not city_code:
		return render_template('error.html')

	weatherinfo = weather.getAimWeather(city_code)
	weatherinfo['pic'] = getPic(cityname)
	print(weatherinfo)
	return render_template('weather.html', weather=weatherinfo)

@app.route('/search',methods=['GET'])
def search():
	error = None
	if request.args.get("cityname"):
		return redirect(url_for('weatherinfo',cityname=request.args.get("cityname")))

	else:
		return render_template('error.html')



def getPic(area):
	url = 'http://zhannei.baidu.com/cse/search?s=18291016424463923645&q=' + area
	search_page = requests.get(url)
	search_page.encoding = 'utf-8'
	response = search_page.text
	search_soup = BeautifulSoup(response)
	atags = search_soup.find_all('a')
	url = atags[random.randint(0,min(10, len(atags))-1)].get('href')
	if url[:10]!='http://www':
		return getPic(area)
	pic_page = requests.get(url)
	pic_page.encoding = 'utf-8'
	response = pic_page.text
	pic_soup = BeautifulSoup(response)
	imgtags = pic_soup.find_all('img')[2:-4]
	try:
		img_url = imgtags[random.randint(0, len(imgtags)-1)].get('src')
	except:
		img_url = 'static/back.jpg'

	return img_url



