#61. Создайте список из случайных чисел. Найдите количество различных элементов в нем.

array = input("Введите список через пробел").split()
count = 0
unique_array = []
for x in array:
    if x not in unique_array:
        count += 1
        unique_array.append(x)
print(len(unique_array))

