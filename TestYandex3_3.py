from random import uniform
from math import cos,sin,pi
import numpy as np

def generate1():  
    a = uniform(0, 1)  
    b = uniform(0, 1)  
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))

def generate2():  
    while True:  
        x = uniform(-1, 1)  
        y = uniform(-1, 1)  
        if x ** 2 + y ** 2 > 1:  
            continue  
        return (x, y)


kit = []
for i in range(100):
    text = ''
    choice = uniform(0, 1)
    if choice < 0.5: 
        print('ch 1')
        for i in range(2000):
            t = generate1()
            text += str(t[0]) + ' ' + str(t[1]) + ' '
    else:
        print('ch 2')
        for i in range(2000):
            t = generate2() #это можно не дублировать, но вопрос как это делается в python
            text += str(t[0]) + ' ' + str(t[1]) + ' '
    kit.append(text)


print('test')
for j in kit:
    gen = [float(i)**2 for i in j.split()]
    s = 0
    for i in gen:
        s += i
    #print(s/(len(gen)*2))
    #print(len(gen))
    if s/(len(gen)) < 0.2: print(1)
    else: print(2)
 




"""
#То что посылаем на задание
for j in range(100):
    gen = [float(i)**2 for i in input().split()]
    s = 0
    for i in gen:
        s += i
    if s/(len(gen)*2) < 0.2: print(1)
    else: print(2)
"""

