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
poly_reg = PolynomialFeatures(degree=5)
poly_x = poly_reg.fit_transform(x)
lin_reg.fit(poly_x,y)

x_val, y = input_points_train(text_line[1000:])
x_val = np.array(x_val)
x_pol = poly_reg.fit_transform(x_val)

for i in range(1000):
    print('{:.6f}'.format(lin_reg.predict([x_pol[i]])[0]))