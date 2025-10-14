# # Задачи по уроку "Цикл while"
# # ++++++++++++++++++++++++++++++++++++++++++++++++
# # ===============================================
# # # 1. Вывод чисел от 1 до N
# # n = int(input("Введите число N: "))
# # i = 1
# # while i <= n:
# #     print(i)
# #     i += 1
#
# #2. Сумма четных чисел до N
# # n = int(input("Введите число N: "))
# # sum = 0
# # i = 1
# # while i <= n:
# #     if i % 2 == 0:
# #         sum += i
# #     i += 1
# # print(sum)
#
# #3. Подсчет количества цифр в числе
# # num_x = input("Введите натуральное число: ")
# # i = 0
# # while i < len(num_x):
# #     i += 1
# # print("количество цифр в указанном числе: ", i)
#
# #4. Определение максимальной цифры в числе
#
# # num_z = int(input("Введите натуральное число: "))
# # i = 0
# # max_len = 0
# # max_num = list(str(num_z))
# # while i < len(max_num):
# #     current_value = int(max_num[i])
# #     if current_value > max_len:
# #         max_len = current_value
# #     i += 1
# # print(max_len)
#
# #5. Запрос пароля
# # correct_password = "pass123"
# # password = input("Enter your password: ")
# # while password != correct_password:
# #     print("Wrong password")
# #     password = input("Enter your password: ")
# # print("Access granted")
#
# # Задачи по уроку "Операторы break, continue и else в цикле while"
# #1. Поиск первого четного числа
#
# numbers = [23, 33, 45, 76, 32, 77, 89 ]
# founders = False
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print("Первое четное число равно: ", numbers[i])
#         founders = True
#         break
#     i += 1
#     if founders == False:
#         print("Четное число не найдено ")
#
# #2. Пропуск отрицательных чисел
# # num = 1
# # result_sum = 0
# # while num != 0:
# #    num = int(input("Введите целое число или 0 для выхода: "))
# #    if num > 0:
# #        result_sum = result_sum + num
# #    else:
# #        continue
# # print(result_sum)
#
# #3. Вывод нечетных чисел из диапазона
# # a = int(input("Введите число а: "))
# # b = int(input("Введите число b: "))
# # x = a
# # result = []
# # if a <= b:
# #     while x <= b:
# #         if x % 2 == 0:
# #             x += 1
# #             continue
# #         result.append(x)
# #         x += 1
# # else:
# #     while x >= b:
# #         if x % 2 == 0:
# #             x -= 1
# #             continue
# #         result.append(x)
# #         x -= 1
# # print(result)
#
# #4. Проверка на простое число
# # N = int(input("Введите число N: "))
# # num_1 = 2
# # count = 1
# # result = ""
# # while num_1 <= N:
# #     if N % num_1 == 0:
# #         count += 1
# #         if count > 2:
# #             break
# #     num_1 += 1
# # if count == 2:
# #     result = "Число простое"
# # else:
# #     result = "Число не является простым"
# # print(result)
#
# #5. Поиск максимального числа
#
# # num = 1
# # res_sum = []
# # while num != 0:
# #    num = input("Введите целое число или 0 для выхода: ")
# #    if num == "":
# #        result = ("Введено пустое значение: ")
# #        break
# #    num = int(num)
# #    if num != 0:
# #        res_sum.append(num)
# #        result = max(res_sum)
# #    else:
# #        continue
# # print(result)
#
# #1. Вывести все символы строки в обратном порядке
# # result = []
# # stoka = input("Введите строку: ")
# # for i in range(len(stoka) - 1, -1, -1):
# #     result.append(stoka[i])
# # print(result)
#
# #2.Замена четных элементов списка на 0
# # shopping_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # for i in range(len(shopping_list)):
# # #     if shopping_list[i] % 2 == 0:
# # #         shopping_list[i] = 0
# # # print(shopping_list)
#
# #3. Генерация списка степеней двойки
# # N = int(input("Введите число N: "))
# # result = []
# # for i in range(0, N +1, 1):
# #     result.append(2 ** i)
# # print(result)
#
# #4. Вывод всех чисел от A до B с шагом K
A = int(input("Введите А: "))
B = int(input("Введите B: "))
K = int(input("Введите K: "))
result = []
for i in range(A, B + 1, K):
    result.append(i)
print(result)