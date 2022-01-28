"""
Урок 9. Объектно-ориентированное программирование. Введение
"""
from datetime import datetime, timedelta

# определение класса
class Woman:
    name: str = 'Светлана'  # глобальные атрибуты класса
    birthday: datetime = datetime.now()

    # методы класса
    def introduce_youself(self):
        print(f"I'm {self.__class__.__name__}")

    def get_info(self):
        print(f'Давая знакомиться: я - {self.name} и я родилась {self.birthday.strftime("%d %B %Y")}')

    def say(self, message: str):
        print(f'{self.name} сказала нам: "{message}"')


i = list()
girl = Woman()
print(type(girl), girl)
girl.introduce_youself()
girl.get_info()
girl.say('Привет мальчики!')
print('\n')
# girl2 = Woman()
# girl2.name = 'Мария'
# print(girl.name, girl2.name, Woman.name)
# Woman.name = 'Елена'
# print(girl.name, girl2.name, Woman.name)
print('\n')

# Конструтор __init__
class Rabbit:
    auto_count: int = 0

    def __init__(self):
        Rabbit.auto_count += 1


rabbits = [Rabbit() for _ in range(1000)]
rabbits = [Rabbit() for _ in range(1000)]
first_rabbit = rabbits[0]
print(f'Наплодили кроликов - {first_rabbit.auto_count} шт.')
print('\n')


# Локальные и глобальные переменные
class Cat:
    breed_2 = 'Дурная'

    def her_breed(self):
        breed = 'Породистая'
        return breed


kitty = Cat()
# print(kitty.breed)
print(kitty.breed_2)
print(kitty.her_breed())
print('\n')


"""
Модификаторы доступа

Public (публичный);
Protected (защищённый);
Private (приватный).
"""
class Dog:

    def __init__(self):
        self.voice = 'гав-гав'
        self._color_hair = 'хаки'
        self.__place = 'будка во дворе'


dog = Dog()
print(dog.voice)
print(dog._color_hair)
# print(dog.__place)
print('\n')

# Инкапсуляция
class Ant:
    __species: str = 'коричневый'

    def __get_species(selfself):
        print('Защищённый метод')


ant = Ant()
ant._Ant__get_species()
print(ant._Ant__species)
print('\n')


# Наследование
import time


class People:
    """Так зарождалось всё человечество)))"""
    def __init__(self, name: str, birthday: datetime):
        self.name = name
        self.birthday = birthday

    def introduce_youself(self):
        return f"I'm {self.__class__.__name__}", self.__get_info()

    def __get_info(self):
        return dict(name=self.name, birthday=self.birthday.strftime("%d %B %Y"))


class Man(People):
    sex: str = 'm'

    def working(self, sleeping: int = 5):
        """Мужик должен уметь работать"""
        while sleeping:
            print(f'Осталось спать секунд: {sleeping}')
            time.sleep(1)
            sleeping -= 1
        print('Поработали, теперь можно и домой!')


worker = Man('Владимир', datetime(year=1993, month=7, day=1))
introduce_message, worker_info = worker.introduce_youself()
print(f' {3 * "-//-"} '.join(map(str, [introduce_message, worker_info, type(introduce_message), type(worker_info)])))
# worker.working()


class Woman2(People):
    sex: str = 'w'

    def __init__(self, name: str, birthday: datetime, secret: str):
        super(Woman2, self).__init__(name, birthday)
        self.secret = secret


girl_2 = Woman2('Светлана', datetime.now() - timedelta(days=365 * 18), 'Секретная фраза - "Пожалуй нет"')
introduce_message, woman_info = girl_2.introduce_youself()
print(f' {3 * "-//-"} '.join(map(str, [introduce_message, woman_info, type(introduce_message), type(woman_info)])))
# girl_2.working()
print('\n')


# Несколько родителей у одного класса
# class Father:
#     def send_money(self):
#         print('Деньги перечислены')
#
#     def my_dream(self):
#         print('Я стану космонавтом')


class Mother:
    def be_happy(self):
        print('Не в деньгах счастье!')

    def my_dream(self):
        print('Где спрятаться от этого всего!')


# class Child(Father, Mother): ...




# Полиморфизм | Перегрузка методов
class Father:
    def send_money(self, empty: bool = False):
        if not empty:
            print('Деньги перечислены')
        else:
            print('Я иду заработать')


class Child(Father, Mother):
    def my_dream(self):
        # super(Child, self).my_dream()
        print('Закончу школу и жизнь изменится ^_^')


baby = Child()
baby.send_money(empty=True)
baby.be_happy()
baby.my_dream()
print('\n')

print('end')
