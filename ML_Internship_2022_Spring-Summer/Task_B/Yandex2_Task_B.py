n = int(input())
archive = []
for i in range(n):
    x,y = [int(c) for c in input().split()]
    archive.append([x,y])

last = [0,0]
s = 0
for i in range(n):
    x = archive[i][0] - last[0]
    y = archive[i][1] - last[1]
    second = (x*x + y*y)**(0.5)
    #print(x*x + y*y)
    s += second
    last = archive[i]
#print('-'*40)
fl = False #флаг для обработки исключения
tops_l = []
for i in range(n - 1):
    j = 0
    while j < len(tops_l):
        # условие что эта вершина не следующая, и выше указанной
        if fl and i - tops_l[j][1] > 1 and  archive[i][1] >= tops_l[j][0][1]:
            x = archive[i][0] - tops_l[j][0][0]
            y = archive[i][1] - tops_l[j][0][1]
            second = (x*x + y*y)**(0.5)
            #print(x*x + y*y)
            s += second           
            tops_l.remove(tops_l[j])
            j -= 1
        j += 1
    if archive[i][1] >= archive[i + 1][1]:
        tops_l.append((archive[i], i))
        fl = True

print(s)
#print('_'*50)

"""
fl = False
tops_r = []
for i in range(1,n + 1):
    j = 0
    index = n - i
    while j < len(tops_r):
        if fl and tops_r[j][1] - index > 1 and archive[index][1] > tops_r[j][0][1]: 
            x = archive[index][0] - tops_r[j][0][0]
            y = archive[index][1] - tops_r[j][0][1]
            second = (x*x + y*y)**(0.5)
            #print(x*x + y*y)
            s += second
            tops_r.remove(tops_r[j])
            j -= 1
        j += 1
    if i != n + 1 and archive[index][1] >= archive[index - 1][1]:
       tops_r.append((archive[index], index))
       fl = True

print(s)
"""




"""
6
3 2
5 1
7 1
9 3
11 7
12 1

#27.307707393305986

10
3 5
5 1
6 3
7 1
8 2
9 1
10 4
11 2
14 7
16 1

#58.28937642030368

4
1 2
2 2
3 2
4 1

#5.650281539872885

#права
4
1 4
2 2
3 3
4 1


#подъем
4
1 2
2 3
3 4
4 1

5
1 2
2 3
3 4
4 5
5 1


"""

