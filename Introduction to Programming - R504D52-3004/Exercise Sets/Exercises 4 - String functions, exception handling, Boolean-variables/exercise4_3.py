# problem (a)
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)
text = text.replace("fox", "duck")
print(text)

# problem (b)
remove_word = input("Which word should be removed?:\n")
if remove_word in text:
    text = text.replace(remove_word,"")
    print(text)
else:
    print("Word not found")

# problem (C)
print(f"{len(text)} characters.")
print(f"{len(text.split())} words.")

# problem (d)
text=text.replace(".","\n")
print(text)

# problem (e)
usertext = input("Write a new sentence:\n")
if len(usertext) > 20:
    usertext = usertext[:20]
    print(f"{usertext}...")
else:
    print(usertext)