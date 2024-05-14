import math
from factorial import second_function

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

def main():
    first_function()
    
    # Виклик функції second_function з модуля factorial
    n = int(input("Введіть натуральне число n: "))
    sum_of_factorials = second_function(n)
    print("Сума факторіалів:", sum_of_factorials)

if __name__ == "__main__":
    main()
