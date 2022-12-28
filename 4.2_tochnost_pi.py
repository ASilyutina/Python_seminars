#42. (30) Вычислить число  п с заданной точностью d

import math
x=math.pi
n=input('Введите число d  чтобы задать точность вывода числа пи (0.01, 0.001)')
count=0

n=n.replace('0.', '')

for i in n:
    count+=1

print(f'число {x:.{count}f}')    