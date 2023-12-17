def read_guestbook():
    with open('guestbook.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                print(line.strip())

def write_guestbook():
    message = input("Write a new message: \n")
    # Using 'a' to append message in txt file.
    with open('guestbook.txt', 'a') as file:
        file.write(message + '\n')

user_input = input("Would you like to read or write into the guestbook? (r/w)\n")

if user_input=="r":
    read_guestbook()
elif user_input=="w":
    write_guestbook()