# 63. 3.Еще немного о друзьях -Пользователь вводит число N.
#  Затем он вводит личные данные (имя и возраст)своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.


n = int(input("Введите количество друзей: "))
friends = []
new_friend = {}
for element in range(0, n): # проходим по колисчетсву друзей
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    new_friend["name"] = name
    new_friend["age"] = age
    friends.append(new_friend)
    new_friend = {}

print("Список Ваших друзей: ", friends)

min_age = friends[0]['age']
for element in friends:
    if element['age'] < min_age:
        min_age = element['age']
for element in friends:
    if element['age'] == min_age:
        print(element['name'])