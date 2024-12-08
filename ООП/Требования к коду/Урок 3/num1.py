from math import sqrt
from typing import Optional


def add_numbers(xv: int, yv: int) -> int:
    return xv + yv


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return ''
    str_ret = 'Мы вычислили квадратный корень из введённого вами числа. '
    str_ret += 'Это будет: '
    roott = calculate_square_root(your_number)
    str_ret += str(roott)
    return str_ret


xv = 10
yv = 5
print('Сумма чисел: ', add_numbers(xv, yv))
print(calc(25.5))
