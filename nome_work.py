'''
Створіть функцію greeting, яка всередині виводить вітальне повідомлення print('Hello world!'). 
І викличте її.
'''
# def greeting():
#     print('Hello world!')

# greeting()
'''
Нехай нам необхідно створити розсилку запрошень на якийсь захід. 
Повідомлення для кожного учасника однакове, нам необхідно міняти лише ім'я запрошеного. 
Цілком очевидно, що для формування такого повідомлення краще використовувати функцію. 
Створіть функцію invite_to_event, яка приймає ім'я запрошеного username і повертатиме 
наступний f-рядок: "Dear {username}, we have the honour to invite you to our event".
'''
# def invite_to_event(username):
#     return f'Dear {username}, we have the honour to invite you to our event'


# username = input('Username: ')
# print(invite_to_event(username))
'''
Необхідно написати функцію, яка буде обчислювати суму за користування послугами таксі. 
Сума складається з базового тарифу 40 грн, та 10 грн за кожен кілометр поїздки. 
Напишіть функцію, яка приймає один параметр — відстань поїздки в кілометрах. 
Функція має повертати підсумкову суму оплати за послуги таксі дійсним числом. 
Також функція повинна змінювати глобальну змінну — лічильник total_trip після кожного виклику 
та збільшувати її на одиницю.
'''
# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def calculate_trip_price(distance_km):

#     global total_trip
#     total_trip += 1
#     sum = base_rate + (price_per_km * distance_km)
#     return sum

# distance_km = int(input('Distance km.: '))
# print(calculate_trip_price(distance_km))
# print(total_trip)
'''
Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price. 
Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1. 
Тут і надалі ми під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни. 
І на цей розмір ми знижуємо підсумкову вартість товару. Логіку функції необхідно 
прописати у внутрішній функції apply_discount, використовуючи оголошення зміною price як nonlocal.
'''
# def discount_price(price, discount):

#     def apply_discount():
#         nonlocal price
#         price = price - (price * discount)

#     apply_discount()
#     return price

# print(discount_price(100, 0.1))
'''
Напишімо функцію, яка повертає повне ім'я користувача. У базі даних переважно зберігають ім'я 
користувача first_name, його прізвище last_name та по батькові, або, як заведено в західних країнах, 
друге ім'я — middle_name. Причому middle_name — це необов'язкова змінна, вона може бути, 
а може й не передаватися під час виклику функції. Наша функція повертатиме рядок з повним ім'ям 
'first_name middle_name last_name', якщо ж змінна middle_name відсутня, то рядок, 
що повертається повинен бути 'first_name last_name'.
'''
# def get_fullname(fitst_name, last_name, middle_name = 0):
#     if middle_name:
#         return f'{fitst_name} {middle_name} {last_name}'
#     else:
#         return f'{fitst_name} {last_name}'

# print(get_fullname('Taras', 'Sabat', 'Volodimirovich'))
'''
Створіть функцію format_string для форматування рядка. У функцію ми передаємо рядок string та length 
довжину нового рядка. Функція повертає новий рядок за наступним алгоритмом:
Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.
Тести на правильність роботи функції виконуються для наступних наборів аргументів:
string='aaaaaaaaaaaaaaaaac', length=12
length=15, string='abaa'
'''
## Варіант мій
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         probil = (length - len(string)) // 2
#         return f'{" " * probil}{string}'


# print(format_string(length=15, string='abaa'))
## Варіант 2
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         probil = (length - len(string)) // 2
#         char = " " * probil
#         string = char + string
#         return string


# print(format_string(length=15, string='abaa'))
'''
Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.
Створіть дві функції:
перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість 
позиційних аргументів. Функція повинна повернути суму size із загальною кількістю переданих до неї 
позиційних аргументів.
друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових 
аргументів, і також має повернути суму size з кількістю переданих у функцію ключових аргументів.
Тестові виклики функцій для правильності роботи будуть наступними:

first(5, "first", "second", "third")
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")
'''
# def first(size, *args):
#     return size + len(args)

# def second(size, **kwargs):
#     return size + int(len(kwargs))

# print(first(5, "first", "second", "third"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
'''
Онлайн-магазин "У Бобра" надає послугу експрес доставлення своїх товарів за ціною 5$ за перший товар 
у замовленні та 2$ - за всі наступні товари. Необхідно реалізувати функцію, яка приймає як перший 
параметр кількість товарів у замовленні quantity, але також має бути присутнім параметр, 
що передається тільки за ключем discount.
Параметр discount за замовчуванням має значення 0 - знижки немає. Приймає значення від 0 до 1. 
Функція cost_delivery повертає загальну суму за доставлення товару з урахуванням знижки.
Треба передбачити, що функція cost_delivery при визові може приймати будь-яку кількість позиційних 
аргументів.
Приклад:
cost_delivery(2, 1, 2, 3)
При такому виклику quantity дорівнює 2, а параметр discount за умовчанням має значення 0.

Тестові виклики функції для правильності роботи будуть наступними:
cost_delivery(2, 1, 2, 3) == 7
cost_delivery(3, 3) == 9
cost_delivery(1) == 5
cost_delivery(2, 1, 2, 3, discount=0.5) == 3.5
'''    
def cost_delivery():