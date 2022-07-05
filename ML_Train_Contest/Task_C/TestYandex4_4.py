from collections import defaultdict
import copy

n_cities = int(input())
cities = defaultdict(dict)

for i in range(n_cities):
    city,n_rooms = input().split()
    for j in range(int(n_rooms)):
        time,room = input().split()
        time = time.replace('.','1')
        time = time.replace('X','0')      
        cities[city][room] = time


requests = int(input())
for i in range(requests):
    n,*req = input().split()
    shard = dict() # словарь [вариант][[комнта города 1][комнта города 2]...[комнта города n]]
    shard[0] = list()
    for city in req:
        tmp_copy = [] #список со словорями 
        for j in range(len(cities[city])): #сколько комнат, столько и копий
            tmp_copy.append(copy.deepcopy(shard))   
        index = 0
        for room in cities[city]:
            for k,v in tmp_copy[index].items():
                tmp_copy[index][k].append(room) # [номер копии][ключ].append(комната конкретного города)
                #то есть таким образом, постепенно мы получим все комбинации комнат
            index += 1
        
        shard.clear()
        for tmp in tmp_copy:
            for k,v in tmp.items():
                shard[(k + 1)*(tmp_copy.index(tmp)+1)] = v #формула для ключа сделана для уникальности

    fl = True
    for k,v in shard.items():

      #работаем с v, точнее подставляем значения поочередно перемножая побитово
      time = int('0b' + cities[req[0]][v[0]], base=2)
      for i in range(1,len(req)):
        #cities[req[index]][v[index]] - время     
        time_tmp =  int('0b' + cities[req[i]][v[i]], base=2)
        time = time & time_tmp
      if time != 0: 
          print('Yes ' + ' '.join([i for i in v]))
          fl = False
          break
    if fl: print('No')