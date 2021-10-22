# Задание 1
my_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

key = input('Введите число от 0 до 10 на английском языке: ')

def num_translate(key):
    return my_dict.get(key)
print(num_translate(key))

# Задание 3
name = input('Введите имена сотрудников: ')
name1 = name.split(' ')
def thesaurus(name1):
    names = {}
    for i in name1:
        names.setdefault(i[0], []).append(i)
    return names
print (thesaurus(name1))

# Задание 5
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input('Введите количество шуток: '))
jokes = []


def get_jokes(n):
    '''

    :param n: number of jokes
    :return: the list of jokes combined from nouns, adverbs and adjectives
    '''
    while n > 0:
        jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
        n -= 1
    return jokes


print(get_jokes(n))

