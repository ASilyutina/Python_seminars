# 11. Напишите программу которая принимает на вход число N,
#и выдает последовательность из N членов
n=int(input())
for i in range(n-1):
    print((-3)**i, end=', ')
print((-3)**(i+1))

n=int(input())
out_list=[]
for i in range(n):
    out_list.append((-3)**i)
print(*out_list, sep=', ')

#12Для натурального n создать словарь индекс-значений состоящий из элементов последовательности 3n+1

n=int(input())
out_dict={}
for i in range(1, n+1):
    out_dict[i]=3*i+1
print(out_dict)



#13Напишите программу в которой пользователь будет задавать две строки, а программа определять 
# колличество вхождений одной строки в другой.

str1=input()
str2=input()
print(str1.count(str2) or str2.count(str1))