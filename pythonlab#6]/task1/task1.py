def reverse_list_and_count():
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()
    reversed_list = lst[::-1]
    count = len(lst)
    
    print("Зворотній список:", reversed_list)
    print("Кількість елементів у списку:", count)

reverse_list_and_count()
