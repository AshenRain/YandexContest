
gen = []
def generation(q, depth, num = ''):
    if depth != 0:
        for i in q:
            generation(q, depth - 1, num + i)
    else:
        gen.append(num)

'''
#Пример 3
k = 2
c = ['1','2']
a = ['1','2','1','2','2','2']
'''

'''
#Пример 2
k = 3
c = ['1']
a = ['1','1','1','1','1','1']
'''

'''
#Пример 1
k = 2
c = ['1','2','3','4','5','6']
a = ['1','2','3','4','5','6']
'''

generation(c,k)
#for i in gen: print(i)
#print('len(gen) = ',len(gen))

prob = dict() #вероятности сторон кубика
for i in a: prob[i] = prob.get(i,0) + 1/6

m = dict()
for i in gen:
    p = 1
    sum = 0
    for j in range(k): 
        p*= prob[i[j]] #рассчет вероятностей события
    for j in range(k-1,0,-1):
        if i[j] == i[j-1]: 
            i = list(i)
            i.pop(j) #удаление повторящющихся эл-ов
    for j in i:
        sum += int(j) #сумирование оствашихся цифр для мат. ожид.
    m[sum] = m.get(sum,0) + p

mat_o = 0
for k,v in sorted(m.items()):
    print(k,v)
    mat_o += k*v
print('Математическое ожидание: ',mat_o) 
