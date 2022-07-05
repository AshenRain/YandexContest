def read_ints():
    return map(int, input().split())
 
 
n, k = read_ints()
a = list(read_ints())
 
counts = [0] * (k + 1)
absent = k #счетчик отсутсвующих чисел
cost = 0
 
ans = sum(a) + 1 #сумма для всех статуэток
 
right = -1
for left in range(n):
    while right + 1 < n and absent > 0:
        right += 1
        value = a[right]
        cost += value
 
        if value <= k: #нас интересуют числа только принадлежащие отрезку
            if counts[value] == 0:
                absent -= 1
 
            counts[value] += 1
 
    if absent == 0: #срабатывает только когда все фигурки из списка присутствуют 
        ans = min(ans, cost)
 
    value = a[left]
    cost -= value
 
    if value <= k:
        counts[value] -= 1
 
        if counts[value] == 0:
            absent += 1
 
print(ans)
