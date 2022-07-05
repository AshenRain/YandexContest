from random import uniform
from math import cos,sin,pi
import matplotlib.pyplot as plt
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

def add_titlebox(ax, text):
    ax.text(.55, .8, text,
        horizontalalignment='left',
        transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.6),
        fontsize=12.5)
    return ax

#100 * 2000
gen1,gen2 = [],[]
s1,s2 = 0,0
for i in range(1000):
    a = generate1()
    b = generate2()
    s1 += a[0]**2 + a[1]**2
    s2 += b[0]**2 + b[1]**2
    gen1.append(a)
    gen2.append(b)
print(s1/2000,s2/2000)
gen1 = np.array(gen1)
gen2 = np.array(gen2)


"""
data = np.column_stack(gen1)

fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(16, 8)
)

ax1.scatter(gen1[:,0],gen1[:,1], c = 'red', s = 1)
ax1.scatter(gen2[:,0],gen2[:,1], c = 'blue',s = 1)
ax1.set_facecolor('black')   #  цвет области Axes
ax1.set_title('Распределение точек')     #  заголовок для Axes

ax2.hist(
        data, bins=np.arange(data.min(),data.max()),
        label=('gen1','gen2')
)

"""



gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))

ax1.scatter(gen1[:,0],gen1[:,1], c = 'red', s = 1)
ax1.scatter(gen2[:,0],gen2[:,1], c = 'blue',s = 1)
ax1.set_facecolor('black')   #  цвет области Axes
ax1.set_title('Распределение точек')     #  заголовок для Axes
ax2.hist(gen1, bins='auto')
ax3.hist(gen2, bins='auto')

add_titlebox(ax2, 'Histogram: gen1')
add_titlebox(ax3, 'Histogram: gen2')
plt.show()
