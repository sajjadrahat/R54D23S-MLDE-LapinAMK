temperature= int(input("Give the temperature: \n"))
if temperature >= 0 and temperature <=10:
    print("COLD")
elif temperature >= 11 and temperature <=15:
    print("CHILLY")
elif temperature >= 16 and temperature <=20:
    print("NORMAL TEMPERATURE")
elif temperature >= 21 and temperature <=25:
    print("WARM")
elif temperature >= 26 and temperature <=30:
    print("HOT")
else:
    pass