import functions

user_input = int(input(
    "How do you want to input the time?\n"
    "-Type: 1 for a single line input (e.g., '2h 45min 33sec')\n"
    "-Type: 2 for separate lines input (hours, minutes, seconds)\n"
))

if user_input==1:
    user_time= input("Give time: \n")
    # making a list
    user_time = user_time.split(" ")
    # Getting the hours, minutes, seconds using slicing from the list 
    hours = int(user_time[0][:-1])
    minutes = int(user_time[1][:-3])
    seconds = int(user_time[2][:-3])
elif user_input==2:
    hours=int(input("Give hours: \n"))
    minutes=int(input("Give minutes: \n"))
    seconds=int(input("Give seconds: \n"))

returned_val = functions.count_seconds(hours, minutes, seconds)

print(returned_val)