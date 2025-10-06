# 1. Создание переменных и вывод значений
# name = "Vitaliy"
# # age = 35
# height = 175.5
from operator import truediv
from tkinter.font import names

# print("Имя", name)
# print("Возраст", age)
# print("Рост", height)

# 2. Изменение значений переменных
# x = 10
# print("Значение 1 :", x)
# print("Тип переменной :", type(x))
#
# x = 25.5
# print("Новое значение 2 :", x)
# print("Тип переменной :", type(x))
#
# x = "Python"
# print("Новое значение 3 :", x)
# print("Тип переменной :", type(x))
# print(x)

# 3. Копирование ссылок
# a = 7
# b = a
# print(a)
# print(b)
# # "b = a, мы не копируем значение, а создаем новую ссылку на тот же объект в памяти"
#
# a = 10
# print(a)
# print(b)
# # когда мы выполняем a = 10,cоздается новый объект со значением 10 Переменная a теперь ссылается на этот новый объект
# #а переменная b по-прежнему ссылается на старый объект со значением 7 это наверное можно еще проверить по ID
# print(id(a))
# print(id(b))

# 4. Каскадное присваивание

# x = y = z = 100
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))
# # ID Одинаковые

# x, y, z, = 1, 2, 3,
# print(id(x))
# print(id(y))
# print(id(z))
# # ID Разные

#  Обмен значений переменных
# a = 5
# b = 10
# print("a=", a)
# print("b=", b)
#
# a, b = b, a
# print("a=", a)
# print("b=", b)


# Работа с именами переменных
# Нельзя использовать зарезервированные слова

# # 7. Использование функции type()
#
# var_1 = 10
# var_2 = 3.14
# var_3 = "Hello"
#
# print(type(var_1))
# print(type(var_2))
# print(type(var_3))
# # После присвоения Var_1 строкового значения она стала str а до была int


# 8. Дополнительные задания
name = "Vitaliy"
age = 35
height = 175.5
weight = 90
car = "BMW"
приветики = 10
print(type(name))
print(type(age))
print(type(height))
print(type(weight))
print(type(приветики))
# как мы видим переменная с ру именем работает но это не совсем корректно )
