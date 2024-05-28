import csv

def load_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

def save_csv(file_path, data, fieldnames):
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Сталася помилка під час запису файлу: {e}")

def print_csv(data):
    for row in data:
        print(row)

def search_countries(data, countries):
    results = [row for row in data if row['\ufeff"Country Name"'] in countries]
    return results

# Основна частина програми
input_file = 'data.csv'
output_file = 'search_results.csv'
data = load_csv(input_file)

if data:
    print("Вміст CSV файлу:")
    print_csv(data)

    countries = input("Введіть назви країн через кому: ").split(',')
    countries = [country.strip() for country in countries]

    search_results = search_countries(data, countries)
    
    if search_results:
        print("\nРезультати пошуку:")
        print_csv(search_results)
        
        fieldnames = data[0].keys()
        save_csv(output_file, search_results, fieldnames)
        print(f"Результати збережено у файл {output_file}")
    else:
        print("Жодна з введених країн не знайдена.")
else:
    print("Не вдалося завантажити дані.")
