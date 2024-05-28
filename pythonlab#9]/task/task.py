def create_file_TF17_1(filename):
    lines = [
        "Hello1234",
        "Python3.8",
        "2021Year",
        "Code123Code",
        "1234567890"
    ]
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Файл {filename} створено.")
    except IOError as e:
        print(f"Помилка при створенні файлу: {e}")

def process_files(input_file, temp_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(temp_file, 'w') as tempfile:
            digits = ''
            others = ''
            for line in infile:
                for char in line:
                    if char.isdigit():
                        digits += char
                    elif char.isalpha():
                        others += char

            combined = digits + others
            tempfile.write(combined)
        
        with open(temp_file, 'r') as tempfile, open(output_file, 'w') as outfile:
            while True:
                chunk = tempfile.read(10)
                if not chunk:
                    break
                outfile.write(chunk + '\n')
        print(f"Вміст файлів {input_file} переписано у файл {output_file} через файл {temp_file}.")
    except IOError as e:
        print(f"Помилка при обробці файлів: {e}")

def print_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Вміст файлу {filename}:")
            for line in file:
                print(line, end='')
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")

# Виконання завдань
create_file_TF17_1('TF17_1.txt')
process_files('TF17_1.txt', 'TF17_3.txt', 'TF17_2.txt')
print_file_content('TF17_2.txt')
