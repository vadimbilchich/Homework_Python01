# Задача 1:
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week = int(input('Введите число дня недели(от 1 до 7 включительно): '))
if day_week == 6 or day_week == 7:
    print(f'День недели {day_week} -> выходной')
elif 1 <= day_week <= 5:
    print(f'День недели {day_week} будни')
else:
    print('Введено неверное число')