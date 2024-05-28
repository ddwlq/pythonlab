def every_second_element():
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()
    new_list = lst[1::2]
    
    print("Новий список (кожен другий елемент):", new_list)

every_second_element()
