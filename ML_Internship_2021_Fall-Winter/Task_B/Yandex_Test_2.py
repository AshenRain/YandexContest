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



"""
n,s = [int(s) for s in input().split()]
bar = dict()
for i in range(n):
    t = int(input())
    bar[t] = bar.get(t,0) + 1


time,sum,fl,k_pred,fl_2 = 0,0,True,0,True
if bar.get(0,'f') != 'f': time = 1
for k,v in sorted(bar.items()):
    if v > s:
        print('Impossible')
        fl_2 = False
        break
    if fl:
        sum += v
        if sum <= s:
            time += k - k_pred
            k_pred = k
        else:
            fl = False

if fl_2:
    if fl:
        print('INF')
    else:
        print(time)

"""
