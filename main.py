questionery = 'Здравствуйте, вы проходите анкету'
print(questionery)
name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
date_birth = input('Введите ваш год рождения: ')
course = input('Нравится ли вам курс? ')
question = input('Что вы ожидаете в дальнейших занятиях? ')
full_name = name + ' ' + surname
age = 2023 - int(date_birth)
print("Введите ваше ФИО:", full_name)
print("Ваш возраст:", age)
print("Нравится ли вам курс?", course)
print("Что вы ожидаете в дальнейших занятиях?", question)


