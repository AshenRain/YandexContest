from collections import Counter

def lbinsearch(l, r, checkparams, check):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l
 
def searchindexcl(r, checkparams):
    def check_left_cl(index, params):
        array,x = params
        return array[index] <= x

    def check_left_cl_equal(index, params):
        array,x = params 
        return array[index][0] < x[0]

    mean = lbinsearch(0, r, checkparams, check_left_cl)
    mean = lbinsearch(mean, r, checkparams, check_left_cl_equal) - 1 
    return(mean) 

def searchindexzn(l,r, checkparams):
    def check_left_zn(index, params):
        array,x = params 
        return array[index][1] < x[1]
    mean = lbinsearch(l,r, checkparams, check_left_zn)
    return(mean)

x = []
for i in range(int(input())):
    ti,yi = input().split()
    x.append((float(ti), float(yi)))
    
zn = sorted(x ,key = lambda y: (y[1],y[0]), reverse = True)    
cl = sorted(x ,key = lambda y: (y[0],y[1]), reverse = True)    
pair = 0
s = 0
for i in range(len(zn)):                                #идем по значениям 
    index_cl = searchindexcl(len(zn), (cl,zn[i]))       #нужен для нахождения начала мультимножества подходящих пар
    index_zn = searchindexzn(i, len(zn), (zn,zn[i]))    #нужен для нахождения конца мультимножества одинаковых значений
    zn_set_equal = Counter(zn[i + 1:index_zn])
    zn_set = Counter(zn[i:]) 
    cl_set = Counter(cl[index_cl + 1:])                 # + 1 так как приплюсовывать мы начинаем со следующего
    items = sum((zn_set & cl_set).values())          
    items_equal = sum((zn_set_equal & cl_set).values()) #sum(cl_set.values())
    pair += len(zn) - index_cl - 1
    s += items - 0.5 * items_equal

print('{:.6f}'.format(s/pair))