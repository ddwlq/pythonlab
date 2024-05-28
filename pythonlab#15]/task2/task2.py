import pandas as pd
import matplotlib.pyplot as plt

# Використовуйте сировий рядок для шляху до файлу, щоб уникнути проблем з символами escape
file_path = r'D:\my projects\lab\lab-python\pythonlab#15\pythonlab#15]\data.csv'

# Завантаження даних з локального CSV файлу
data = pd.read_csv(file_path)

# Перевірка правильного зчитування колонок
print(data.head())

# Перетворення дати в формат datetime з параметром dayfirst=True
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Додавання колонки з місяцем
data['Month'] = data['Date'].dt.month

# Вибір колонки для аналізу. Наприклад, 'Berri1' для кількості велосипедистів на цій велодоріжці
bicycles_column = 'Berri1'  # Замініть 'Berri1' на назву колонки, яку хочете аналізувати

# Перевірка наявності обраної колонки
if bicycles_column not in data.columns:
    raise KeyError(f"Column '{bicycles_column}' not found in the dataset")

# Аггрегація даних для підрахунку велосипедистів по місяцях
monthly_counts = data.groupby('Month')[bicycles_column].sum()

# Визначення найпопулярнішого місяця
most_popular_month = monthly_counts.idxmax()
print(f"The most popular month is: {most_popular_month}")

# Побудова графіку
monthly_counts.plot(kind='bar', color='skyblue')
plt.title(f'Monthly Bicycle Counts for {bicycles_column}')
plt.xlabel('Month')
plt.ylabel('Number of Bicycles')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()
