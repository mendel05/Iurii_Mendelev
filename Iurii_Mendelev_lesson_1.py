# Задание 1
duration = int(input('Введите количество секунд: '))
if duration <= 59:
    print(duration, 'сек')
elif 60 <= duration <= 3599:
    print(duration//60, 'мин', duration%60, 'сек')
elif 3600 <= duration <= 86399:
    print (duration//3600, 'ч', (duration - (duration//3600)*3600)//60, 'мин', (duration - (duration//3600)*3600)%60, 'сек')

# Задание 2
coub_list = []
for i in range(1, 1001, 2):
    coub_list.append(i ** 3)
print(coub_list)
#дальше не получается

# Задание 3
percent1 = 'процент'
percent2 = 'процента'
percent3 = 'процентов'
digit = range(1, 101)
for i in digit:
    if i %10 == 1 and i!= 11:
        print (i, percent1)
    elif i%10 == 2 or i%10 == 3 or i%10 == 4 and i != 12 and i != 13 and i != 14: #не пойму в чем ошибка в числах 12 и 13
        print (i, percent2)
    else:
        print (i, percent3)