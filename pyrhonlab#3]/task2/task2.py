def count_underscores(word):
    count = word.count('_')
    return count

word = input("Введіть слово: ")
underscore_count = count_underscores(word)
if underscore_count > 0:
    print(f"Символи «_» є в слові, їх кількість: {underscore_count}")
else:
    print("Символів «_» немає в слові")
