"""
Урок 3. Функции. Словари
"""
# Функции в Python
def summ_two_value(a, b):
    """Пример простейшей функции"""
    c = a + b
    return c


# print(summ_two_value(1, 5))

func = summ_two_value
# print(func(2, 3))

text_example_1 = 'Опыт выполнения домашних заданий предыдущих уроков наверняка подсказывает вам, ' \
                 'что нужен какой-то способ для повторного использования уже написанного кода.'
text_example_2 = 'Один из способов был изобретен очень давно — обособление фрагментов кода в функции. ' \
                 'Мы уже говорили о них.'

from Shishkin_Anatoliy_lesson_3.utils.string_transform import clear_punctuation, lower_and_split


for own_text in (text_example_1, text_example_2):
    new_text = clear_punctuation(own_text)
    print(lower_and_split(new_text))


# Возвращаем callback
# упрощённый пример
nums = ['1578.4', '892.4', '354.1', '871.5']
value = 0
for num in nums:
    value += float(num)
print(value)

# решение усложнённое
print(sum(map(float, nums)))


# Доведём до абсурда
"""
for own_text in (text_example_1, text_example_2):
    new_text = clear_punctuation(own_text)
    print(lower_and_split(new_text))
"""
print(
    *tuple(
        map(
            lower_and_split,
            list(
                map(
                    clear_punctuation,
                    (text_example_1, text_example_2)
                )
            )
        )
    ), sep='\n'
)

# Области видимости переменных
# def say_hello_wrapper():
#     # name = 'Петр'
#
#     def say_hello():
#         name = 'Петр'
#         print(name)
#
#     say_hello()
#
#
# name = 'Иван'
# print(say_hello_wrapper())

# запрещённый проброс переменной из локальной области в глобальную
# def say_hello():
#     global name
#     name = 'Петр'
#     print(name)
#
# print('\n\n')
# name = 'Иван'
# print(name)  # Иван
# say_hello()  # Петр
# print(name)

# пример использования nonlocal
def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer


v = counter()
print(v())
print(v())
print(v())


# ещё пример использования nonlocal
def wrapper():
    name = 'Анатолий'

    def say_hello():
        nonlocal name
        name = name[:-1]
        return name

    return say_hello


name = 'Иван'
callback = wrapper()
print(callback())
print(callback())
print(callback())
print(callback())


# Словари Python (Ассоциативные массивы)
pers_1 = ['pikachu', 87.9, 103]
pers_2 = ['smurfik', 10.0, 66]


def get_info(data: list):
    print(f'Никнейм - {data[0]}, health - {data[1]}, level - {data[2]}')


get_info(pers_1)
get_info(pers_2)
print()

# определение словаря
temp_dict_1 = {}
temp_dict_2 = dict()


# upgrade pers
pers_1_adv = {
    "nickname": 'pikachu',
    "health": 87.9,
    "level": 103
}
pers_2_adv = {
    "nickname": 'smurfik',
    "health": 10.0,
    "level": 66
}


def get_info(dataset: dict) -> None:
    print(f'Никнейм - {dataset["nickname"]}, health - {dataset["health"]}, level - {dataset["level"]}')


get_info(pers_1_adv)
get_info(pers_2_adv)
print()

# Словари: .get() и .setdefault()
"""
pers_1_adv.get('nickname')
'pikachu'
pers_1_adv.get('nick')
pers_1_adv.get('nick', 'Анатолий')
'Анатолий'
pers_1_adv.get('nickname', 'Анатолий')
'pikachu'
pers_1_adv['nick']
Traceback (most recent call last):
  File "/home/avshishkin/.pyenv/versions/3.9.0/lib/python3.9/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
KeyError: 'nick'

pers_1_adv.setdefault('nickname', 'Анатолий')
'pikachu'
pers_1_adv
{'nickname': 'pikachu', 'health': 87.9, 'level': 103}
pers_1_adv.setdefault('nick', 'Анатолий')
'Анатолий'
pers_1_adv
{'nickname': 'pikachu', 'health': 87.9, 'level': 103, 'nick': 'Анатолий'}
"""

