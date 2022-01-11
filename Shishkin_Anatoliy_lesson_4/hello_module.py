def say_hello(name: str) -> None:
    print(f'Привет, {name}!')


def sum_privet_my_world(a: str, b: str) -> str:
    return a + b


if __name__ == '__main__':
    say_hello('Тимур')
    print(__name__)
    sum([1, 2, 3])