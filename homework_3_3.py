# 1. Простая работа с print()

# print("Привет, мир!")
#
# print(5, 10 , 15)
#
# r = 10 + 25
# print(r)

# 2. Использование параметров sep и end в print()

# print(1, 2 , 3, sep=" & ")
#
# print("Python", end=" ")
# print("Лучший язык")

# 3. Форматированный вывод с F-строками
# x = 3.14
# y = -8
# print(f"Координаты точки: x = {x}, y = {y} ")
#
# name = input("Ваше Имя")
# age = input("Введите ваш возраст")
# print(f"Имя {name}, Возраст: {age}")

# 4. Работа с input()

# name = input("Введите ваше имя")
# print(f"Привет, {name}")

#  Преобразование типов

# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
#
# number1 = float(num_1)
# number2 = float(num_2)
#
# result = number1 + number2
#
# print(f"Сумма чисел: {result}")

# integer = input("Целое число: ")
#
# number = int(integer)
#
# result = number ** 2
#
# print(f"Квадрат числа: {number} равен: {result}")

# 1. Основы булевой логики

# print(5 > 3)
# print(10 < 2)
# print(7 == 7)
# print(6 != 8)
# print(4 >= 4)
# print(9 <= 3)
#
# res = 8 > 12
# print("Результат сравнения :", res)
# print("Тип переменной :", type(res))

# 2. Проверка четности и кратности числа

# x = 15
#
# a = x % 2 == 0
# print(f"число {x} чётное {a}")
#
# b = x % 5 == 0
# print(f"число {x} делится на 5? {b}")
#
# c = (x % 3 == 0) and (x % 5 == 0)
#
# print(f"число {x} делится на 3 и 5 одновременно? {c}")

# 3. Работа с логическими операторами (and, or, not)

# y = 4.5
#
# c = (y >= 1) and (y <= 10)
# print(c)
#
# d = ((y >= 0) and (y <= 5)) or ((y >= 10) and (y <= 15))
# print(d)
#
# a = not (y <= 5)
# print(a)


# Приоритет логических операций
# a = True or False and False
# print(a)
#
# b = not False and True
# print(b)
#
# c = False or not True and True
# print(c)
#
# d = not (10 > 5 or 3 < 1)
# print(d)

# Приведение типов к bool

# print(bool(0))
# print(bool(-5))
# print(bool(3.14))
#
# print(bool(""))
# print(bool("Python"))
# print(bool(" "))

# n = 18
#
# tes = n > 0
# print(tes)
#
# rep = n % 2 == 0
# print(rep)
#
# rek = n % 3 == 0
# print(rek)

# Доступ к символам по индексу.

s = "Программирование"
#
# char_1 = s[0]
# print(char_1)
#
# char_2 = s[-1]
# print(char_2)
#
# char_3 = s[2]
# print(char_3)
#
# char_4 = s[-2]
# print(char_4)

# char_22 = s[100]
# print(char_22) #IndexError: string index out of range

# charm = len(s) - 1
# charm2 = s[charm]
# print(charm)
# print(s[charm])

# Создание срезов

s = "Программирование"

# print(s[:6])
# print(s[:-5])
# print(s[2:7])
# print(s[::2])
# print(s[::-1])

# Работа с шагом в срезах

# print(s[::3])
# print(s[::-2])

# Проверка неизменяемости строк

# s[0] = "п"
# print(s) #TypeError: 'str' object does not support item assignment

# s2 = "п" + s[1:]
# print(s)
# print(s2)

# Дополнительное задание

word = "abcdefgh"

a = word[2:5]
print(a)

b = word[::-1]
print(b)

c = word[1:-1]
print(c)