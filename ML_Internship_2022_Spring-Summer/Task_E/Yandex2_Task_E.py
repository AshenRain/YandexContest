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
#x,y = train_x, train_y
lin_reg = LinearRegression()
#poly_reg = PolynomialFeatures(degree=2)
#poly_reg = SplineTransformer(degree = 1, n_knots = 4, knots = 'quantile')
#poly_x = poly_reg.fit_transform(x)
#print(poly_x)
lin_reg.fit(x,y)
print('score ',lin_reg.score(x,y))
print(lin_reg.coef_)
print(len(lin_reg.coef_[0]))



for i in lin_reg.coef_[0]:
    print("{:2f}".format(i), end = ' ')
