
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Task_D/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/Task_D/2.jpg)

Код:

```
def read_ints():
    return map(int, input().split())
 
 
n, k = read_ints()
a = list(read_ints())
 
counts = [0] * (k + 1)
absent = k
cost = 0
 
ans = sum(a) + 1
 
right = -1
for left in range(n):
    while right + 1 < n and absent > 0:
        right += 1
        value = a[right]
        cost += value
 
        if value <= k:
            if counts[value] == 0:
                absent -= 1
 
            counts[value] += 1
 
    if absent == 0:
        ans = min(ans, cost)
 
    value = a[left]
    cost -= value
 
    if value <= k:
        counts[value] -= 1
 
        if counts[value] == 0:
            absent += 1
 
print(ans)
```

Пример 1:

```
Ввод
6 3
1 2 2 3 3 1

Вывод
8
```

Пример 2:

```
Ввод
5 3
1 2 5 4 3

Вывод
15
```

Пример 3:

```
Ввод
6 3
1 2 6 3 3 1
Вывод
12
```

Пример 4:

```
Ввод
6 1
6 2 3 1 2 3

Вывод
1
```

Пример 5:

```
Ввод
7 7
1 2 3 4 6 5 7
Вывод
28
```

Пример 6:

```
Ввод
10 2
1 9 2 4 3 1 8 2 10 9

Вывод
10
```
