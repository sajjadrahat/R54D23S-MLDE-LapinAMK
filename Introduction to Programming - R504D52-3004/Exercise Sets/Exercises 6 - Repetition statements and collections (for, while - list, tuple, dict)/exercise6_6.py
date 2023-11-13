basket = ["apple", "banana", "cherry", "carrot", "potato", "tomato", "cabbage"]
user_word =input("Which word to ignore? \n")

if user_word.isnumeric():
    user_word = basket[int(user_word)-1]
if user_word not in basket:
    print("Word not found.")
else:
    for word in basket:
        if word == user_word:
            continue
        else:
            print(word)