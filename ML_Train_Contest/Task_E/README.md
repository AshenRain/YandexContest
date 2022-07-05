

![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Task_E/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Task_E/2.jpg)


Код:

```
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def input_points_train(stroki):
    train_x = []
    train_y = []
    tmp = []
    for i in range(1000):
        tmp = list(map(float, stroki[i].split(sep = '\t')))
        train_x.append(tmp[:5])
        train_y.append(tmp[-1])
    return train_x, train_y


fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close

x,y = input_points_train(text_line[:1000])
x,y = np.array(x), np.array(y)
lin_reg = LinearRegression()
poly_reg = PolynomialFeatures(degree=3)
poly_x = poly_reg.fit_transform(x)
lin_reg.fit(poly_x,y)

x_val, y = input_points_train(text_line[1000:])
x_val = np.array(x_val)
x_pol = poly_reg.fit_transform(x_val)

for i in range(1000):
        print('{:.6f}'.format(lin_reg.predict([x_pol[i]])[0]))
```

Код генератора (Для примера, не обязательно что функция будет именно такая)

```
from random import uniform

def generate1():  
    x1 = uniform(-100, 100)  
    x2 = uniform(-100, 100)
    x3 = uniform(-100, 100)
    x4 = uniform(-100, 100)
    x5 = uniform(-100, 100)
    y = x1 * x2 * x2 + x3 * x4 + x5
    tmp = str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\t' + str(x5) + '\t' + str(y)
    return tmp

def generate2():  
    x1 = uniform(-100, 100)  
    x2 = uniform(-100, 100)
    x3 = uniform(-100, 100)
    x4 = uniform(-100, 100)
    x5 = uniform(-100, 100)
    tmp = str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\t' + str(x5)
    return tmp

"""
f = open('train.txt', 'w')
f2 = open('validate.txt', 'w')

for i in range(1000):
    f.write(generate1() + '\n')
    f2.write(generate2() + '\n')
    print(f"{i+1}/1000")
print('generetion complete')

f.close
f2.close
"""

f = open('input.txt', 'w')
for i in range(1000):
    f.write(generate1() + '\n')
    print(f"{i+1}/2000")
for i in range(1000):
    f.write(generate2() + '\n')
    print(f"{i+1001}/2000")
print('generetion complete')
f.close
"""
k = '-48.448298734896824	-68.90597219055338	7.105858955266825	-94.27113056025918	-81.83460737068175	-230785.8333226294'
d = list(map(float, k.split(sep = '\t')))
print(d)
"""
```
