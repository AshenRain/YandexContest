import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def input_points_train(stroki):
    train_x = []
    train_y = []
    tmp = []
    for i in range(1000):
        tmp = list(map(float, stroki[i].split(sep = '\t')))
        #tmp[:5] = [x*100 for x in tmp[:5]]
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

x_val, yy = input_points_train(text_line[1000:])
print('Before np.array',x_val[0])
np.set_printoptions(precision=20)
x_val = np.array(x_val, dtype=np.float64)
print('After np.array ',x_val[0])
x_pol = poly_reg.fit_transform(x_val)
tmp = x_val[0][0] * x_val[0][1] * x_val[0][1]+ x_val[0][2]* x_val[0][3] + x_val[0][4]
# y = x1 * x2 * x2 + x3 * x4 + x5
print('tmp ', tmp)
print('     {:.6f}'.format(lin_reg.predict([x_pol[0]])[0]))
print(tmp - lin_reg.predict([x_pol[0]])[0])

tmp = x_val[1][0] * x_val[1][1] * x_val[1][1]+ x_val[1][2]* x_val[1][3] + x_val[1][4]
print('tmp ', tmp)
print('     {:.6f}'.format(lin_reg.predict([x_pol[1]])[0]))
print(tmp - lin_reg.predict([x_pol[1]])[0])
#for i in range(1000):
 #   print('{:.6f}'.format(lin_reg.predict([x_pol[i]])[0]))