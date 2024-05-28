import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з .csv файлу
data = pd.read_csv('data.csv')

# Виводимо перший рядок, щоб перевірити стовпчики
print(data.head(1))

# Фільтруємо дані для вибраного індикатора і країн
indicator_name = "Children out of school, primary"  # Назва індикатора
country1 = "Ukraine"
country2 = "United States"

filtered_data = data[(data['Indicator Name'] == indicator_name) &
                     (data['Country Name'].isin([country1, country2]))]

# Перетворюємо дані для побудови графіку
years = [str(year) for year in range(2000, 2024)]  # Вибираємо роки з 2000 по 2023
data_country1 = filtered_data[filtered_data['Country Name'] == country1][years].values.flatten()
data_country2 = filtered_data[filtered_data['Country Name'] == country2][years].values.flatten()

# Побудова графіків
plt.figure(figsize=(14, 7))

# Графік для двох країн
plt.subplot(1, 2, 1)
plt.plot(years, data_country1, label=country1)
plt.plot(years, data_country2, label=country2)
plt.xlabel('Year')
plt.ylabel(indicator_name)
plt.title('Динаміка показника')
plt.legend()

# Стовпчаста діаграма для країн
plt.subplot(1, 2, 2)
selected_country = input('Введіть назву країни для побудови діаграми (Ukraine/United States): ')
if selected_country == country1:
    plt.bar(years, data_country1)
elif selected_country == country2:
    plt.bar(years, data_country2)
else:
    print(f"Неправильна назва країни: {selected_country}")
    exit()

plt.xlabel('Year')
plt.ylabel(indicator_name)
plt.title(f'Стовпчаста діаграма для {selected_country}')

plt.tight_layout()
plt.show()
