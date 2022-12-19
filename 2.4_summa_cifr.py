#2.4 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from random import uniform

n = round(uniform(1, 100), 2)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print(sum_digit(n))