#! python3
# -*- coding: utf-8 -*-

import json
import os.path

##pardir obtain parent address
filename = os.path.pardir + r'\resource\weather_info.txt'  
fhand = open(filename, 'r', encoding='utf-8')  #encoding statement
lines = fhand.readlines()
weather_data = {}
history_data = []

for data in lines:
    seperator = data.index(',')
    city = data[:seperator]
    weather = data[seperator + 1:].rstrip()
    weather_data[city] = weather

def query_weather(city):
    if city in weather_data.keys():
        result = weather_data[city]
        history_data.append(city)
    else:
        result = "please enter valid command or city: "
    return result

def query_help():
    result = """
            typein 'help' to check help doc
            typein 'quit' to exit scrpit
            typein 'city name' to check weather
            typein 'history' to check correct query history
            """
    return result


def main():
    while True:
        typein = input("please enter valid command or city: ")
        if typein == 'help':
            print(query_help())
        elif typein == 'quit':
            fhand.close()
            break
        elif typein == 'history':
            print(history_data)
        else:
            print(query_weather(typein))
       
if __name__ == '__main__':
    main()
