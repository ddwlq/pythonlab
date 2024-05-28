import pandas as pd

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

# Створення датафрейму з використанням бібліотеки Pandas
df = pd.DataFrame(students_grades)
df = df.T  # Транспонування для кращої читабельності
df.columns = [f"Month_{i+1}" for i in range(df.shape[1])]  # Додавання заголовків стовпців

# Виведення датафрейму на екран
print("DataFrame:")
print(df)

# Додавання колонки із середнім балом кожного учня
df['Average'] = df.mean(axis=1)

# Виведення датафрейму з середніми оцінками на екран
print("\nDataFrame with Averages:")
print(df)

# Групування даних по середньому балу (наприклад, вище або нижче середнього)
class_average = df['Average'].mean()
print(f"\nClass Average: {class_average:.2f}")

above_average_students = df[df['Average'] > class_average]
print("\nStudents with above average grades:")
print(above_average_students)

below_average_students = df[df['Average'] <= class_average]
print("\nStudents with below average grades:")
print(below_average_students)
