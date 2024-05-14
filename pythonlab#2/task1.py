import math

def first_function():
    # Введення чисел a і b
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))

    # Обчислення значення виразу
    z = math.sin(2*a) + math.cos(2*b)
    if a >= 15:
        z = math.sqrt(a + b**2)

    # Виведення результату
    print("Значення виразу:", z)

def second_function():
    # Введення числа n
    n = int(input("Введіть натуральне число n: "))

    # Обчислення суми факторіалів
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, n + 1):
        factorial *= i
        sum_of_factorials += factorial

    # Виведення результату
    print("Сума факторіалів:", sum_of_factorials)

first_function()
second_function()
