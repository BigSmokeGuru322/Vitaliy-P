# def greet(name):
#     print(f"Привет, {name}! Добро пожаловать!")
# greet("Анна")

# def square(num):
#     res = (num ** 2)
#     return res
# print(square(10))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(7))
# print(is_even(4))

# def add(a, b):
#     res = a + b
#     return res
# print(add(12, 8))

# def get_max(a, b, c):
#     res = max(a, b, c)
#     return res
# print(get_max(10, 25, 7))

# def calculate(a, b, operation):
#    if operation == "+":
#        return a + b
#    elif operation == "-":
#        return a - b
#    elif operation == "*":
#        return a * b
#    elif operation == "/":
#        return a / b
# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "*"))

# def reverse_string(text):
#     reverse = text [::-1]
#     return reverse
# print(reverse_string("Python"))

# def compare_strings(s1, s2, ignore_case = True, ignore_spaces = True):
#     if ignore_case and ignore_spaces:
#         return s1.replace(" ", "").lower() == s2.replace(" ", "").lower()
#     elif ignore_case and not ignore_spaces:
#         return s1.lower() == s2.lower()
#     elif not ignore_case and ignore_spaces:
#         return s1.replace(" ", "") == s2.replace(" ", "")
#     else:
#         return s1 == s2
# print(compare_strings("Hello", " hello "))  # True
# print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
# print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False

# def summarize(*args):
#     total = 0
#     for item in args:
#         if isinstance(item, (int, float)) and not isinstance(item, bool):
#             total += item
#     return total
#
# print(summarize(1, 2, 3))
# print(summarize(10, "abc", 5, 2))
# print(summarize(1.5, 2.5, "xyz"))
# print(summarize("a", "b", "c"))
# print(summarize())

# def create_profile(name, age, **extra):
#     print("Профиль пользователя:")
#     print("Имя: ", name)
#     print("Возраст: ", age)
#     for key, value in extra.items():
#         print(f"{key}: {value}")
# create_profile("Иван", 30, city="Москва", job="Инженер")

# def process_orders(*orders, discount=0):
#     total_sum = sum(orders)
#     discount_sum = total_sum * (1 - discount / 100)
#     print(f"Сумма заказа: {total_sum}")
#     print(f"С учетом скидки: {int(discount_sum)}")
#     return ""
# print(process_orders(100, 200, 300, discount=10))

# def merge_lists(*lists):
#     result = []
#     for lst in lists:
#         if isinstance(lst, list):
#             result.extend(lst)
#     return result
#
# print(merge_lists([1, 2], [3, 4], [5, 6]))
# # Вывод: [1, 2, 3, 4, 5, 6]
#
# print(merge_lists([1, 2], "not a list", [3, 4]))
# # Вывод: [1, 2, 3, 4] (строка "not a list" игнорируется)
#
# print(merge_lists())
# # Вывод: [] (пустой вызов возвращает пустой список)
#
# print(merge_lists([], [1], [2, 3]))
# # Вывод: [1, 2, 3] (пустой список корректно обрабатывается)


# def merge_dicts(*dicts):
#     result = {}
#     for i in dicts:
#         result.update(i)
#     return result
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# d3 = {"c": 5, "d": 6}
# print(merge_dicts(d1, d2, d3))
