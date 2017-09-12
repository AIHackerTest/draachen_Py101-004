#! python3
# -*- coding: utf-8 -*-

import random

target = random.randint(0, 20)
print("target value: %d" % target)
guess = 10

while True:
    if guess > 1:
        try:
            value = int(input("Gussess the number: "))
            if value > target:
                guess -= 1
                print("higher than target, %d times left. Please retry: " % guess)
            elif value < target:
                guess -= 1
                print("lower than target, %d times left. Please retry: " % guess)
            else:
                print("congratulation!")
                break
        except:
            guess -= 1
            print("please enter valid number, %d times left. Please retry: " % guess)
    else:
        print("Sorry, no try left!")
        break


