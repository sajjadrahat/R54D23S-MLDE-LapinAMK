year= int(input("Give Year: \n"))
leap_year= False

if year%400==0:
    leap_year = True
else:
    if year%100==0:
        pass
    elif year%4==0:
        leap_year = True
if leap_year==True:
    print("Leap year: YES")
else:
    print("Leap year: NO")