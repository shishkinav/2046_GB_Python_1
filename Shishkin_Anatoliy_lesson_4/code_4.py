"""
Урок 4. Работа с модулями и пакетами
"""
from num2words import num2words


print(num2words(42))                                # forty-two
print(num2words(42, to='ordinal'))                  # forty-second
print(num2words(42, to='ordinal_num'))              # 42nd
print(num2words(42, to='year'))                     # forty-two
print(num2words(12.42, to='currency'))              # twelve euro, forty-two cents
print()
print(num2words(42, lang='ru'))                     # сорок два
print(num2words(42, to='ordinal', lang='ru'))       # сорок второй
print(num2words(42, to='ordinal_num', lang='ru'))   # 42
print(num2words(42, to='year', lang='ru'))          # сорок два
print(num2words(12.42, to='currency', lang='ru'))   # двенадцать евро, сорок два цента


# from hello_module import say_hello
from hello_module import sum_privet_my_world as hello_sum, say_hello

say_hello("Павел")

print('\n\n')

# Django


print(('\n\n'))
print(sum([1, 2]))
text_1 = 'Hello '
text_2 = 'world!'
print(hello_sum(text_1, text_2))



# requests
import requests

# response = requests.get('http://geekbrains.ru')
# print(response)

# Правила порядка импорта:
# импортируем стандартные библиотеки  -  sys, time, datetime, math ...
# импортируем внешние библиотеки - requests, django, flask...
# импортируем свои модули, пакеты


# Модуль sys: запуск скрипта с параметрами
# Напишем скрипт для сложения чисел в командной строке (терминале)
# import sys
#
#
def main(argv):
    print(f'argv={argv}')
    program, *args = argv
    result = sum(map(int, args))
    print(f'результат: {result}')

    return 0
#
#
# if __name__ == '__main__':
#    exit(main(sys.argv))

# Рекомендуем в будущем изучить модуль argparse — он позволяет писать серьёзные инструменты для командной строки.
# argparse - https://docs.python.org/3.8/library/argparse.html#module-argparse


# Модуль time: профилируем время выполнения участков кода
# time_profiler.py

print('end file')
