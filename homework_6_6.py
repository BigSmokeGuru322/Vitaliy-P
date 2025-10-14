# """
# ++++++++++++++++++++++++++++++++++++++++++++++++
# Условный оператор
# ++++++++++++++++++++++++++++++++++++++++++++++++
# #1. Проверка знака числа
x = float(input("Введите x: "))
if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

#2. Проверка на четность
x = int(input("Введите целое число x: "))
if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

#3. Определение диапазона
x = float(input("Введите x: "))
if 1 <= x <= 10:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")

#4. Перестановка двух чисел
a = float(input("Введите число а: "))
b = float(input("Введите число b: "))
if a < b:
    a, b = b, a
print(a, b)

#5. Поиск минимума из двух чисел
a = float(input("Введите число а: "))
b = float(input("Введите число b: "))
if a > b:
    print(b)
else:
    print(a)

#6. Проверка наличия элемента в списке
marks = [3, 4, 5, 2, 5, 4]
if 2 in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")

#7. Проверка делимости
x = float(input("Введите x: "))
if x % 3 == 0 and x % 5 == 0:
    print("Число делится на 3 и 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
else:
    print("Число не делится на 3 и 5")

#8. Оператор in для проверки пароля
password = input("Введите пароль: ")
if password == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#9. Калькулятор скидки
amount = float(input("Введите сумму покупки: "))
if amount >= 5000:
    print(amount * 0.9)
else:
    if  1000 <= amount < 5000:
        print(amount * 0.95)
    else:
        print(amount)

#10. Определение високосного года
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0):
    (print("Год високосный"))
elif (year % 400 == 0):
    (print("Год високосный"))
else:
    print("Год не високосный")
# Вложенные условия и elif
#1. Проверка оценки
evaluations = int(input("Введите оценку: "))
if evaluations == 5:
    print("Отлично!")
elif evaluations == 4:
    print("Хорошо")
elif evaluations == 3:
    print("Удовлетворительно")
elif evaluations == 2 or evaluations == 1:
    print("Неудовлетворительно")
else:
    print("Некорректная оценка")

#2. Определение времени суток по часам
time = int(input("Введите время: "))
if 6 <= time <= 11:
    print("Утро")
elif (12 <= time <= 17):
    print("День")
elif 18 <= time <= 21:
    print("Вечер")
elif 22 <= time <= 23 or 0 <= time <= 5:
    print("Ночь")
else:
    print("Некорректное время")

#3. Классификация температуры
temp = int(input("Введите температуру: "))
if temp < -10:
    print("Очень холодно")
elif (-10 <= temp <= 0):
    print("Холодно")
elif 1 <= temp <= 10:
    print("Прохладно")
elif 11 <= temp <= 25:
    print("Тепло")
else:
    print("Жарко")

#4. Проверка года на високосность
year1 = int(input("Введите год: "))
if (year1 % 4 == 0 and year1 %100 != 0) or year1 % 400 == 0:
    print("Год високосный")
else:
    print("Год не високосный")

#5. Калькулятор двух чисел
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
sign = input("Введите операцию (+, -, *, /): ")
if sign == "+":
    print(x + y)
elif sign == "-":
    print(x - y)
elif sign == "*":
    print(x * y)
elif sign == "/":
    if y != 0:
        print(x / y)
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Некорректная операция")


#1. Проверка четности числа
x = int(input("Введите число: "))
res = "Число четное" if x % 2 == 0 else "Число нечетное"
print(res)

#2. Определение наибольшего числа
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
res = x if x > y else y
print(res)

#3. Проверка положительного или отрицательного числа
x = float(input("Введите число: "))
res =  "Число положительное" if x > 0 else "Число отрицательное" if x < 0 else "Число равно нулю"
print(res)

#4. Определение возраста для входа в клуб
age = int(input("Введите свой возраст: "))
access = "Вход разрешен" if age >= 18 else "Вход запрещен"
print(access)

#5. Определение скидки в магазине
summa_pokupki_1 = float(input("Введите сумму покупки: "))
full = summa_pokupki_1 * 0.9 if summa_pokupki_1 >= 5000 else summa_pokupki_1
print(full)