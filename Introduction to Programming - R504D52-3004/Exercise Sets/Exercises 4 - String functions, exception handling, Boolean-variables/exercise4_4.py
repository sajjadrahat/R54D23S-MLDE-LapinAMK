try:
    first_num = float(input("First number:\n"))
    second_num = float(input("Second number:\n"))
    print(first_num/second_num)

except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Incorrect format.")


