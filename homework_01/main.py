"""
Домашнее задание №1
Функции и структуры данных
"""
from math import factorial


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd_number(number):
    return number % 2 != 0


def is_even_number(number):
    return number % 2 == 0


def is_prime_number(number):
    return False if number < 2 else factorial(number - 1) % number == number - 1


def get_filter_function_by_mode(mode):
    return {
        "odd": is_odd_number,
        "even": is_even_number,
        "prime": is_prime_number
    }.get(mode)


def filter_numbers(numbers, mode):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filter_function = get_filter_function_by_mode(mode)

    return [number for number in numbers if filter_function(number)]
