#Задача 1
#print(len((set(input().split())) & ((set(input().split())))))
#Задача из 5 лекции

""" 
def countzeroxumranges(nums):
    cntranges = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            rangesum = 0
            for k in range(i,j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges += 1
    return cntranges


num = [int(i) for i in input().split()]
print(countzeroxumranges(num))

#1 0 0 1 0 1 0 0 0 1
"""

#Задача 5.1

"""
def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1,len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum

def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l - 1]

n,q = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]

prefix_array = makeprefixsum(array)
for i in range(q):
    l,r = [int(s) for s in input().split()]
    print(rsq(prefix_array,l,r))

"""

#Задача 5.2

"""
def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1,len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum

def max_sum(prefixsum):
    maxs = prefixsum[1]
    for i in range(len(prefixsum)):
        for j in range(i + 1, len(prefixsum)):
            maxs = max(maxs,(prefixsum[j] - prefixsum[i]))
    return maxs

n = int(input())
array = [int(i) for i in input().split()]

prefix_array = makeprefixsum(array)
print(max_sum(prefix_array))
"""

#Задача 5.3

"""
def num_pack_sort(nums):
    array = []
    for i in range(len(nums)):
       array.append([i+1,nums[i]])
    array.sort(key = lambda x: x[1])
    return array

def max_group(group,classroom):
    journal = {a+1: 0 for a in range(len(group))}
    count = 0
    i = 0
    j = 0
    while i < len(group) and j < len(classroom):
        if group[i][1] + 1 <= classroom[j][1]:
            journal[group[i][0]] = classroom[j][0]
            count += 1
            i += 1
        j += 1
    return count,journal

n,m = [int(i) for i in input().split()]
n_array = [int(i) for i in input().split()]
m_array = [int(i) for i in input().split()]

n_array = num_pack_sort(n_array)
m_array = num_pack_sort(m_array)
count,journal = max_group(n_array,m_array)
print(count)
for k,v in journal.items():
    print(v,end=' ')


#n_array = [2,3,3,4,5,6]
#m_array = [3,4,4,5,5,7]

#n_array = [4,6,5,3,3,2]
#m_array = [5,5,4,3,7,4]
"""

#Задача 5.3 от разработчика

"""
def readandenum():
    x = list(map(int,input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i + 1)
    x.sort()
    return x

n, m = map(int,input().split())
x = readandenum()
y = readandenum()
ynum = 0
ans = [0] * (n+1)
cnt = 0
for pupils, xnum in x:
    while ynum < len(y) and y[ynum][0] < pupils + 1:
        ynum += 1
    if ynum == len(y):
        break
    ans[xnum] = y[ynum][1]
    ynum += 1
    cnt+= 1
print(cnt)
print(*ans[1:])
"""

"""
3 3
1 2 3
3 4 2
"""

#Задача 5.4
"""
def pravilo(stroka):
    balance = 0 
    if len(stroka)%2 != 0:
        return 'NO'
    for c in str:
        if c == '(': balance +=1
        else: balance -=1
        if balance < 0:
            return 'NO'
    if balance != 0: return 'NO'
    else: return 'YES'

str = input()
print(pravilo(str))
"""

#Задача 6.1

"""
def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1)// 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def check_right(index,params):
    seq,x = params
    return seq[index] <= x

def check_left(index, params):
    seq,x = params
    return seq[index] >= x

def countx(seq, l, r):
    index_right = rbinsearch(0, len(seq) - 1, check_right, (seq,r))
    index_left = lbinsearch(0, len(seq) - 1, check_left, (seq,l))
    if (index_left == index_right == 0 and seq[0] > r) or (index_left == index_right == (len(seq) - 1) and seq[-1] < l):
        return 0
    return index_right - index_left + 1

n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()
q = int(input())

answer = []
for i in range(q):
    l,r = [int(j) for j in input().split()]
    answer.append(countx(nums, l, r))
print(*answer)

"""

"""
6
3 5 6 10 18 22
3
-10 4
-3 -2
1 1
1 7 7

6
-10 -2 0 2 10 12
3
-3 1
-11 -2
-2 12

2 2 5 
"""

