
"""Задача 1"""
# number1 = int(input())
# number2 = int(input())
# if number1 ** 2 == number2 or number2 ** 2 == number1:
#     print('да')
# else:
#     print('нет')
"""Задача 2"""
# some_list = []
# for _ in range(5):  # 0, 1, 2, 3
#     x = int(input())
#     some_list.append(x)
# maxx = some_list[0]
# for el in some_list:
#     if el > maxx:
#         maxx = el
# print(maxx)
#
#
# maxx = int(input())
# for _ in range(4):  # 0, 1, 2, 3
#     x = int(input())
#     if x > maxx:
#         maxx = x
# print(maxx)

# print(max(some_list))

# maxx = some_list[0]
# for el in some_list:  # 6, 7, 0, -1, 4
#     if el > maxx:
#         maxx = el
# print(maxx)

# maxx = some_list[0]
# for ind in range(5):
#     if some_list[ind] > maxx:
#         maxx = some_list[ind]
# print(maxx)
"""Параметры sep, end"""
# print(7, end=', ')
# print(8)
# print(7, 8, 9, sep=', ')
# some_list = [1, 2, 3, 4]
# print(*some_list, sep='*')
"""Задача 3"""
# N = int(input())
# for i in range(-N, N):
#     print(i, end=', ')
# print(N)

# N = int(input())
# print(*range(-N, N + 1), sep=', ')

# N = int(input())
# some_list = []
# for i in range(-N, N + 1):
#     some_list.append(i)
# print(*some_list, sep=', ')
"""Задача 4"""
# a = float(input())
# if a % 1 == 0:
#     print('нет')
# else:
#     print(int(a * 10) % 10)

# a = input()
# if '.' in a:
#     ind = a.index('.')
#     print(a[ind + 1])
# else:
#     print('нет')

# '''Задача 5'''
# a = int(input())
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('да')
# else:
#     print('нет')
# #
# # print((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0)
#
# text = 'съешь ещё этих мягких французских булок'
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл