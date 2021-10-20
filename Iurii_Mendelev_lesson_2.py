#Задание 1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
# Задание 2
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list1 = []
for i in my_list:
    for j in i[::-1]:
        if j.isdigit() == 0:
            my_list1.append(i)
            break
        elif j.isdigit() == 1:
            my_list1.append('"')
            my_list1.append('{:02d}'.format(int(i)))
            my_list1.append('"')
            break

print(my_list1)
my_string = ' '.join(my_list1)
print(my_string)

# Задание 4
jobs_and_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
for i in jobs_and_names:
    names.append(i.split(' ')[-1])
for i in names:
    print('Привет, {}!'.format(i.title()))

# Задание 5
prices = [11, 33.3, 25.83, 71.5, 48.45, 66.6, 99.99, 648.22, 65.25, 76.21, 45.4]
for i in prices:
    print('{:.2f}'.format(i), end = ', ')
print(id(prices))
prices.sort()
print(prices, id(prices))
prices_decrease = []
for i in prices[::-1]:
    prices_decrease.append(i)
print(prices_decrease)
prices = [11, 33.3, 25.83, 71.5, 48.45, 66.6, 99.99, 648.22, 65.25, 76.21, 45.4]
print('Цены пяти самых дорогих товаров по возрастанию с минимумом кода {}'.format(sorted(prices)[-5:]))