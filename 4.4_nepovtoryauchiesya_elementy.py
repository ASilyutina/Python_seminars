# 44. (32) Задайте последовательность чисел. 
# Напишите программу которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def create_list(size, m, n):
    return[randint(m,n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 100

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))