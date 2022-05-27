import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from random import uniform
import pandas as pd

"""
print('+' + '-'*40 + '+')
X = np.array([[1, 1, 3, 3], [1, 2, 4 , 4], [2, 2, 4, 4], [2, 3 , 5, 5]])
y = np.dot(X, np.array([1, 2, 3, 4])) + 3
print(X)
print('+' + '-'*40 + '+')
print(y)
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
"""

def generate1():  
    x1 = uniform(-100, 100)  
    x2 = uniform(-100, 100)
    x3 = uniform(-100, 100)
    x4 = uniform(-100, 100)
    x5 = uniform(-100, 100)
    y = x1 * x2 * x2 + x3 * x4 + x5
    return y, x1, x2, x3, x4, x5 

train_x,test_x = [],[]
train_y,test_y = [],[]

for i in range(1000):
    print(f"generate {i+1}/1000")
    y1,*x1 = generate1()
    y2,*x2 = generate1()
    train_y.append(y1)
    train_x.append(x1)
    test_y.append(y2)
    test_x.append(x2)

train_x = np.array(train_x)
train_y = np.array(train_y)
lin_reg = LinearRegression()
poly_reg = PolynomialFeatures(degree=5)
poly_train_x = poly_reg.fit_transform(train_x)
lin_reg.fit(poly_train_x,train_y)
print('coefficient of determination:',lin_reg.score(poly_train_x, train_y))

sum_v = 0
sum_test = 0
test_x = np.array(test_x)
poly_test_x = poly_reg.fit_transform(test_x)
test_y = np.array(test_y)
print('{0:20} |  {1}'.format('validate', 'test'))
for i in range(1000):
    #print('{0:20} | {1}'.format(test_y[i], lin_reg.predict([poly_test_x[i]])))
    sum_v += test_y[i]
    sum_test += lin_reg.predict([poly_test_x[i]])

print(sum_v,sum_test)
print(sum_v/sum_test)


"""
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values  
y = dataset.iloc[:,2].values
print(X)
"""