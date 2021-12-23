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

gen1,gen2 = [],[]

for i in range(100):
    s1,s2 = 0,0
    for i in range(2000):
        a = generate1()
        b = generate2()
        s1 += a[0]**2 + a[1]**2
        s2 += b[0]**2 + b[1]**2
        #gen1.append(a)
        #gen2.append(b)
    #print((s1/4000)**(1/2),(s2/4000)**(1/2))
    print((s1/4000),(s2/4000))
#gen1 = np.array(gen1)
#gen2 = np.array(gen2)

"""
#Проверка на соответствие
c = 0
for i in gen1:
    if (i[0]**2 + i[1]**2) < 1: 
        print(i[0],i[1])
        c+=1
print(c/len(gen1)*100)

"""

