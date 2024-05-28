N = int(input("Введіть довжину масиву: "))

array = []

for i in range(N):
    element = float(input(f"Введіть елемент масиву [{i+1}]: "))
    array.append(element)

positive_sum = 0
positive_count = 0

for num in array:
    if num > 0:
        positive_sum += num
        positive_count += 1

if positive_count > 0:
    average_positive = positive_sum / positive_count
    print(f"Середнє арифметичне додатніх елементів: {average_positive}")
else:
    print("У масиві немає додатніх елементів.")
