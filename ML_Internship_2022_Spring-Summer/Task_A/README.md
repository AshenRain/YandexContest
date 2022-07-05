![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_A/1.jpg)
![Image alt](https://github.com/AshenRain/YandexContest/raw/main/ML_Internship_2022_Spring-Summer/Task_A/2.jpg)

Код:

```
from collections import defaultdict

def zaraza(meetings, meet_zaraza, pcr, arhcive):
    for worker in meetings[meet_zaraza][1:]:
        if pcr[worker] == 0:
            pcr[worker] = 1
            index = archive[worker].index(meet_zaraza) #таким образом, мы знаем с какой встречи он заразился
            for meet in archive[worker][index:]:
                if meetings[meet][0] == 0:
                    meetings[meet][0] = 1 #нужно ли это, так как потом из за этого повторно будет проходить
                    zaraza(meetings, meet, pcr, arhcive)

fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()

n = int(text_line[0])
pcr = list(map(int, text_line[1].split()))
meetings = dict() #хранит в себе всех сотрудников, которые посещали определенную встречу
archive = dict()  #хранит в себе порядок посещения для каждого сотрудника
index_worker = 0

for line in text_line[2:]:
    count_meeteings, *meet = map(int, line.split()) 
    archive[index_worker] = []
    for i in range(count_meeteings):
        archive[index_worker].append(meet[i])
        if meetings.get(meet[i], False):
            if index_worker not in meetings[meet[i]][1:]:
                if pcr[index_worker] != 0 and meetings[meet[i]][0] == 0:
                    meetings[meet[i]][0] = 1
                meetings[meet[i]].append(index_worker)
        else:
            meetings[meet[i]] = [pcr[index_worker], index_worker]
    index_worker +=1

print('pcr', pcr)
print('meetings ', meetings)
print('archive ', archive)

for meet in meetings.keys():
    if meetings[meet][0] != 0:
        zaraza(meetings,meet,pcr,archive)
        
print(*pcr)

```

Пример 1:

```
Ввод:
4
1 0 0 1
1 1
1 1
0
0

Вывод:
1 1 0 1 

```
