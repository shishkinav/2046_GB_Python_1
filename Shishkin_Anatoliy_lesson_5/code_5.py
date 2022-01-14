"""
Урок 5. Генераторы и comprehensions. Множества
"""
import sys

# миллион элементов в списке создадим
# nums = list()
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append((num ** 2))
# print(type(nums), sys.getsizeof(nums))
#
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(type(nums_gen), sys.getsizeof(nums_gen))

# профилируем чтобы понять не в цщерб ли используем генератор
from time import perf_counter

# start = perf_counter()
# nums_sum = sum(nums)
# print(nums_sum, perf_counter() - start)
#
# start = perf_counter()
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)


print('\n\n')

# в чём разница?

# start = perf_counter()
# nums = list()
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append((num ** 2))
# nums_sum = sum(nums)
# print(nums_sum, perf_counter() - start)
#
# start = perf_counter()
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)

# nums_2 = []
# for num in range(1, 10 ** 6 + 1, 2):
#     nums_2.append((num ** 2))
#
# nums_gen_2 = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))

# print(nums_2[:5])
# print(next(nums_gen_2), next(nums_gen_2), next(nums_gen_2), next(nums_gen_2), next(nums_gen_2), sep=', ')

from itertools import islice

# print(*islice(nums_gen_2, 5))

# nums_gen_3 = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(sum(nums_gen_3))  # 166666666666500000
# print(sum(nums_gen_3))  # будет 0

# а что же такое yield и как его использовать?
# def letter_generator(start: str, end: str):
#     for code in range(ord(start), ord(end) + 1):
#         # print('start func generator')
#         yield chr(code)
#         # print('end func generator')
#
#
# eng_letters = letter_generator('A', 'Z')
# print(*eng_letters, sep='')

import string

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)


# Nested List Comprehensions
# lc_list = [num ** 2 for num in range(1, 10 ** 6 + 1, 2)]
# gen_exp = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(type(lc_list), sys.getsizeof(lc_list))
# print(type(gen_exp), sys.getsizeof(gen_exp))

matrix_1 = [
    [1, 1, 1],
    [2, 2, 2]
]
matrix_2 = [
    [4, 4, 4],
    [5, 5, 5]
]

matrix_sum = []
for i in range(len(matrix_1)):
    _ = list()
    for j in range(len(matrix_1[0])):
        _.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_sum.append(_)

# мы победили, спасибо Андрею Калабину, навёл на мой косяк )))

# matrix_sum = [
#     [matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))
# ]



from pprint import pprint

pprint(matrix_sum)

# Dict Comprehensions
eng_ru_nums = {'one': 'один', 'two': 'два', 'tree': 'дерево'}
ru_eng_nums = {value: key for key, value in eng_ru_nums.items()}
print(eng_ru_nums, '\n', ru_eng_nums)

"""
ll_if_list = [num for num in range(11) if num % 2 == 0]
ll_if_list
[0, 2, 4, 6, 8, 10]
"""

# Множество в Python (Хэш-таблицы)
box = ['pen', 'pencil', 'cat', 'dog', 'cat', 'paper', 'pen', 'money']
start = perf_counter()
unique_box = [el for el in box if box.count(el) == 1]
print(unique_box, perf_counter() - start)

# уникальность подбирается по разово встречающимся объектам
start = perf_counter()
unique_box_2 = set()
tmp = set()
for el in box:
    if el not in tmp:
        unique_box_2.add(el)
    else:
        unique_box_2.discard(el)
    tmp.add(el)

print(unique_box_2, perf_counter() - start)

# сохранение последовательности элементов уникальных для коробки
unique_set = [el for el in box if el in unique_box_2]
print(unique_set)

# ещё методы множества
chat_1 = {'user_1', 'user_5', 'user_7', 'user_8', 'user_11'}
chat_2 = {'user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'}

# пересечения по множествам
chat_common = chat_1.intersection(chat_2)
print(chat_common)
print(chat_1 & chat_2)  # {'user_1', 'user_7'}

# только пользователей конкретного чата
chat_1_only = chat_1 - chat_2
chat_2_only = chat_2 - chat_1
print(chat_1_only, chat_2_only)
print(chat_1.difference(chat_2), chat_2.difference(chat_1))
# {'user_5', 'user_8', 'user_11'} {'user_10', 'user_9', 'user_2'}

# объединение пользователей двух множеств
both_chats = chat_1.union(chat_2)
print(both_chats)
print(chat_1 | chat_2)  # {'user_9', 'user_5', 'user_10', 'user_8', 'user_1', 'user_11', 'user_2', 'user_7'}

# print(chat_1 + chat_2)  # не позволяет складывать

# Снова множества - frozetset
chat_1 = frozenset(('user_1', 'user_5', 'user_7', 'user_8', 'user_11'))
chat_2 = frozenset(('user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'))
chat_3 = frozenset(['user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'])
print(chat_3)
chat_common = chat_1.intersection(chat_2)
print(chat_common)
# chat_1.add('user_101') - нельзя сделать, т.к. неизменяемый

# Set Comprehensions
from random import randint

random_nums = {randint(1, 100) for _ in range(50)}
print(len(random_nums), random_nums)

print('end')
