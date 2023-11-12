rain_amount=0
for i in range(12):
    amount=int(input("Give rain amount of month: \n"))
    rain_amount+=amount
avg_rain=round(rain_amount/12,2)
print(f"Year average for rain = {avg_rain} mm")