#Задача 6.2

"""
def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1)// 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l

def check_right(index,params):
    seq,x = params
    return seq[index] <= x

def check_left(index, params):
    seq,x = params
    return seq[index] >= x

def countx(seq, x):
    index_right = rbinsearch(0, len(seq) - 1, check_right, (seq,x))
    index_left = lbinsearch(0, len(seq) - 1, check_left, (seq,x))
    if (index_left == index_right == 0 and seq[0] > x) or (index_left == index_right == (len(seq) - 1) and seq[-1] < x) or index_left > index_right:
        return (0,0)
    return (index_left + 1,index_right + 1)

n = int(input())
nums = [int(i) for i in input().split()]
q = int(input())
x = [int(j) for j in input().split()]

for i in range(q):
    print(*countx(nums, x[i]))

"""


#Задача 6.3

"""
def check_coren_up(x,params):
    a,b,c,d = params
    return a*x**3 + b*x**2 + c*x + d > 0

def check_coren_down(x,params):
    a,b,c,d = params
    return a*x**3 + b*x**2 + c*x + d < 0

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m,checkparams):
            r = m
        else:
            l = m
    return l

eps = 0.00001
nums = [int(i) for i in input().split()]

if nums[0] > 0:
    print(fbinsearch(-100000, 100000, eps, check_coren_up, nums))
else:
    print(fbinsearch(-100000, 100000, eps, check_coren_down, nums))
"""


"""
def check_less(days,params):
    a,k,b,m,x = params
    return a*(days - days//k) + b*(days - days//m) >= x

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

nums = [int(i) for i in input().split()]
print(lbinsearch(0,nums[-1],check_less,nums))
"""

#Задача на таблицу exel zz -> 702 ac -> 29

"""
def exel_num(str):
    sum = 0
    ex = 1
    for i in range(len(str)):
        sum += (ord(str[i]) - 64)*(26**(len(str)- ex))
        ex += 1
    return sum

print(exel_num(input()))
"""

#Задача на полиндром

"""
def palindrome(str):
    begin = 0
    end = len(str) - 1
    while begin < end:
        while not str[begin].isalpha():
            begin += 1
        while not str[end].isalpha():
            end -= 1
        if str[begin].lower() != str[end].lower():
            return False
        begin += 1
        end -= 1
    return True

print(palindrome(input()))
"""

#Задача 7.2

"""
def color_paint(n, cin, cout):
    events = []
    for i in range(n):
        events.append((cin[i], -1))
        events.append((cout[i], 1))
    events.sort()
    online = 0
    painted = 0
    for i in range(len(events)):
        if online > 0:
            painted += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return painted

n = int(input())
l = [0]*n
r = [0]*n
for i in range(n):
    l[i],r[i] = [int(c) for c in input().split()]
print(color_paint(n,l,r))
"""

#Задача 7.3

"""
def cargo_time(n, cin, cout):
    events = []
    for i in range(n):
        events.append((cin[i], 1))
        events.append((cout[i], -1))
    events.sort()
    online = 0
    machine = 0
    for i in range(len(events)):
        if events[i][1] == 1:
            online += 1
            machine = max(online,machine)
        else:
            online -= 1
    return machine

n = int(input())
l = [0]*n
r = [0]*n
for i in range(n):
    l[i],timer = [int(c) for c in input().split()]
    r[i] = l[i] + timer
print(cargo_time(n,l,r))
"""

#Задача 7.4

"""
m = int(input())
segs = []
l, r = map(int, input().split())
while l != 0 or r != 0:
    if r > 0 and l < m:
        segs.append((l, r))
    l, r = map(int, input().split())
segs.sort()
ans = []
nowright = 0
nextright = 0
nowbest = 0, 0
for seq in segs:
    if seq[0] > nowright:
        ans.append(nowbest)
        nowright = nextright
        if nowright >= n:
            break
    if seq[0] <= nowright and seq[1] > nextright:
        nextright = seq[1]
        nowbest = seq

if nowright < m:
    nowright = nextright
    ans.append(nowbest)
if nowright < m:
    print('No solution')
else:
    print(len(ans))
    for seq in ans:
        print(*seq)

"""

