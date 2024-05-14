def second_function(n):
    # Обчислення суми факторіалів
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, n + 1):
        factorial *= i
        sum_of_factorials += factorial

    return sum_of_factorials