# Словари: .update() и .popitem()
"""
pers_1_adv.setdefault('nickname', 'Анатолий')
'pikachu'
pers_1_adv
{'nickname': 'pikachu', 'health': 87.9, 'level': 103}
pers_1_adv.setdefault('nick', 'Анатолий')
'Анатолий'
pers_1_adv
{'nickname': 'pikachu', 'health': 87.9, 'level': 103, 'nick': 'Анатолий'}
pers_1_adv.update({'nickname': 'Иван', 'weght': 97.9})
pers_1_adv
{'nickname': 'Иван', 'health': 87.9, 'level': 103, 'nick': 'Анатолий', 'weght': 97.9}
pers_1_adv.popitem()
('weght', 97.9)
pers_1_adv
{'nickname': 'Иван', 'health': 87.9, 'level': 103, 'nick': 'Анатолий'}
pers_1_adv.pop("weght")
pers_1_adv.pop("level")
103
pers_1_adv
{'nickname': 'Иван', 'health': 87.9, 'nick': 'Анатолий'}
"""

dataset = {
    'mail.ru': '94.100.180.201',
    'geekbrains.ru': '178.248.232.209',
    'amazon.com': '205.251.242.103'
}

for key in dataset:
    print(key)

print()

for key in dataset.keys():
    print(key)

print()

for key, value in dataset.items():
    print('{}={}'.format(key, value))

print()

for v in dataset.values():
    print(v)


# Позиционные аргументы и *args
from Shishkin_Anatoliy_lesson_3.utils.tools import own_sum, own_sum_upgrade

# разбираем распаковку
a = 5
b = 10
a, b = b, a

print(f'own_sum([1, 5, 89]) = {own_sum([1, 5, 89, 5])}')
# print(own_sum(1, 5, 89))  # ОШИБКА
print(f'own_sum_upgrade(1, 5, 89) = {own_sum_upgrade(1, 5, 89, 5)}')  # НЕТ ОШИБКИ - WHY?
print(own_sum([1, 5, 89]) == own_sum_upgrade(1, 5, 89))


own_list = [1, 5, 89]
print(f'own_sum_upgrade(*[1, 5, 89]) = {own_sum_upgrade(*[1, 5, 89])}')
print(f'own_sum_upgrade(*own_list) = {own_sum_upgrade(*own_list)}')
print()


# Модуль random
from random import randrange, randint, choice

numbers = [value * 11 for value in range(1, 11)]
print(f'numbers = {numbers}')
print()
idx = randrange(len(numbers))  # как пользоваться randrange
print(f'idx = {idx}')
print(f'numbers[{idx}] = {numbers[idx]}')
print()
new_idx = randint(0, len(numbers) - 1)  # как пользоваться randint
print(f'new_idx = {new_idx}')
print(f'numbers[{new_idx}] = {numbers[new_idx]}')
print()
print(f'Случайное значение из списка {numbers} получили {choice(numbers)}')
print()
# choices, sample и shuffle - разбираем самостоятельно в методичке есть ссылки



# Необязательные аргументы, именованные аргументы - **kwargs

def my_game(count_game: int) -> None:
    """Играем на стандартном кубике"""
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(1, 6)}')


my_game(2)
print()


def my_game(count_game: int, luck: float = 0.00) -> None:
    """Играем на стандартном кубике с удачей"""
    if luck > 100:
        luck = 100.00
    end_number = 6
    start_number = 1 + int(((end_number - 1) * luck) / 100)
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
# print()
# my_game(2, 100.00)
print()


def my_game(count_game: int, *args, luck: float = 0.00, **kwargs) -> None:
    """Играем на кубике"""
    # print(f'kwargs: {kwargs}')
    if luck > 100:
        luck = 100.00
    # end_number = 6
    end_number = kwargs.get('count_edge', 6)
    start_number = 1 + int((end_number - 1) * luck / 100)
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
print()
my_game(2, luck=50)
# print()
# my_game(2, luck=50, count_edge=12)
print()


# filter(), map(), zip() и lambda-функции
new_numbers = [value * 11 for value in range(20)]
print(f'new_numbers = {new_numbers}')
print()


def my_filter(element) -> bool:
    """Наша функция для фильтрации"""
    return element % 10 == 5


own_filter_result = filter(my_filter, new_numbers)
print(type(own_filter_result))
print('result =', *own_filter_result)
print('result =', *own_filter_result)  # а здесь уже ничего НЕ УВИДИМ кроме 'result ='
print()

own_filter_result = filter(lambda obj: obj % 10 == 5, new_numbers)
print('lambda filter result =', *own_filter_result)
print()

map_result = map(lambda obj: obj // 10, new_numbers)
print('map_result =', list(map_result))
print()

user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
user_logins = ['ivan', 'petr', 'olga', 'sergey', 'Anatoliy']
user_roles = ['user', 'staff', 'admin']
zip_result = zip(user_names, user_logins, user_roles)
print('zip_result =', tuple(zip_result))
print()


print('end')