#Задача 7.6

"""
from math import pi

n = int(input())
events = []
rmin = 0
rmax = 10**6
for i in range(1, n + 1):
    r1, r2, phi1, phi2 = map(float, input().split())
    rmin = max(rmin, r1)
    rmax = min(rmax, r2)
    events.append((phi1, -i))
    events.append((phi2, i))
events.sort()

used = set()
cntsegs = 0
for event in events:
    if event[1] < 0:
        cntsegs += 1
        used.add(-event[1])
    elif event[1] in used:
        cntsegs -= 1

ans = 0
for i in range(len(event)):
    event = events[i]
    if event[1] < 0:
        cntsegs += 1
    else:
        cntsegs -= 1
    if cntsegs == n:
        if i < len(events) - 1:
            ans += (events[i + 1][0] - events[i][0]) * (rmax ** 2 - rmin **2) / 2
        else:
            ans += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2
print(ans)
"""

#Задача 8.2

"""
#Менеджер памяти

def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]

def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


#Реализация поиска

def find(memsturct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            retrun = -1
        else: 
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)
    return -1

#Реализация добавления

def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]
    tmp = ''
    if x == key:
        return 'ALREADY'
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
            return 'DONE'
        else:
            return add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
            return 'DONE'
        else:
            return add(memstruct, right, x)

def printtree(memsturct, root, depth = 0):
    key = memstruct[0][root][0]
    if memstruct[0][root][1] != -1:
        printtree(memstruct, memstruct[0][root][1], depth + 1)
    print(f"{''.join('.' * depth)}{key}")
    if memsturct[0][root][2] != -1:
        printtree(memstruct, memstruct[0][root][2], depth + 1)
    if memstruct[0][root][1] == -1 and memstruct[0][root][2] == -1:
        return 

fin = open('input.txt', 'r', encoding='utf8')
memstruct = initmemory(1000)
fl = False
command = []
root = -1
for line in fin:
    command = line.split()
    if not fl and command[0] == 'ADD':
        root = createandfillnode(memstruct, int(command[1]))
        print('DONE')
        fl = True
    elif fl and command[0] == 'ADD':
        print(add(memstruct, root, int(command[1])))
    elif command[0] == 'SEARCH':
        if root != -1 and find(memstruct,root,int(command[1])) != -1:
            #print(find(memstruct,root,int(command[1])))
            print('YES')
        else: 
            print('NO')
    elif command[0] == 'PRINTTREE':
        printtree(memstruct, root)
#print(memstruct)

"""

#Задачака 8.3
#TL

"""
def found_pred(nod,pred):
    fl = 0
    for i in range(len(des)):
        if nod == des[i]:
            if par[i] == pred:
                fl = 2
                break
            elif par[i] == end and par[i] != pred:
                break
            fl = found_pred(par[i],pred)
        elif pred == end: 
            fl = 2
            break
    return fl



#Ввод
fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()

n = int(text_line[0])
gen = {}
des,par = [],[]

for i in range(n - 1):
    des_one,par_one = text_line[i + 1].split()
    des.append(des_one)
    par.append(par_one)

#Поиск родоначальника
for i in range(n - 1):
    if par[i] not in des:
        end = par[i]
        break

tmp = []
for i in range(len(text_line) - n):
    des_one,par_one = text_line[i + n].split()
    tmp.append(int(found_pred(des_one,par_one) +  found_pred(par_one,des_one)/2))
print(*tmp)

"""

#Задачка 8.3
#Не моя

