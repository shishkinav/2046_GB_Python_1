"""
Урок 2. Некоторые встроенные типы и операции с ними
"""
a = 10
print(type(a))

if not isinstance(a, str):
    print('целочисленное')

print(type(a) == int)


# Список и его методы
print(dir(list))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

my_list = []
type(my_list)
<class 'list'>
my_list = list()
type(my_list)
<class 'list'>
my_list.append(666)
my_list
[666]
my_list.append('hello world')
my_list
[666, 'hello world']
my_list.clear()
my_list
[]
my_list.append(666)
my_list.append('привет')
my_list
[666, 'привет']
my_list.extend(('Василий', 15.55, 666))
my_list
[666, 'привет', 'Василий', 15.55, 666]
my_list.index('Василий')
2
my_list.insert(2, 'Марина')
my_list
[666, 'привет', 'Марина', 'Василий', 15.55, 666]
my_list.pop()
666
my_list
[666, 'привет', 'Марина', 'Василий', 15.55]
my_list.pop(1)
'привет'
my_list
[666, 'Марина', 'Василий', 15.55]
my_list.remove('Василий')
my_list
[666, 'Марина', 15.55]
"""
print('\n\n')
year = ['январь', 'февраль', "март", "апрель", "май"]
print('Реверс списка in_place')
print(id(year), year)
year.reverse()
print(id(year), year)

print('Реверс списка not in_place')
print(id(year), year)
year_reversed = list(reversed(year))
print(id(year_reversed), year_reversed)

# obj[start=0, stop=len(obj), step=1]
print('Ещё один способ реверса')
print(id(year), year)
new_year = year[::-1]
print(id(new_year), new_year)

"""
text = 'Hello world!'
text[0]
'H'
text[1]
'e'
text[2]
'l'
text[0:4:]
'Hell'
text[0:5:]
'Hello'
text[:5:]
'Hello'
text[::2]
'Hlowrd'
text[::-1]
'!dlrow olleH'
text[100::]
''
text[:100:]
'Hello world!'
"""

print('Сортировка in_place')
# print(id(year), year)
# year.sort()
# print(id(year), year)

print('Сортировка not in_place')
print(id(year), year)
new_year = sorted(year)
print(id(new_year), new_year)

"""
import string
string.digits
'0123456789'
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

import string
string.digits
'0123456789'
string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
ord("a")
97
ord("A")
65
chr(97)
'a'
chr(97-32)
'A'

for simbol in string.ascii_lowercase:
    print(simbol, end=' ')
    
a b c d e f g h i j k l m n o p q r s t u v w x y z >>> for simbol in string.ascii_lowercase:
    print(chr(ord(simbol) - 32), end=' ')
    
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
"""

my_list = [_ for _ in range(1, 11)]
print(my_list[2:10:3])  # хотелось бы срез для отображения 3, 6, 9

# Кортежи
import sys
my_list = ['Привет', True, 1.11, 555]
print(type(my_list), sys.getsizeof(my_list), my_list)
my_tuple = ('Привет', True, 1.11, 555)
print(type(my_tuple), sys.getsizeof(my_tuple), my_tuple)

print('\n\n')
print(dir(list))
print(dir(tuple))

# Нюансы присваивания и копирования объектов
print('\n\n')
a = [['Привет'], 10]
b = a
print(id(a), id(b))
b[1] = 15
print(a, b)
print(id(a), id(b))

from copy import copy, deepcopy

a = [['Привет'], 10]
b = a.copy()
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)

print('\n\n')
a = [['Привет'], 10]
b = deepcopy(a)
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)


print('\n\n')
# Форматирование строк
name = 'Айдар'
minute = 5
print("Проснись, %s! Вебинар закончится через %d" % (name, minute))
print("Проснись, {username:^20}! Вебинар закончится через {clock:.2f}".format(clock=minute, username=name))
print(f"Проснись, {name}! Вебинар закончится через {minute}")

print('\n\n')
text = "С новым годом!"
print(text.split())
text_list = text.split()
print('Привет' + 'мир!')
print(" ".join(text_list), type(" ".join(text_list)))

lst = ('аНаТоЛиЙ шишкин', "ПаВеЛ гордеев", "аНтон дубовицкий")
for name in lst:
    print(name.title())
    print(name.capitalize())
    print(name.upper())
    print(name.lower())

# реверс строки
message = 'екшамод к ьрепет илангоп'
print(message[::-1])

