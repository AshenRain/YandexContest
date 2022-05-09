import copy

def generation(q, depth, num = ''):
    if depth != 0:
        for i in q:
            generation(q, depth - 1, num + i)
    else:
        num_tmp = copy.deepcopy(num)
        p = 1
        sum = 0
        num = list(num)
        for j in range(k-1,0,-1):
            if num[j] == num[j-1]: 
                num.pop(j) #удаление повторящющихся эл-ов
        for j in num:
            sum += int(j) #сумирование оствашихся цифр для мат. ожид.
        if sum not in m:
            for j in range(k): 
               p*= prob[num_tmp[j]] #рассчет вероятностей события 
            m[sum] = [p] #общая вероятность для данной суммы
            m[sum].append(p) #вероятность для одного такого выпадения
        else:
             m[sum][0] += m[sum][1] 

a = input().split()
k = int(input())
c = set(a) #уникальные стороны кубика
m = dict()
prob = dict() #вероятности сторон кубика
for i in a: prob[i] = prob.get(i,0) + 1/6
generation(c,k)#генерация уникальных комбинаций

mat_o = 0
for k,v in m.items():
    mat_o += k*v[0]
print(mat_o) 
