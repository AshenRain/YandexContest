![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_C/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_C/2.jpg)


Код:

```
import statistics
fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()
numbers = []
for line in text_line[1:]:
    numbers.append(int(line))
mse = statistics.mean(numbers)
mae = statistics.median(numbers)
print(mse)
print(mae)
print(mae)
```

Пример 1:

```
10
5
4
6
7
9
2
1
3
8
0
```

