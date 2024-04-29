def print_pattern(N):
    for i in range(N, 0, -1):
        for j in range(N, N - i, -1):
            print(j, end=' ')
        print()

N = int(input("Введіть ціле число N (1<N<9): "))
if 1 < N < 9:
    print_pattern(N)
else:
    print("Введене число не задовольняє умовам.")
