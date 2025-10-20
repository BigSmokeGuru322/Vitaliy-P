# sqare = lambda x: x ** 2
# print(sqare(3))
# print(sqare(5))
# print(sqare(3))
# print(sqare(-4))
# print(sqare(2.5))
#
#
# even_number = lambda x: x % 2 == 0
# print(even_number(4))
# print(even_number(7))
# print(even_number(0))
# print(even_number(-2))
# print(even_number(-3))

# words = ["banana", "apple", "cherry"]
# sort_by_last_letter = sorted(words, key=lambda x: x[-1])
# print(sort_by_last_letter)

# def multiply_by(n):
#     def multiplicate(x):
#         return x * n
#     return multiplicate
# times3 = multiply_by(3)
# times5 = multiply_by(5)
# print(times3(10))
# print(times5(10))

# def counter(start=0):
#     res = start
#     def update_counter():
#         nonlocal res
#         res += 1
#         return res
#     return update_counter
#
# c1 = counter(5)
# c2 = counter()
#
# print(c1())
# print(c1())
# print(c2())
# print(c2())