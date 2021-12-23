# YandexContest

Генератор точек в круге


Задание 3 (по моим номерам файлов, в последнем решение, предыдущие - ход моих мыслей)
Петя написал два генератора точек в круге:
def generate1():  
    a = uniform(0, 1)  
    b = uniform(0, 1)  
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))
def generate2():  
    while True:  
        x = uniform(-1, 1)  
        y = uniform(-1, 1)  
        if x ** 2 + y ** 2 > 1:  
            continue  
        return (x, y)
Даны 100 наборов по 1000 точек, каждый набор сгенерирован каким-то одним из этих двух алгоритмов. Необходимо определить для каждого набора, первый или второй алгоритм использовался для его генерации.
Для того, чтобы получить ОК по этой задаче, надо предсказать правильный генератор хотя бы для 98 наборов.

Формат ввода
Даны 100 строк. Каждая строка отвечает за свой набор точек.
В каждой строке находится 2000 действительных чисел разделённых пробелом. Точки идут подряд, то есть формат строки: 
x0 y0 x1 y1 … x999 y999
Формат вывода
Нужно вывести 100 строк, в каждой из которой должно быть 1 число: 1 или 2, в зависимости от того, первым или вторым генератором был сгенерирован данный набор точек.
