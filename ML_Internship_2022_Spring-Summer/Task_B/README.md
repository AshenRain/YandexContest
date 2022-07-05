![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_B/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_B/2.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_B/3.jpg)

Код:

```
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

tops = [(archive[0],0)]
for i in range(1,n - 1):
    j = 0
    while j < len(tops):
        # условие что эта вершина не следующая, и выше указанной
        if i - tops[j][1] > 1 and  archive[i][1] > tops[j][0][1]:
            x = archive[i][0] - tops[j][0][0]
            y = archive[i][1] - tops[j][0][1]
            second = (x*x + y*y)**(0.5)
            #print(x*x + y*y)
            s += second
            tops.remove(tops[j])
            j -= 1
        j += 1
    if archive[i][1] > archive[i + 1][1]:
        tops.append((archive[i], i))

print(s)

```

Пример 1:

```
6
3 2
5 1
7 1
9 3
11 7
12 1

#27.307707393305986
```

Пример 2:

```
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
```

Пример 3:

```
4
1 2
2 2
3 2
4 1

#5.650281539872885
```
