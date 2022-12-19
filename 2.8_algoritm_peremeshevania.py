#18. Реализуйте алгоритм перемешивания списка.

import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 5
lft = -50
rght = 50

mylist = get_list(n, lft, rght)
print("Начальный список: " + str(mylist))
shuffle_list(mylist)
print("Перемешанный список: " +  str(mylist))

