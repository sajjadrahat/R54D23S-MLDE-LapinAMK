import functions

user_input = input("Would you like to read or write into the guestbook? (r/w)\n")

if user_input=="r":
    functions.read_guestbook()
elif user_input=="w":
    functions.write_guestbook()