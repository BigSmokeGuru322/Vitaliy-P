# 1. Пройти по списку с помощью итератора
from lesson_4.lesson_4_1 import words

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# it_numbers = iter(num)
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
#
# # 2. Итератор для строки
# str_1 = "Vitaliy"
# it_str1 = iter(str_1)
# print(next(it_str1))
# print(next(it_str1))

# 1. Создайте список из квадратов чисел от 1 до N, используя list comprehension.

# N = int(input("Введите N: "))
# squares = [num ** 2 for num in range(1, N + 1)]
# print(squares)
#
# result = [i for i in range(-10,11) if i % 2 == 0]
# print(result)

# words = ["Машинка", "Телевизор", "Апельсин", "Пульт", "Киви"]
#
# word_lengths = [len(words) for words in words]
#
# print("Список длин слов:", word_lengths)

# numbers = ["Чётное" if x % 2 == 0 else "нечётное" for x in range(1, 21)]
# print(numbers)

# objects = [42, "строка", [1, 2, 3]]
# iters = [True if type(i) == list or type(i) == str else False for i in objects]
# print(objects)
