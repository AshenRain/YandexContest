
n,k = [int(i) for i in input().split()]
array_main = [int(i) for i in input().split()]

#Массив для готовых порядков
ready_array = []

def search_cost(array):
    #Массив для поиска
    cost_array = [[0,0]] #[сумма][id] элемента
    i = 0
    fl = False #флаг на отсутсвие элементов с id = 1, используется только на первый заход
    while(i < n):
        for id in cost_array:
            if array[i] == id[1] or array[i] == (id[1] + 1):
                id[1] += 1
                id[0] += array[i]
                if id[1] == k + 1 or id[1] == k and array[i] == k:
                    ready_array.append(id)
                    cost_array.remove(id) 
            elif id[0] != 0:
                id[0] += array[i]
          
        # условие len(cost_array) != 0 используется для исключения случая, когда k == 1, так как в данном случае cost_array был бы пустым
        if array[i] == 1 and len(cost_array) != 0 and cost_array[-1][1] != 0 and fl: 
            cost_array.append([0,0])
            #i-=1
        elif len(cost_array) != 0 and cost_array[0][1] == 1 and len(cost_array) == 1:
            cost_array.append([0,0])
            fl = True 
        print('sum ', cost_array)
        i+=1

search_cost(array_main)
print("invers")
search_cost(array_main[::-1])
print(ready_array)

min_cost = ready_array[0][0]
for id in ready_array:
    if min_cost > id[0]: min_cost = id[0]
print(min_cost)
