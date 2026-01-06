import module

text = input("Enter text: ")
letter = input("Enter letter to count: ")
print(f"The letter '{letter}' appears {module.count_letter(text, letter)} times in the text.")