while True:
    try:
        multiplication_table_num = int(input("Which multiplication table would you like to see? (1-10). 0 stops program. \n"))
        if multiplication_table_num==0:
            break
        elif 1 <= multiplication_table_num <= 10:
            for i in range(10):
                print(f"{i+1} * {multiplication_table_num} = {(i+1)*multiplication_table_num}")
        else:
            print('Wrong number format.')
    except ValueError:
        print("Wrong number format.")       \n")
    if ask_user=="n":
        break