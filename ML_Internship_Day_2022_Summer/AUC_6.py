def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

x = []
for i in range(int(input())):
    ti,yi = input().split()
    x.append((float(ti), float(yi)))
    
t = sorted(x ,key = lambda y: (y[0], y[1]))
print(t)

# Поиск общего кол-ва пар
less_t = [0]
for i in range(1,len(t)):
    if t[i-1][0] < t[i][0]: less_t.append(i)
    else: less_t.append(less_t[i-1])
pair_all = sum(less_t)

# Поиск числа пар, равных по значению
cnt = {t[0][1]:1}
eq_y = [0]
for i in range(1,len(t)):
    if t[i-1][0] == t[i][0] and t[i-1][1] == t[i][1]: 
        eq_y.append(eq_y[i-1])
    else:
        eq_y.append(cnt.get(t[i][1], 0))
    cnt[t[i][1]] = cnt.get(t[i][1], 0) + 1
pair_equal = sum(eq_y)

# Поиск числа пар где t[i-1] < t[i] и y[i-1] > y[i]
t,inv = mergeSortInversions([x[1] for x in t])

# Финальный подсчет
auc = (pair_all - inv - 0.5*pair_equal)/pair_all
print('{:.6f}'.format(auc))

"""
4
1 0.1
1 0.4
2 0.35
2 0.8

0.75


2
1 1
0 0

10
0 4
3 0
1 2
2 4
1 0
2 1
4 1
2 1
4 4
0 0

0.538462
"""
