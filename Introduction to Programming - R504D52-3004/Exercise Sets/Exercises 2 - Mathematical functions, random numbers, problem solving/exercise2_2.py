import math
first_leg = float(input("Give me the first leg:\n"))
second_leg= float(input("Give me the second leg:\n"))
print(f"Hypotenuse: {round(math.sqrt(math.pow(first_leg,2)+(math.pow(second_leg,2))),2)} m")