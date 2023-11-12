import math
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

#example 1: complex solutions - x^2 + 4x + 5 = 0
#example 2: One solution - x^2 + 2x + 1 = 0
#example 3: Two Real Solution - 6x^2 - 11x + 35 = 0

#calculate the (b^2- 4ac) value to determine the different x values

if  (math.pow(b,2)- (4*a*c))< 0:
    print("no real values")
elif (math.pow(b,2)-4*a*c)==0:
    single_solution = round(-b/(2*a),2)
    print(single_solution)
else:
    first_solution = round( (-b+math.sqrt (math.pow(b,2)-4*a*c)) /(2*a), 2)
    second_solution = round ( (-b-math.sqrt (math.pow(b,2)-4*a*c)) /(2*a), 2)
    print(f"({first_solution}, {second_solution})")