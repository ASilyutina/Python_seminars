
# эта функция отображает все содержимое телефонной книги pb
def display_all(pb):
    if not pb:
# если функция отображения вызывается после удаления всех контактов, то len будет 0
# А без этого условия выдаст ошибку
        print("Список пуст: ")
    else:
        for i in range(len(pb)):
            print(pb[i])