#! python3
# -*- coding: utf-8 -*-

import random

target = random.randint(0, 20)
#print("target value: %d" % target)
guess = 10

def guess_value(value, target, guess):
    try:
        if int(value) > target:
            info = "higher than target, %d time try left" % guess
        elif int(value) < target:
            info = "lower than target, %d time try left" % guess
        else:
            info = "congratulations!"
    except:
        info = "please enter valid number, %d time try left" % guess
    return info
        
    
while True:
    
    if guess > 1:
        guess -= 1
        value = input("Gussess the number: ")
        feedback = guess_value(value, target, guess)
        print(feedback)
        if feedback == "congratulations!" :
            break
    else:
        feedback = "Sorry, no try left!"
        print(feedback)
        break