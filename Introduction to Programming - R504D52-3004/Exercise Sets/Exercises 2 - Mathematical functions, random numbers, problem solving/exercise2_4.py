km_outside_urban = float(input("kilometers outside urban area:\n"))
km_inside_urban = float(input("kilometers inside urban area:\n"))
print(f"Consumption: {round((km_outside_urban*5.1/100)+(km_inside_urban*7.5/100),2)} l")