# https://github.com/mesckallin/synergy_workshop/blob/main/input_print/task_1.py

#  Задание №1
#  Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
#  Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца,
#  его возраст и кличку, а потом выведет все эти данные в одно предложение.
#  Например: Это желторотый питон по кличке "Каа". Возраст: 34 года.


# Водд данных пользователем и присвоение значения переменной
animal_type = input('Введите вид Вашего домашнего питомца: ')
nickname = '"' + input('Введите кличку Вашего питомца: ') + '"'
age = input('Введите возраст питомца: ')

# Вывод с пустым разделителем
print('Это ', animal_type, ' по кличке ', nickname, '. ', 'Возраст: ', age, ' года.', sep='')
