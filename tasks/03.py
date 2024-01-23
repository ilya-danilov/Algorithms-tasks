# Реализуйте алгоритм быстрого возведения числа a в степень b.


# Исходная степень | Преобразованная степень | Количество операций умножения
#  x^1 | x               | 0
#  x^2 | x^2             | 1
#  x^3 | x^2 * x         | 2
#  x^4 | (x^2)^2         | 2
#  x^5 | (x^2)^2 * x     | 3
#  x^6 | (x^2 * x)^2     | 3
#  x^7 | (x^2 * x)^2 * x | 4
#  x^8 | ((x^2)^2)^2     | 3
#  x^9 | ((x^2)^2)^2 * x | 4


def fast_power(number: int, degree: int) -> int:
    result = 1
    intermediate = number

    if degree < 0:
        raise ValueError(f'The degree of the number should be more than zero, not equal to {degree}')

    while degree != 0:
        if degree % 2 == 0:
            degree = degree / 2
            intermediate = intermediate ** 2
        else:
            degree = degree - 1
            result = result * intermediate

    return result


# print(fast_power(-2, 7))