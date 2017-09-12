#! python3
# -*- coding: utf-8 -*-

import json
from urllib import request, parse
from query_weather_cli import query_help

KEY = "6tstj8nvx5kjd1me"
history = []

def query_weather_api(city):
    params = parse.urlencode({
          'key': KEY,
          'location': city,
          'language': 'en',
          'unit': 'c'
    })
    url = 'https://api.seniverse.com/v3/weather/now.json?{}'.format(params)
    req = request.Request(url)
    try:
        response = request.urlopen(req, context=None).read().decode('UTF-8')
        response_dict = json.loads(response)  #get dict from str
        response_list = response_dict["results"]  #get dict from list
        weather_info = [value for value in response_list[0].values()]
        city_weather = weather_info[1]['text']
        city_temprature = weather_info[1]['temperature']
        update_time = weather_info[2]
        output = ("""
        {} weather is: {}, temperature is: {}, 
        updated on:{}
        """.format(
            city.upper(), 
            city_weather.lower(),
            city_temprature, 
            update_time,))
    except:
        output = "please enter valid command or city: "
    history.append(city)
    return output

def main():
    while True:
        typein = input("please enter valid command or city: ")
        if typein.lower() == 'help':
            print(query_help())
        elif typein.lower() == 'quit':
            break
        elif typein.lower() == 'history':
            print(history)
        else:
            print(query_weather_api(typein))

if __name__ == '__main__':
    main()
