# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы
# оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# (*) Усложнение. Решите для числа произвольной разрядности: произвольное
# количество цифр в числе.
# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку
# с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
# Совет: Для этого используйте конкатенацию строк и срезы


# ------------------
# трехзначное число

# number = int(input("Введите трехзначное число: "))
# num1 = number // 100 % 10
# num2 = number // 10 % 10
# num3 = number % 10
# summa = num1 + num2 + num3
# print(f"Сумма чисел числа {number} равна {summa}")


# ------------------
# число произвольной разрядности

# number = int(input("Введите число: "))
# num = number
# summa = 0
# while num > 0:
#     summa += num % 10
#     num = num // 10
# else:
#     summa += num % 10
# print(f"Сумма чисел числа {number} равна {summa}"


# ------------------
# число произвольной разрядности с перечисленными складываемыми числами

# number = int(input("Введите число "))
# num = number
# summa = 0
# strDigit = ""
# while num > 0:
#     digit = num % 10
#     summa = digit + summa
#     num //= 10
#     strDigit = f"{digit} + {strDigit}"
# print(f"Сумма чисел числа {number} = {summa} ({strDigit[:-3]})")
