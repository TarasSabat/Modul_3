''' Функції котрі виводять ім'я файлу та шлях до нього.'''

# import sys
# import pathlib

# def print_file_name(file_name, full_name=False, margin=0, margin_item=' '):
#     margin = margin * margin_item
#     if full_name:
#         print(margin + str(file_name.absolute())) # шлях до файлу
#     else:
#         print(margin + str(file_name.name))       # сама назва файлу

# def main():
#     file_name = pathlib.Path(sys.argv[0])
#     print_file_name(file_name, margin_item='*', full_name=True, margin=30) # іменовані не обов'язково по порядку
    # print_file_name(file_name, True, 30, '-')   # позиційні можна не називати
    # print_file_name(                              # ще один варіант передаі даних
    #     file_name,                                # якщо вказані дефолтні значення (по замовчуванню) -
    #     margin_item='*',                           # - їх можна взагалі не передавати
    #     full_name=True,
    #     margin=30
    # )


# if __name__ == "__main__":
#     main()

''' Порахувати суму всіх аргументів '''

# def sum(start, *args):
#     sum = start
#     for element in args:
#         sum += element
#     return sum

# result = sum(2, 3, 5, 1)
# print(result)
# ​або
# print(sum([2, 3, 5, 1]))

'''Порахувати суму всіх чисел через рекурсію
10 -> 10 + 9 + 8 + 7 + ... + 1'''

# import sys
# sys.setrecursionlimit(2000)   # збільшення глибини рекурсії

# sum = 0

# # for num in range(1, 11):  # звичайний спосіб
# #     sum += num
# #
# # print(sum)

# def sum_numbers(max_num):
#     if max_num <= 0:
#         return 0
#     elif max_num == 1:
#         return 1
#     return max_num + sum_numbers(max_num - 1)


# print(sum_numbers(1999))
# # sum_numbers(10) -> 10 + sum_numbers(9)
# # sum_numbers(9) -> 9 + sum_numbers(8)
# # sum_numbers(8) -> 8 + sum_numbers(7)
# # sum_numbers(7) -> 7 + sum_numbers(6)
# # sum_numbers(6) -> 6 + sum_numbers(5)
# # sum_numbers(5) -> 5 + sum_numbers(4)
# # sum_numbers(4) -> 4 + sum_numbers(3)
# # sum_numbers(3) -> 3 + sum_numbers(2)
# # sum_numbers(2) -> 2 + sum_numbers(1)
# # sum_numbers(1) -> 1

'''Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII'''
# {'key': 'value'} # словник

# hello world

# def codes_of_string(string: str) -> dict:
#     codes = {}                  #  створення пустого словника
#     for ch in string:           #  ch - символ
#         if not ch in codes:
#             codes[ch] = ord(ch)  #  {'h': 104} ord - повертає символ кодом
#     return codes

# print(codes_of_string('hello world'))

'''Написати функцію для визначення, чи є число простим?'''
# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def main():
#     value = int(input('Please enter the number: '))
#     if is_prime(value):
#         print(f'{value} - просте число')
#     else:
#         print(f'{value} - не є простим числом')


# if __name__ == "__main__":
#     main()

'''Написати калькулятор'''
# 3, 4, '+' -> 7
# 3, 4, '*' -> 12
# 3, 4, '-' -> Функція не підтримує дану операцію
def calc(operation: str):
    result = None  # -
    if operation == "+":
        result = 0
    elif operation == "*":
        result = 1
    else:
        return "Функція не підтримує дану операцію"
​
    value = input('Please enter the value: ')
​
    while True:
        if value == '':
            break
        if operation == "+":
            result += int(value)
        elif operation == "*":
            result *= int(value)
        value = input('Please enter the value: ')
    return result
​
​
result = calc("*")
print(result)
