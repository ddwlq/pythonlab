# Ініціалізація даних
students_grades = {
    "Ivanov": [9, 8, 7, 6, 10, 8, 7, 8, 9, 6, 7, 8],
    "Petrov": [5, 6, 7, 6, 5, 6, 5, 6, 7, 6, 5, 6],
    "Sidorov": [8, 9, 10, 8, 9, 10, 8, 9, 10, 8, 9, 10],
    "Kuznetsov": [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],
    "Nikolaev": [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9],
    "Smirnov": [9, 10, 8, 9, 10, 8, 9, 10, 8, 9, 10, 8],
    "Popov": [5, 6, 7, 8, 9, 6, 7, 8, 9, 5, 6, 7],
    "Vasiliev": [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8],
    "Kuzmin": [9, 9, 10, 9, 9, 10, 9, 9, 10, 9, 9, 10],
    "Fedorov": [6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8]
}

# Функція для виведення всіх значень словника
def display_all_grades():
    for student, grades in students_grades.items():
        print(f"{student}: {grades}")

# Функція для додавання нового запису
def add_student():
    student_name = input("Enter the student's name: ")
    if student_name in students_grades:
        print(f"Student {student_name} already exists.")
    else:
        try:
            grades = list(map(int, input("Enter the student's grades (12 grades separated by spaces): ").split()))
            if len(grades) != 12:
                print("You must enter exactly 12 grades.")
                return
            students_grades[student_name] = grades
            print(f"Student {student_name} added successfully.")
        except ValueError:
            print("Invalid input. Please enter 12 integer grades.")

# Функція для видалення запису
def remove_student():
    student_name = input("Enter the student's name to remove: ")
    if student_name in students_grades:
        del students_grades[student_name]
        print(f"Student {student_name} removed successfully.")
    else:
        print(f"Student {student_name} does not exist.")

# Функція для перегляду словника за відсортованими ключами
def display_sorted_students():
    for student in sorted(students_grades.keys()):
        print(f"{student}: {students_grades[student]}")

# Функція для визначення середньої оцінки кожного учня
def calculate_average_grades():
    average_grades = {}
    for student, grades in students_grades.items():
        average_grades[student] = sum(grades) / len(grades)
    return average_grades

# Функція для визначення середньої оцінки класу
def calculate_class_average(average_grades):
    total = sum(average_grades.values())
    return total / len(average_grades)

# Функція для виведення прізвищ учнів з середньою оцінкою вище середньої в класі
def display_students_above_class_average():
    average_grades = calculate_average_grades()
    class_average = calculate_class_average(average_grades)
    print(f"Class average: {class_average:.2f}")
    print("Students with above average grades:")
    for student, avg_grade in average_grades.items():
        if avg_grade > class_average:
            print(f"{student}: {avg_grade:.2f}")

# Головна функція для відображення меню та обробки вибору користувача
def main():
    while True:
        print("\nMenu:")
        print("1. Display all students' grades")
        print("2. Add a new student")
        print("3. Remove a student")
        print("4. Display students sorted by name")
        print("5. Display average grades of each student")
        print("6. Display students with above average grades")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            display_all_grades()
        elif choice == '2':
            add_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            display_sorted_students()
        elif choice == '5':
            average_grades = calculate_average_grades()
            for student, avg_grade in average_grades.items():
                print(f"{student}: {avg_grade:.2f}")
        elif choice == '6':
            display_students_above_class_average()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Запуск головної функції
if __name__ == "__main__":
    main()
