from emojis import emoji_dict

sentence = input("Enter a sentence: ")

words = sentence.split()
translated = []

for word in words:
    translated.append(emoji_dict.get(word.lower(), word))

print("\nResult:")
print(" ".join(translated))
