#! python3
# -*- coding: utf-8 -*-

import json
import urllib.request, urllib.parse
from flask import Flask, request, render_template 

KEY = "6tstj8nvx5kjd1me"
history = []

def query_weather_api(city):
    params = urllib.parse.urlencode({
          'key': KEY,
          'location': city,
          'language': 'en',
          'unit': 'c'
    })
    url = 'https://api.seniverse.com/v3/weather/now.json?{}'.format(params)
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req, context=None).read().decode('UTF-8')
        response_dict = json.loads(response)  #get dict from str
        response_list = response_dict["results"]  #get dict from list
        weather_info = [value for value in response_list[0].values()]
        city_weather = weather_info[1]['text']
        city_temprature = weather_info[1]['temperature']
        output = ("""
        {} : {}, {} degree
        """.format(
            city.upper(), 
            city_weather.lower(),
            city_temprature))
    except:
        output = "Please enter valid city or push Help "
    history.append(city)
    return output
    
def query_help():
    output = """
            Help -> check help doc;
            City -> check weather;
            History -> check query history
            """
    return output

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def query_weather_innerweb():
    output = ' '
    if request.method == 'POST':
        city = request.form['City']
        output = query_weather_api(city)
    elif request.method == 'GET':
        if request.args.get('button') == 'Help':
            output = query_help()
        elif request.args.get('button') == 'History':
            output = history
    return render_template('home.html', message=output)

if __name__ == '__main__':
    app.run()