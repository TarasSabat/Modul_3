'''
Створення та виклик функцій
'''
# def say_hello():
#     print('Привіт, Світ!')   # блок, що належить функції
#     # Кінець функції say_hello()
'''
виклик функції
'''
# say_hello()
##
# def calculate_sum():

#     x = 2
#     y = 3
    
#     return x + y

# print(calculate_sum())
'''
Аргументи функцшї
'''
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
'''
Повернення результату
'''
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
'''
Локальні змінні
Область видимості усіх змінних обмежена блоком, в якому вони оголошені, 
починаючи з точки оголошення імені.
'''
# x = 50

# def func():
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('x як і раніше', x)   # x як і раніше 50
##
# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x


# result = func_outer()  # 5
'''
Global
Щоб присвоїти деяке значення змінній, визначеній на вищому рівні програми 
(тобто не у якійсь зоні видимості, як функції), необхідно вказати Python, що її ім'я не локальне, 
а глобальне (global). Зробимо це за допомогою зарезервованого слова global. 
Без застосування зарезервованого слова global неможливо присвоїти значення змінній, 
визначеній за межами функції.
'''
# x = 50

# def func():
#     global x
#     print('x дорівнює', x) # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)   # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)   # Значення x складає 2
##
# a = 5
# b = 0


# def fun():
#     global a
#     a = 10
#     b = 2


# fun()
# print(a)  # 10
# print(b)  # 0
'''
Ключові аргументи
'''
# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# func(3, 7)          # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(25, c=24)      # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(c=50, a=100)   # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# #
# def calculate_diff(x, y, z):
#     return x - y -z
# result = calculate_diff(2, z = 5, y = 10)
# print(result)
'''
## Функція з ім'ям say використовується для виведення на екран рядка, вказаного число разів.
'''
# def say(message, times=1):
#     print(message * times)

# say('Привіт')   # Привіт
# say('Світ', 5)   # СвітСвітСвітСвітСвіт

'''
## Змінна кількість параметрів (Flexible Number or Argument) прийме за аргумент усе, 
# що вказати при виклику
Іноді буває необхідно визначити функцію, здатну приймати будь-яку кількість параметрів. 
Цього можна досягти за допомогою зірочок:
'''
# def total(a=5, *numbers, **phone_book):
#     print('a', a)
#     # прохід по всіх елементах кортежу
#     for single_item in numbers:
#         print('single_item', single_item)

#     #прохід по всіх елементах словника
#     for first_part, second_part in phone_book.items():
#         print(first_part,second_part)

# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
##
# def calculate_diff(*args):
#     return args
# result = calculate_diff(1, 2, 3, 4, 5)
# print(result)
'''
В результаті в консолі ми побачимо:
a 10
single_item 1
single_item 2
single_item 3
Jack 1123
John 2231
Inge 1560
None
'''
'''
Щоб створити порожній кортеж, існують два способи, хоча і не зовсім зрозуміло навіщо потрібний 
порожній кортеж :-)
'''
# my_tuple = tuple()
# another_tuple = ()

# # Створення ж непорожніх кортежів відбувається наступним чином:

# not_empty = (1, 2, 3)

# # Доступ до елементів кортежу відбувається за індексом за допомогою синтаксису квадратних дужок:

# not_empty = (2, 4, 6)
# not_empty[0]    # 2
# not_empty[1]    # 4
# not_empty[2]    # 6
'''
Словники
Порожній словник можна створити одним з двох способів:
'''
# empty_dict = {}
# another_empty_dict = dict()

# # Створити непорожній словник можна наступним чином:

# some_dict = {"key": "value", 1: "one", }
# # Запис пари ключ-значення у вже існуючий словник відбувається за допомогою квадратних дужок 
# # і оператора присвоєння =:

# not_empty = {"key": "value"}
# not_empty["new_key"] = "new value"
# print(not_empty)    # {"key": "value", "new_key": "new value"}
'''
Рекірсія
'''
##
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# factorial(5)    # 120
##
# def pover(x, n):
#     if n == 0:
#          return 1
#     return x * pover(x, n-1)

# pover(2, 3)
# print(pover)

# Як працює ?
# pover (2, 3)
# 2 * pover (2, 2)
#     2 * pover (2, 1)
#         2 * pover (2, 0)
'''
Фібаначі (Fn = Fn-1 + Fn-2)
'''


# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n-1)+fib(n-2)


# print(fib(10))

'''
Імпорт пакетів та модулів
У Python є великий набір пакетів та модулів з готовими корисними функціями та інструментами.
Імпортування у Python відбувається за допомогою ключового слова import, після якого ви можете 
вказати один або декілька пакетів, які ви хочете імпортувати.
'''
# import math

# sin_pi = math.sin(math.pi)
# # У цьому прикладі ми імпортували пакет математичних функцій і констант math та зберегли 
# # значення синуса π у sin_pi

# # Є й інший спосіб: можна імпортувати з пакета тільки те, що нам необхідно 
# # за допомогою виразу from ... import ...:

# from math import pi, sin

# sin_pi = sin(pi)

# # Модулем Python є будь-який текстовий файл з розширенням py, який містить код мовою Python. 
# # Це означає, що коли ви створюєте скрипт hello.py, який містить ось такий код:

# def say_hello(name):
#     print(f'Hello {name}')
# # ви можете імпортувати функцію say_hello з hello.py за домопогою виразу: 
# # from hello import say_hello у будь-якому модулі в тій самій папці, що і hello.py.

# # Важливо розуміти, що під час імпорту модуля Python виконує увесь код, що міститься в модулі. 
# # Саме через це модуль з ось таким вмістом:

# def say_hello(name):
#     print(f'Hello {name}')

# print("You imported hello.py")
# say_hello('user')

# # Під час імпорту (виконання виразу from hello import say_hello) виведе у консоль:

# You imported hello.py
# Hello user

# # Далеко не завжди така поведінка бажана.
'''
Точка входу
Що ж робити, коли ми хочемо зробити скрипт, що виконується (який можна викликати із консолі 
командою python [ім'я скрипта]), але зберегти можливість імпорту з цього модуля, не викликаючи його? 
В таких випадках нам може допомогти службова змінна Python: __name__. 
Річ у тому, що якщо скрипт викликаний безпосередньо, то він є "точкою входу" та __name__ == "__main__".
Якщо ж цей модуль виконується під час імпорту, то __name__ == "hello" 
(наприклад для модуля, який називається hello.py). 
Таким чином ми можемо модифікувати наш модуль hello.py:
'''
# def say_hello(name):
#     print(f'Hello {name}')

# if __name__ == '__main__':
#     print("You imported hello.py")
#     say_hello('user')

# # Тоді під час імпорту функції say_hello із hello.py код у блоці if ... не буде виконаний, 
# # а якщо ж в консолі виконати python hello.py, то буде.
# # Для зручності прийнято весь код, який потрібно виконати, коли модуль викликається із консолі 
# # (не імпортується), поміщати у функцію main:

# def say_hello(name):
#     print(f'Hello {name}')

# def main():
#     print("You imported hello.py")
#     say_hello('user')

# for arg in sys.argv:
#     print(arg)
# if __name__ == '__main__':
#     main()

# # Так заведено і функцію main ще називають "точкою входу", оскільки робота застосунку починається 
# # з виклику цієї функції. Ви, звичайно, можете назвати цю функцію як завгодно, 
# # але називати її саме main вважається хорошим тоном.
