from random import uniform
from math import tan, sin, cos

def generate1():  
    x = uniform(0, 100)
    y = 5*tan(x) + (2*sin(x) + 3*cos(x))**2 + 10 * (x ** (0.5))
    tmp = str(x) + ' ' + str(y)
    return tmp


f = open('input.txt', 'w')
for i in range(1000):
    f.write(generate1() + '\n')
    print(f"{i+1}/1000")

f.close
