"""
Урок 6. Работа с файлами
"""
# Читаем текстовые файлы

# file_1 = open('hello.txt', 'r')
# content = file_1.read()
# print(content)
# file_1.close()
# print(file_1.read())

# file_2 = open('hello.txt', 'r', encoding='utf-8')
# print(file_2.readline())
# print(file_2.readline())
# print(file_2.readline())
# print(file_2.readline())
# file_2.close()

# file_3 = open('hello.txt', 'r', encoding='utf-8')
# for line in file_3:  # \n
#     print(line.strip())
# file_3.close()

# file_4 = open('hello.txt', 'r', encoding='utf-8')
# print(file_4.readlines())
# file_4.close()

# Менеджер контекста и запись файла
# with open('qwerty.txt', 'w+', encoding='utf-8') as fw:
#     print('Я оказывается могу писать в файл!!!', file=fw)
#     fw.write('qwe\nqwe\nqwe\n')
#     fw.writelines(['1 строка\n', '2 строка\n'])
#
# with open('qwerty_2.txt', 'a+', encoding='utf-8') as fw:
#     from datetime import datetime
#
#     current_time = datetime.now()
#     fw.write(f'{current_time}\n')
#     fw.write(f'{current_time}\n')

# Поэксперементируем - содадим summator
# формируем тестовые данные для разбора
import random

tasks = [f"{random.randrange(1, 10)} {random.randrange(1, 10)}\n" for _ in range(10)]

# with open('trash/tasks_summator.txt', 'w', encoding='utf-8') as fw:
#     fw.writelines(tasks)


def send_sum(value_1: int, value_2: int) -> int:
    """Простейшая функция суммирования двух значений"""
    return value_1 + value_2


# result_1 = 0
# with open('trash/tasks_summator.txt') as fr:
#     for row in fr.readlines():
#         v1, v2 = row.split(' ')
#         result_1 += send_sum(*map(int, [v1, v2]))
# print(f'1 - Результат рассчитанной суммы: {result_1}')
#
# result_2 = 0
# with open('trash/tasks_summator.txt') as fr:
#     for row in fr:
#         v1, v2 = row.split(' ')
#         result_2 += send_sum(*map(int, [v1, v2]))
# print(f'2 - Результат рассчитанной суммы: {result_2}')
#
# result_3 = 0
# with open('trash/tasks_summator.txt') as fr:
#     while True:
#         row = fr.readline()
#         if not row:
#             break
#         v1, v2 = row.split(' ')
#         result_3 += send_sum(*map(int, [v1, v2]))
# print(f'3 - Результат рассчитанной суммы: {result_3}')

# json
import json

my_dataset: list = [
    {'name': 'Тимур', 'level': 50},
    {'name': 'Светлана', 'level': 51},
    {'name': 'Анатолий', 'level': 5}
]

# with open('trash/tasks_json_2.json', 'w', encoding='utf-8') as fw:
#     # json.dump(my_dataset, fw, ensure_ascii=False, indent=2)
#     data_str = json.dumps(my_dataset, ensure_ascii=False, indent=4)
#     fw.write(data_str)

# with open('trash/tasks_json_2.json', 'r', encoding='utf-8') as fr:
#     # import_dataset = json.load(fr)
#     text = fr.read()
#     import_dataset = json.loads(text)
#     print(type(import_dataset), import_dataset)


# pickle
import pickle

data: dict = {
    1: [random.randrange(1, 10) for _ in range(5)],
    2: ('Я какая-то строка', b'binary data'),
    3: {None, True, False}
}
# with open('trash/data.pickle', 'wb') as fw:
#     #     pickle.dump(data, fw)
#     data_binary = pickle.dumps(data)
#     fw.write(data_binary)
#
# with open('trash/data.pickle', 'rb') as fr:
#     # data_new = pickle.load(fr, encoding='utf-8')
#     text = fr.read()
#     import_dict = pickle.loads(text)
#     print(type(import_dict), import_dict)


# профилируем создание файла в байтах и текстового - проверяем размер
from time import perf_counter

nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]

# start = perf_counter()
# with open('trash/random_million.json', 'w', encoding='utf-8') as fw:
#     json.dump(nums, fw)
# print(f'json saved: {perf_counter() - start}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'wb') as fw:
#     pickle.dump(nums, fw)
# print(f'pickle saved: {perf_counter() - start}')

print('\n\n')

# профилируем считываение файла в байтах и текстового
# start = perf_counter()
# with open('trash/random_million.json', 'r', encoding='utf-8') as fr:
#     nums_json = json.load(fr)
# print(f'json loaded: {perf_counter() - start} - {type(nums_json)}, {len(nums_json)}')
#
# start = perf_counter()
# with open('trash/random_million.pickle', 'rb') as fr:
#     nums_pickle = pickle.load(fr)
# print(f'pickle loaded: {perf_counter() - start} - {type(nums_pickle)}, {len(nums_pickle)}')


print('\n\n')

# Чтение файлов чанками
# chunk_size = 256
# with open('trash/random_million.json', 'r') as fr:
#     str_data: list = []
#     while True:
#         chunk = fr.read(chunk_size)
#         if not chunk:
#             break
#         str_data.append(chunk)
#     nums_j = json.loads(''.join(str_data))
# print(f'{type(nums_j)}, {len(nums_j)}')
#
# with open('trash/random_million.pickle', 'rb') as fr:
#     binary_data = bytearray()
#     while True:
#         chunk = fr.read(chunk_size)
#         if not chunk:
#             break
#         binary_data.extend(chunk)
#     nums_p = pickle.loads(binary_data)
# print(f'{type(nums_p)}, {len(nums_p)}')

# encode и decode
# hello_text = 'Привет мир input'
# txt_binary = hello_text.encode(encoding='utf-8')
# txt_origin = txt_binary.decode(encoding='utf-8')
# print(type(txt_binary), txt_binary)
# print(type(txt_origin), txt_origin)


n = 123.45
print(str(n).ljust(10, ' '))
print(str(n).rjust(10, ' '))

# seek(), tell()
# +r

print('end')
