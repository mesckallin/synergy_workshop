# https://github.com/mesckallin/synergy_workshop/blob/main/lesson_4/task_2.py

num = int(input('Ведите 5-значное число: '))

tens = num // 10 % 10
units = num % 10
hundreds = num // 100 % 10
thousands = num // 1000 % 10
tens_thousands = num //10000

print(tens ** units * hundreds / (tens_thousands - thousands))
