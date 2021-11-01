# Задание 1

n = int(input('Введите верхний предел генерации: '))
def nums_generator(n):
   for num in range(1, n + 1, 2):
       yield num
num_generator = nums_generator(n)
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))


# Задание 2
n = int(input('Введите верхний предел генерации: '))
num_gen = (num for num in range (1, n + 1, 2))

print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))


# Задание №4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(1, len(src)):
    for j in src:
        if src[i] > src[i-1]:
            result.append(src[i])
            break
print(result)

# Задание 5
from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
preresult = set()
buf = set()
result = []

start = perf_counter()

def is_not_repeated():
    for i in src:
        if i not in buf:
            preresult.add(i)
        else:
            preresult.discard(i)
        buf.add(i)

    for i in src:
        if i in preresult:
            result.append(i)
    return result

print(is_not_repeated(), perf_counter() - start)
