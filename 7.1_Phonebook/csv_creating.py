def creating ():
    file = 'phone.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия; Имя; Отчество; Дата рождения; Номер контакта ; Категория\n')