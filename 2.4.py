text = input("Введите строку: ").lower().split()
unique_words = set(text)

for word in sorted(unique_words):
    print(f"{word}: {text.count(word)}")