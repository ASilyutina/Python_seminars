# 22. Задайте список из нескольких чисел. 
#Напишите программу, которая найдет сумму элементов списка, стоящих на нечетной позиции.

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = 5
frst = 1
last = 20

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))

 #если самостоятельно вводить
def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)