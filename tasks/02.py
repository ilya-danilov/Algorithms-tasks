# Даны два числа a и b, представленные в виде строк.
# Найдите произведение этих чисел и верните его в виде строки.


NUM_SYS = 10

def add_two_large_numbers(initial_number: str, number_to_add: str, dozen_shift: int) -> str:
    resulting_number = ''
    dozen_flag = 0

    initial_number = '0' * (len(number_to_add) + dozen_shift - len(initial_number)) + initial_number

    for index in range(-1, (-dozen_shift - 1), -1):
        resulting_number = str(initial_number[index]) + resulting_number
    
    for index in range(-1, -len(number_to_add) - 1, -1):
        sum_figures = int(number_to_add[index]) + int(initial_number[index - dozen_shift]) + dozen_flag
        resulting_number = str(sum_figures % NUM_SYS) + resulting_number
        dozen_flag = sum_figures // NUM_SYS
    
    for index in range(-(len(number_to_add) + dozen_shift) - 1, -len(initial_number) - 1, -1):
        sum_figures = int(initial_number[index]) + dozen_flag
        resulting_number = str(sum_figures % NUM_SYS) + resulting_number
        dozen_flag = sum_figures // NUM_SYS
    
    if dozen_flag != 0:
        resulting_number = str(dozen_flag) + resulting_number

    return resulting_number


def multiply_large_number_on_single_digit_number(large_number: str, single_digit_number: str) -> str:
    resulting_number = ''
    dozen_flag = 0

    single_digit_number = int(single_digit_number)

    if single_digit_number == 0:
        return '0'

    for index in range(-1, -len(large_number) - 1, -1):
        mul_figures = int(large_number[index]) * single_digit_number + dozen_flag
        resulting_number = str(mul_figures % NUM_SYS) + resulting_number
        dozen_flag = mul_figures // NUM_SYS
    
    if dozen_flag != 0:
        resulting_number = str(dozen_flag) + resulting_number

    return resulting_number


def check_the_numbers_for_negativity(first_number: str, second_number: str) -> tuple[str, str, bool]:
    is_negative = False
    is_negative_first = False
    is_negative_second = False

    if first_number[0] == '-':
        is_negative_first = True
    if second_number[0] == '-':
        is_negative_second = True

    if is_negative_first or is_negative_second:
        is_negative = True
        if is_negative_first and is_negative_second:
            is_negative = False
    
    first_number = first_number[1:] if is_negative_first else first_number
    second_number = second_number[1:] if is_negative_second else second_number

    return first_number, second_number, is_negative


def multiply_two_large_numbers(first_number: str, second_number: str) -> str:
    resulting_number = ''

    first_number, second_number, is_negative = check_the_numbers_for_negativity(first_number, second_number)

    longest_number = first_number if len(first_number) >= len(second_number) else second_number
    shortest_number = first_number if len(first_number) < len(second_number) else second_number

    for index in range(-1, -len(shortest_number) - 1, -1):
        dozen_shift = -index - 1

        temp = multiply_large_number_on_single_digit_number(longest_number, shortest_number[index])
        resulting_number = add_two_large_numbers(resulting_number, temp, dozen_shift)
    
    return f'-{resulting_number}' if is_negative else resulting_number


# print(multiply_two_large_numbers('-1234567890123456789012345678901234567890', '9999999999999999999999999999999999999999'))