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