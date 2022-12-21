import numpy as np

n1, m1 = map(int, input().split())
mask = np.array([[x for x in range(1, m1 + 1)] for i in range(n1)])
archive = []
for i in range(n1):
    str = input()
    archive.append(str)

array = np.array([[ord(archive[i][x]) for x in range(m1)] for i in range(n1)])
array_mult = np.multiply(array, mask)
hash_sum_original = np.sum(array_mult, axis = 1)


n2, m2 = map(int, input().split())
fl = True
archive = []
for i in range(n2):
    str = input()
    archive.append(str)

if n1 == n2 and m1 == m2 or n1 == m2 and m1 == n2:
    array = np.array([[ord(archive[i][x]) for x in range(m1)] for i in range(n1)])
    #1 перемножение с обычной маской
    # mask
    if (n1 == n2 and m1 == m2 and fl):
        hash_sum_default = np.sum(np.multiply(array, mask), axis = 1)
        if np.array_equal(hash_sum_default, hash_sum_original):
            fl = False

    #2 перемножение с транспонированной (поворот вправо)
    # mask.T
    if (n1 == m2 and m1 == n2 and fl):
        hash_sum_right = np.sum(np.multiply(array, mask.T), axis = 1)
        if np.array_equal(hash_sum_right, hash_sum_original):
            fl = False

    #3 перемножение с _________________ (поворот влево)
    if (n1 == m2 and m1 == n2 and fl):
        mask = np.array([[x for x in range(m1, 0, -1)] for i in range(n1)])
        hash_sum_left = np.sum(np.multiply(array, mask.T), axis = 1)
        if np.array_equal(hash_sum_left, hash_sum_original):
            fl = False

    #4 перемножение с перевернутой
    if (n1 == n2 and m1 == m2 and fl):
        mask = np.array([[x for x in range(m1, 0, -1)] for i in range(n1)])
        hash_sum_reverse = np.sum(np.multiply(array, mask), axis = 1)
        if np.array_equal(hash_sum_reverse[::-1], hash_sum_original):
            fl = False

if fl: print('No')
else: print('Yes')