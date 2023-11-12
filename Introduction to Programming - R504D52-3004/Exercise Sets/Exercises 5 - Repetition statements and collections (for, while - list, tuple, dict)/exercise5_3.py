import math
while True:
    radius=int(input("Give radius: \n"))
    circle_area = round(math.pi*math.pow(radius,2),2)
    print(f"Circle area: {circle_area}")
    ask_user = input("Do you want to continue? (y/n)\n")
    if ask_user=="n":
        break