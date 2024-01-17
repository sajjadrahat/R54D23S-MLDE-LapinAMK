user_text = input("Give some text: \n").lower()
reverse_text = user_text[::-1]
print(reverse_text)

if user_text == "":
    print("Your text is empty")
elif user_text == reverse_text:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
