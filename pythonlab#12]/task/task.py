import json

# Функція для виведення вмісту JSON файлу на екран
def display_json_content(file_name):
    with open(file_name, 'r') as file:
        content = json.load(file)
        for student in content:
            print(format_student(student))

# Функція для форматування даних про учня у зручний вигляд
def format_student(student):
    formatted_grades = ', '.join([f"{subject}: {grade}" for subject, grade in student['grades'].items()])
    return f"Surname: {student['surname']}, Grades: {formatted_grades}"

# Функція для додавання або видалення нових записів у JSON файлі
def add_or_remove_entry(file_name, new_entry=None, delete_key=None):
    with open(file_name, 'r+') as file:
        data = json.load(file)
        if new_entry:
            data.append(new_entry)
        elif delete_key:
            for entry in data:
                if delete_key in entry:
                    data.remove(entry)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

# Функція для пошуку даних за певним полем у JSON файлі
def search_by_field(file_name, field_name, value):
    with open(file_name, 'r') as file:
        data = json.load(file)
        results = [entry for entry in data if entry.get(field_name) == value]
        return results

# Функція для обчислення середніх оцінок для кожного учня та всього класу
# і визначення учнів, чия середня оцінка вища за середню по класу
def calculate_average_grades(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        class_avg = 0
        for student in data:
            grades_sum = sum(student['grades'].values())
            student['average_grade'] = grades_sum / len(student['grades'])
            class_avg += student['average_grade']
        class_avg /= len(data)
        above_avg_students = [student['surname'] for student in data if student['average_grade'] > class_avg]
        return class_avg, above_avg_students

# Функція для запису результату в інший JSON файл
def write_to_output_file(result, output_file):
    with open(output_file, 'w') as file:
        json.dump(result, file, indent=4)

# Головне меню
def main_menu():
    print("\n==== Main Menu ====")
    print("1. Display JSON content")
    print("2. Add new student")
    print("3. Remove student")
    print("4. Search student by surname")
    print("5. Calculate average grades")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            display_json_content('students.json')
        elif choice == '2':
            surname = input("Enter student's surname: ")
            grades = {}
            for subject in ['math', 'history', 'science', 'english', 'art']:
                grade = int(input(f"Enter {subject} grade: "))
                grades[subject] = grade
            new_student = {"surname": surname, "grades": grades}
            add_or_remove_entry('students.json', new_entry=new_student)
        elif choice == '3':
            surname = input("Enter student's surname to remove: ")
            add_or_remove_entry('students.json', delete_key=surname)
        elif choice == '4':
            surname = input("Enter student's surname to search: ")
            search_results = search_by_field('students.json', 'surname', surname)
            if search_results:
                for student in search_results:
                    print(format_student(student))
            else:
                print("Student not found.")
        elif choice == '5':
            class_avg, above_avg_students = calculate_average_grades('students.json')
            print("Class Average:", class_avg)
            print("Students with above average grades:", above_avg_students)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
