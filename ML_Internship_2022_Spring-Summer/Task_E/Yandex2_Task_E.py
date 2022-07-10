import numpy as np
from math import tan, sin, cos
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#from sklearn.preprocessing import SplineTransformer


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
