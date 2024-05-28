import matplotlib.pyplot as plt

grades_data = {
    'Johnson': {'math': 75, 'history': 80, 'science': 78, 'english': 82, 'art': 80},
    'Jones': {'math': 80, 'history': 75, 'science': 82, 'english': 78, 'art': 80},
    'Davis': {'math': 88, 'history': 85, 'science': 90, 'english': 86, 'art': 89},
    'Wilson': {'math': 78, 'history': 85, 'science': 80, 'english': 82, 'art': 79},
    'Taylor': {'math': 90, 'history': 92, 'science': 88, 'english': 91, 'art': 89}
}

average_grades = {name: sum(grades.values()) / len(grades) for name, grades in grades_data.items()}

plt.figure(figsize=(6, 6))
plt.pie(average_grades.values(), labels=average_grades.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Середні оцінки студентів')
plt.axis('equal') 
plt.show()
