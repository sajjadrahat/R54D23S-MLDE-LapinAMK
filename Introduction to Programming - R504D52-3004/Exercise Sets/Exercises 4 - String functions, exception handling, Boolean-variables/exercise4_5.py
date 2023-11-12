special_price = False
student=input("Are you a student? (y/n)\n")
travel_month = int(input("Travel month? (1-12)\n"))

if student == "y" and not (6 <= travel_month <= 8):
    special_price = True


if special_price:
    print("Special price!")
else:
    print("Normal price.")