"""
# TODO: Не забудь поменять имя файла на 'input.txt' перед отправкой в контест
file = open('input.txt')
lines = file.readlines()
file.close()

n = int(lines[0])

# 1. Заполняем словарь родственников
rel_map = {}
for line in lines[1: n]:
    anc, pre = line.split()
    if pre not in rel_map:
        rel_map[pre] = [anc]
    else:
        rel_map[pre].append(anc)

print(rel_map)

# 2. Определяем функцию поиска потомка
def rel_exists(predecessor, ancestor):
    re_flag = []

    def rel_exists_recur(p, a, flag: []):
        if p not in rel_map:
            return

        anc_list = rel_map[p]
        print(anc_list)
        if a in anc_list:
            flag.append(True)
            return

        for aa in anc_list:
            if not flag:
                rel_exists_recur(aa, a, flag)

    rel_exists_recur(predecessor, ancestor, re_flag)
    return bool(re_flag)


# 3. Обрабатываем запросы
request_results = []

for request in lines[n:]:
    first, second = request.split()
    if rel_exists(first, second):
        request_results.append('1')
    elif rel_exists(second, first):
        request_results.append('2')
    else:
        request_results.append('0')

# 4. Выводим результаты
print(' '.join(request_results))
"""

#Задачка 8.4

"""
def req(nod):
    for i in range(len(des)):
        if  nod == par[i]:
            gen[des[i]] = gen[nod] + 1
            req(des[i])

fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()

n = int(text_line[0])
gen,search = {},{}
des,par = [],[]

#Ввод
for line in text_line[1:n]:
    des_one,par_one = line.split()
    des.append(des_one)
    par.append(par_one)
    #Словарь для поиска общего родителя
    search[des_one] = par_one

#Поиск родоначальника
for i in range(n - 1):
    if par[i] not in des:
        gen[par[i]] = 0
        req(par[i])
        break
'''
for peop in sorted(gen):
    print(peop,gen[peop])
'''
#Подьем по дереву от потомков, без перебора всех родителей
for request in text_line[n:]:
    lca_1,lca_2 = request.split()
    for i in range(len(gen)):
        if gen[lca_1] == gen[lca_2]:
            if lca_1 == lca_2:
                print(lca_1)
                break
            elif search[lca_1] == search[lca_2]:
                print(search[lca_1])
                break
            lca_1,lca_2 = search[lca_1],search[lca_2]
        elif gen[lca_1] > gen[lca_2]:
            lca_1 = search[lca_1]
        else:
            lca_2 = search[lca_2]

"""

# TODO: Не забудь поменять ввод на 'input.txt'
file = open('input_d_12.txt')
lines = file.readlines()
file.close()

n = int(lines[0])
rel_map = {}

# 1. Заполняем map со связями между узлами:
for i in range(1, n):
    parent, child = map(int, lines[i].split())

    if parent not in rel_map:
        rel_map[parent] = [child]
    else:
        rel_map[parent].append(child)

    # Заполняем связи в обратную сторону,
    # так как по условию у нас неориентированный граф:
    if child not in rel_map:
        rel_map[child] = [parent]
    else:
        rel_map[child].append(parent)


# 2. Определяем функцию поиска листов дерева
#    (или по-другому - конечных точек нецикличного неориентированного графа).
#    Признак листа - всего одна связь с другим узлом.
def get_leaves():
    leaves_list = []
    for node in rel_map:
        if len(rel_map[node]) == 1:
            leaves_list.append(node)
    return leaves_list


# 3. Определяем функцию поиска диаметра дерева (наибольшего пути графа).
#    Идея заключается в том, чтобы каждый раз находить листы дерева,
#    затем удалять их из дерева и добавлять к искомому значению 2,
#    пока в дереве не останется меньше двух элементов.
#    После этого прибавляем еще 1, если остался один (нечетный корневой) элемент, и выводим результат.
#
#    Тут стоит отдельно отметить, что наибольший путь в таком дереве (или ацикличном ненаправленном графе)
#    это всегда путь от одного листа до другого через его корень.
#    Прибавляем 2, а не 1, потому что удаляя листья, мы на каждом этапе
#    сокращаем наш искомый наибольший путь сразу на 2 элемента.

def find_diameter():
    global rel_map
    dist = 0

    while len(rel_map) >= 2:
        leaves = get_leaves()
        for leaf in leaves:
            for leaf_child in rel_map[leaf]:
                rel_map[leaf_child].remove(leaf)
            rel_map.pop(leaf)
        if len(leaves) < 2:
            dist += 1
        else:
            dist += 2

    dist += len(rel_map)

    print(dist)


find_diameter()