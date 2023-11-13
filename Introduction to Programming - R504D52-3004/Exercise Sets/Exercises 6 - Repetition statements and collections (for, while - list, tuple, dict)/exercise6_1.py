max_num = 0
for i in range(5):
    try:
        user_input=int(input("Give a number: \n"))
        if user_input>0 and user_input>max_num:
            max_num = user_input
    except ValueError:
        print("user_input")

print(f"The biggest number from user: {max_num}")