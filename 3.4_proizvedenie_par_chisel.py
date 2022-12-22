# 34. (23) Напишите программу, которая найдет произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний.

# from random import randint
# import math

# def get_numbers(n, frst, last):
#     return [randint(frst, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 5
# frst = 1
# last = 10

# mylist = get_numbers(n, frst, last)
# print(mylist)
# print(mult_pairs(mylist))

#второй способ


from random import randint
import math

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]


def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

n = 5
frst = 1
last = 10    

mylist = get_numbers(n, frst, last)
print(mylist)
print(pairs_mult(mylist))