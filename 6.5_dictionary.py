# 65. 4.Английский словарь - "Пора учить английский язык", - сказал себе Степа и решил написать программу 
#     для изучения английского языка. 
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке. 
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. 
#   В этой задаче нужно использовать строчный метод split().  



count = int(input())
vocabulary = {}
for i in range(count):
    words = input()
    temp_list = words.split(' - ')
    vocabulary[temp_list[0]] = temp_list[1].split(', ')
print(vocabulary)

# eng_word = input('Введите слово для перевода: ')
# if vocabulary.get(eng_word):
#     print (', '.join(vocabulary.get(eng_word))
# else:
#     print'такого слова нет в словаре')
# print(vocabulary.get(eng_word, 'такого слова нет в словаре'))

