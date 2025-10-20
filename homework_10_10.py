"""
++++++++++++++++++++++++++++++++++++++++++++++++
Множества в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Создайте множество с элементами .
Добавьте в него число, затем попробуйте добавить уже существующий элемент.
Выведите итоговое множество.
# ===============================================
"""
# cities_list = [
#     "Москва",
#     "Санкт-Петербург",
#     "Москва",
#     "Казань",
#     "Нижний Новгород",
#     "Санкт-Петербург",
#     "Екатеринбург",
#     "Москва",
#     "Казань"
# ]
#
# unique_cities = set(cities_list)
#
# print("Уникальные города:", unique_cities)
# print("Количество уникальных городов:", len(unique_cities))
# Как видим, в списке было 9 городов, но уникальных оказалось только 5, так как некоторые города повторялись.

# 3. Создайте множество с числами от 1 до 10.

# numbers = set(range(1, 11))
# print("Исходное множество:", numbers)
#
# numbers.remove(5)
# print("После удаления 5:", numbers)
#
# numbers.discard(15)
# print("После попытки удаления 15:", numbers)

# 5. Создайте пустое множество и попробуйте добавить в него следующие элементы:

# my_set = set()
# #
# # try:
# #     my_set.add(10)
# #     print("Успешно добавлено число 10")
# #
# #     my_set.add("hello")
# #     print("Успешно добавлена строка 'hello'")
# #
# #     my_set.add((1, 2, 3))
# #     print("Успешно добавлен кортеж (1, 2, 3)")
# #
# #     my_set.add([4, 5, 6])
# #     print("Успешно добавлен список [4, 5, 6]")
# # except TypeError as e:
# #     print(f"Ошибка при добавлении: {e}")
# #
# # print("Итоговое множество:", my_set)

# 6. Создайте 2 множества, в которых совпадают 2 элемента
# Найдите:
# Пересечение A и B.

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
#
# intersection = A & B
# print("Пересечение A и B:", intersection)
#
# union = A | B
# print("Объединение A и B:", union)
#
# difference_AB = A - B
# print("Разность A - B:", difference_AB)
#
# difference_BA = B - A
# print("Разность B - A:", difference_BA)
#
# symmetric_difference = A ^ B
# print("Симметричная разность A ^ B:", symmetric_difference)


# 7. Создайте два множества из чисел 1 до 10:

# even_numbers = {x for x in range(1, 11) if x % 2 == 0}
# print("Четные числа:", even_numbers)
#
#
# odd_numbers = {x for x in range(1, 11) if x % 2 != 0}
# print("Нечетные числа:", odd_numbers)
#
#
# intersection = even_numbers & odd_numbers
# print("Пересечение (общие элементы):", intersection)
#
#
# union = even_numbers | odd_numbers
# print("Объединение (все элементы):", union)


# Создаем множества студентов

# python_students = {"Анна", "Иван", "Мария", "Сергей"}
# java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
#
#
# both_courses = python_students & java_students
# print("На оба курса записаны:", both_courses)
#
#
# only_one_course = python_students ^ java_students
# print("Только на один курс записаны:", only_one_course)
#
#
# all_students = python_students | java_students
# print("Записаны хотя бы на один курс:", all_students)

# 9. Даны множества слов:

# text1 = set("программирование")
# text2 = set("автоматизация")
#
# common_letters = text1 & text2
# print("Общие буквы:", common_letters)
#
# unique_to_text1 = text1 - text2
# print("Буквы только в первом слове:", unique_to_text1)
#
# unique_letters = text1 ^ text2
# print("Уникальные буквы каждого слова:", unique_letters)

# ++++++++++++++++++++++++++++++++++++++++++++++++
# Генераторы множеств и словарей
# ++++++++++++++++++++++++++++++++++++++++++++++++

# 1. Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел.

# even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
# print("Множество квадратов четных чисел:", even_squares)

# 2. Дан список:

# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
#
# unique_uppercase_words = {word.upper() for word in words}
#
# print("Исходный список:", words)
# print("Множество уникальных слов в верхнем регистре:", unique_uppercase_words)
#

# 3. Дан словарь:
# Исходный словарь с оценками

# grades = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "David": 60,
#     "Eve": 88
# }
#
# grade_results = {
#     student: ("отлично" if score >= 80 else "удовлетворительно")
#     for student, score in grades.items()
# }
#
# print("Исходный словарь оценок:")
# print(grades)
# print("\nПреобразованный словарь:")
# print(grade_results)

#Дано множество слов:
# text = {"Python", "automation", "programming", "testing"}
#
# word_lengths = {word: len(word) for word in text}
#
# print("Исходное множество слов:")
# print(text)
# print("\nПолученный словарь:")
# print(word_lengths)

#Создайте вложенный словарь, где ключи – числа от 1 до n (для примера пусть n = 10), а значения – множества квадратов чисел от 1 до ключа.

# n = 10
#
# nested_dict = {
#     i: {x**2 for x in range(1, i+1)}
#     for i in range(1, n+1)
# }
#
# print("Вложенный словарь:")
# for key, value in nested_dict.items():
#     print(f"{key}: {value}")
