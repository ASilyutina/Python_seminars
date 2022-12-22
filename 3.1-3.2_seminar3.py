#(20)задайте список. напишите программу которая определит присутствует ли в заданном списке сторк некое число

a = input().split()
number = input()
for i in a:
  if number in i:
    print('yes')
    break
else:
  print('no')


#(21) Напишите программу которая определит позицию второго вхождения строки в списке, либо сообщит, что ее нет


a = input().split()
find_str = input()
count = 0
for i in range(len(a)):
  if a[i] == find_str:
    count += 1
    if count == 2:
      print(i)
      break
else:
  print(-1)


#задача с начала урока

a = float(input())
if a % 1 == 0:
  s = 0
  while a > 0:
    s += a % 10
    a //= 10
  print(s)
else:
  while int(a) != 0:
    a /= 10
  a = a - int(a)
  print(a)