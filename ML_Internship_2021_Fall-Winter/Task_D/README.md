
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2021_Fall-Winter/Task_D/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2021_Fall-Winter/Task_D/2.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2021_Fall-Winter/Task_D/3.jpg)


Код:

```
from math import exp
from numpy import prod
from collections import defaultdict

def skill_complexity(a,b):
    return(1/(1 + exp(-a*b)))

def input_slov(n):
    slov = dict()
    for i in range(n):
        id, normal = input().split()
        slov[id] = float(normal)
    return slov

share = float(input())
workers = input_slov(int(input()))
tasks = input_slov(int(input()))
competention = defaultdict(dict)
for id,value in workers.items():
    for ik,level in tasks.items():
        p = skill_complexity(value,level)
        competention[id][ik] = [1 - p]
        competention[id][ik].append(p)

base = dict()
overlap = int(input())
for k in range(len(tasks)):
    task = input()
    answers = input_slov(overlap)
    tmp1,tmp2 = [],[]
    for worker,answer in  answers.items():
        tmp1.append(competention[worker][task][int(answer)])
        tmp2.append(competention[worker][task][int(answer) - 1])
    p1 = prod(tmp1)
    p0 = prod(tmp2)
    base[task] = p1/(p1 + p0)

for k,v in sorted(base.items()):
   print(k,round(v,4))


```

Пример 1:

```
Ввод
0.5
1
w1 10
1
t1 1
1
t1
w1 1

Вывод
t1 1.0000

```

Пример 2:

```
Ввод
0.5
3
w1 1
w2 0
w3 2
2
t1 1
t2 2
3
t1
w1 1
w2 0
w3 1
t2
w1 0
w2 1
w3 0

Вывод
t1 0.9526
t2 0.0025


```
