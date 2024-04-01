# https://github.com/mesckallin/synergy_workshop/blob/main/input_print/task_2.py

# Задание №2
# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов.
# Он должен запрашивать по порядку этапы развития человека
# и в конце вывести все стадии, разделенные знаком =>,
# что будет означать постепенный переход от одного к другому.

print('Введите правильную последовательность 4 этапов развития человека, выбрав из вариантов: homo sapiens, australopithecus, homo erectus, dryopithecus.')

stage_1 = input('Этап 1: ')
stage_2 = input('Этап 2: ')
stage_3 = input('Этап 3: ')
stage_4 = input('Этап 4: ')

print(stage_1, stage_2, stage_3, stage_4, sep='=>')
