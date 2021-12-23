# YandexContest

Генератор точек в круге


Задание 3 
(3-ий по моим номерам файлов, в последнем решение, предыдущие - ход моих мыслей или прототипов)


Условие

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
x0 y0 x1 y1 … x999 y999.

Формат вывода

Нужно вывести 100 строк, в каждой из которой должно быть 1 число: 1 или 2, в зависимости от того, первым или вторым генератором был сгенерирован данный набор точек.



Задание 2

Условие

Вася взял игральную кость и написал на гранях числа 
Для генерации случайного числа Вася решил воспользоваться следующим алгоритмом:
Выбрать число k.
Подбросить кубик k раз и записать на листик последовательно выпавших чисел b(j).
Пройтись по списку с конца и вычеркнуть число b(j), если оно равно b(j−1) (b(1) всегда останется в последовательности).
Определите математическое ожидание суммы оставшихся в последовательности чисел, если Вася сообщит вам числа a(i) и k.
Обратите внимание, что кубик у Васи честный и все выпадение любой из граней равновероятно. Кроме этого, подбрасывания кубика независимы.

Формат ввода

В первой строке записаны 6 целых чисел
Во второй строке записано одно число k

Формат вывода

Выведите одно вещественное число — требуемое по условию задачи математическое ожидание.
Ответ будет считаться верным, если относительная или абсолютная погрешность не будет превышать 10^(−6).

