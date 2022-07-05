'''
a = input().split()
k = int(input())
c = set(a) #уникальные стороны кубика
'''


def generation(q, depth, num = ''):
    if depth != 0:
        for i in q:
            generation(q, depth - 1, num + i)
    else:
        #gen.append(num)
        print(num)
        p = 1
        sum = 0
        for j in range(k): 
            p*= prob[num[j]] #рассчет вероятностей события
        for j in range(k-1,0,-1):
            if num[j] == num[j-1]: 
                num = list(num)
                num.pop(j) #удаление повторящющихся эл-ов
        for j in num:
            sum += int(j) #сумирование оствашихся цифр для мат. ожид.
        m[sum] = m.get(sum,0) + p



k = 6
c = ['1','2','3','4','5','6']
a = ['1','2','3','4','5','6']

gen = []
m = dict()
prob = dict() #вероятности сторон кубика
for i in a: prob[i] = prob.get(i,0) + 1/6
generation(c,k)#генерация уникальных комбинаций

mat_o = 0
for k,v in m.items():
    mat_o += k*v
print(mat_o) 
