x = []
for i in range(int(input())):
    ti,yi = input().split()
    x.append((float(ti), float(yi)))

x.sort(key = lambda y: (y[0],y[1]), reverse = True) 
for i in x: print(i)

i = 0
pair = 0
sum = 0
while i < len(x):
    j = i + 1
    while j < len(x):
        if x[i][0] != x[j][0]:
            pair += 1
            if x[i][1] > x[j][1]:
                sum += 1
            elif x[i][1] == x[j][1]:
                sum += 0.5
        j += 1
    i += 1
print('{:.6f}'.format(sum/pair))



"""
4
1 0.1
1 0.4
2 0.35
2 0.8

0.75


2
1 1
0 0

10
0 4
3 0
1 2
2 4
1 0
2 1
4 1
2 1
4 4
0 0

0.538462
"""

