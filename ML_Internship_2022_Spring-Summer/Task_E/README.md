![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_E/1.jpg)


Код:

```
import numpy as np
from math import tan, sin, cos
from sklearn.linear_model import LinearRegression

fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close

train_x = []
train_y = []
tmp = []
n = text_line[0]
for line in text_line[1:]:
   tmp = list(map(float, line.split()))
   train_x.append([tan(tmp[0]), sin(tmp[0])**2, 2*cos(tmp[0])*sin(tmp[0]), cos(tmp[0])**2, tmp[0]**0.5])
   train_y.append([tmp[1]])


x,y = np.array(train_x), np.array(train_y)
lin_reg = LinearRegression(fit_intercept = False)
lin_reg.fit(x,y)
#print('score ',lin_reg.score(x,y))
#print(lin_reg.coef_)
#print(len(lin_reg.coef_[0]))
coef = [lin_reg.coef_[0][0], (lin_reg.coef_[0][1])**0.5, (lin_reg.coef_[0][3])**0.5, lin_reg.coef_[0][4]]

for i in coef:
    print("{:.2f}".format(i), end = ' ')

```


Пример 1:

```
Ввод:
20
0.5 7.11
1.0 6.69
1.5 4.97
2.0 4.25
2.5 5.75
3.0 8.58
3.5 10.56
4.0 10.26
4.5 8.32
5.0 6.86
5.5 7.54
6.0 10.04
6.5 12.35
7.0 12.62
7.5 10.88
8.0 8.97
8.5 8.91
9.0 10.99
9.5 13.53
10.0 14.42

Вывод:
0.00 1.00 2.00 3.00

```
