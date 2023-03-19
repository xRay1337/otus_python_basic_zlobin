"""
Домашнее задание №1
Функции и структуры данных
"""
from math import factorial
from typing import Callable, List


def power_numbers(*numbers: int) -> List[int]:
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


def is_odd_number(number: int) -> bool:
    return number % 2 != 0


def is_even_number(number: int) -> bool:
    return number % 2 == 0


def is_prime_number(number: int) -> bool:
    return False if number < 2 else factorial(number - 1) % number == number - 1


def get_filter_function_by_mode(mode: str) -> Callable[[int], bool]:
    return {
        "odd": is_odd_number,
        "even": is_even_number,
        "prime": is_prime_number
    }.get(mode)


def filter_numbers(numbers: List[int], mode: str) -> List[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    return list(filter(get_filter_function_by_mode(mode), numbers))
