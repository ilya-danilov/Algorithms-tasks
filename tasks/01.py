# Даны два числа a и b в десятичной системе счисления и основание некоторой системы счисления c.
# Найдите сумму этих чисел в системе счисления c.
# Результат представить в виде строки.


from  string import ascii_uppercase


"""Первое решение:"""

def convert_number_to_another_number_system(number: int, resulting_number: str, num_sys: int) -> str:
    remainder = str(number % num_sys)
    number = number // num_sys

    if int(remainder) > 9:
        remainder = ascii_uppercase[int(remainder) - 10]

    resulting_number = remainder + resulting_number
    
    if number == 0:
        return resulting_number
    
    return convert_number_to_another_number_system(number, resulting_number, num_sys)

def add_two_numbers_in_another_number_system(first_number: int, second_number: int, num_sys: int) -> str:
    resulting_number = ''
    is_negative = False

    sum_numbers = first_number + second_number

    if num_sys < 2:
        raise ValueError(f'Base of the number system should be more than 2, not {num_sys}')
    
    if sum_numbers < 0:
        is_negative = True
    sum_numbers = abs(sum_numbers)

    resulting_number = convert_number_to_another_number_system(sum_numbers, resulting_number, num_sys)
    return f'-{resulting_number}' if is_negative else resulting_number


"""Второе решение:"""

def add_two_numbers_in_another_number_system(first_number: int, second_number: int, num_sys: int) -> str:
    resulting_number = ''
    is_negative = False

    sum_numbers = first_number + second_number

    if num_sys < 2:
        raise ValueError(f'The base of the number system should be more than 2, not equal to {num_sys}')
    
    if sum_numbers < 0:
        is_negative = True
    sum_numbers = abs(sum_numbers)

    while sum_numbers != 0:
        remainder = str(sum_numbers % num_sys)
        sum_numbers = sum_numbers // num_sys

        if int(remainder) > 9:
            remainder = ascii_uppercase[int(remainder) - 10]

        resulting_number = remainder + resulting_number
    
    return f'-{resulting_number}' if is_negative else resulting_number


# print(add_two_numbers_in_another_number_system(-30, 0, 16))