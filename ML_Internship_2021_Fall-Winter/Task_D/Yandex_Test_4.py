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


