
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Another/ML_Internship_2021_Fall-Winter/Task_B/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Another/ML_Internship_2021_Fall-Winter/Task_B/2.jpg)


Код:

```
def rbinsearch(l, r, check, tin, p_max):
    while l != r:
        m = (l + r + 1) // 2
        if check(m, tin, p_max):
            l = m
        else:
            r = m - 1
    return l

def check_max_lim(time, tin, max_need): 
    events = []
    for i in range(len(tin)):
        events.append((tin[i], -1))
        events.append((tin[i] + time, 1))
    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        maxonline = max(online,maxonline)
        if maxonline > max_need: 
            return False 
    return True 

n,people_max = map(int, input().split())
people = []
time_max = int(input()) #Нужен для правой границы
for i in range(1,n):
    tmp = int(input())
    people.append(tmp)
    time_max = max(time_max, tmp)


result = rbinsearch(0,time_max,check_max_lim,people,people_max)
if result == 0: #левая граница
    print('Impossible')
elif result == time_max: #правая граница
    print('INF')
else:
    print(result)

```

Пример 1:

```
Ввод
8 3
3
6
4
5
0
2
7
0

Вывод
3

```

Пример 2:

```
Ввод
5 100
98
123
42
1840
999999997

Вывод
INF

```

Пример 3:

```
Ввод
7 2
7
13
9
13
13
0
3

Вывод
Impossible


```
