def unique_words(sentence):
    words = sentence.split()
    words = [word.strip('.,!?;:()[]').lower() for word in words]
    unique_words_set = set(words)
    return unique_words_set

sentence = input("Введіть речення: ")
unique_words_set = unique_words(sentence)
print("Різні слова в реченні:")
for word in unique_words_set:
    print(word)
