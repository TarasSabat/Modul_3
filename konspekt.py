# # Створення та виклик функцій
# def say_hello():
#     print('Привіт, Світ!')   # блок, що належить функції
#     # Кінець функції say_hello()

# # виклик функції
# say_hello()
##
# def calculate_sum():

#     x = 2
#     y = 3
    
#     return x + y

# print(calculate_sum())
###
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# # Повернення результату
# def plus(a, b):
#   c = a + b
#   return c

# res = plus(3, 4)
# print(res)  # Виведе 7

# Або ще коротше:

# def plus(a, b):
#   return a + b

# print(plus(3, 4))   # Виведе 7
'''
Визначення функції починається з ключового слова def, після має йти ім'я функції, далі дужка, 
що відкриває (, дужка, що закриває ) і знак двокрапки :. Тіло функції починається з нового рядка 
з потрібним відступом. Python вважає, що знайшов кінець тіла функції, як тільки відступ у рядку 
стане такого ж рівня, як в оператора def
'''
# def hello():
#     print('Hello user!')

# # Саме визначення функції не змусить код виконатись, необхідно виконати виклик функції

# def hello():
#     print('Hello user!')

# hello()  # Hello user!

## Ключові аргументи
# def calculate_diff(x, y, z):
#     return x - y -z

# result = calculate_diff(2, z = 5, y = 10)
# print(result)

## Змінна кількість параметрів (Flexible Number or Argument) прийме за аргумент усе, 
# що вказати при виклику
# def calculate_diff(*args):
#     return args
# result = calculate_diff(1, 2, 3, 4, 5)
# print(result)

