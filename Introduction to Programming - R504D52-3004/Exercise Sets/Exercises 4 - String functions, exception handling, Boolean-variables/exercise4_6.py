temperature = float(input("Current outside temperature: \n"))
humidity = float(input("Humidity percentage: \n"))

freezing = False
heatwave = False
raining = False
hailstorm = False

if temperature < 0:
    freezing = True
    if temperature < -20:
        hailstorm = True
elif temperature > 20:
    heatwave = True

if humidity > 80:
    if temperature < -20:
        hailstorm = True
    else:
        raining = True

print(f"Current temperature is: {temperature} degrees Celsius.")

if freezing:
    print("It's freezing outside.")
if raining:
    print("It's raining.")
    if heatwave:
        print("It's damp and hot.")
elif hailstorm:
    print("There's a hailstorm, be careful!")
elif heatwave:
    print("Heatwave! Remember to hydrate!")
