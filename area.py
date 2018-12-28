 # coding: utf8
import json
import requests

areas = open('areas.txt', 'r')
area = areas.read()
area = json.loads(area)


def getLocalCode():
    return getAreaCode(getLocalName())


def getLocalName():
    url = 'http://2018.ip138.com/ic.asp'
    try:
        html = requests.request('get', url)

    except ConnectionError as e:
        try:
            url = 'http://2019.ip138.com/ic.asp'
            html = requests.request('get', url)
        except ConnectionError as e:
            return e

    html.encoding = 'gb2312'
    response = html.text
    s_index = response.index('省')
    sh_index = response.index('市')
    area = response[s_index+1:sh_index]

    return area

def getAreaCode(a):
    try:
        return area[a]
    except:
        return 0
