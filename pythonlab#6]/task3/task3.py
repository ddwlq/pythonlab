def unique_characters():
    text = input("Введіть текст латинськими літерами: ")
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    unique_chars = {char for char, count in char_count.items() if count == 1}
    
    print("Символи, які входять у текст один раз:", unique_chars)

unique_characters()
