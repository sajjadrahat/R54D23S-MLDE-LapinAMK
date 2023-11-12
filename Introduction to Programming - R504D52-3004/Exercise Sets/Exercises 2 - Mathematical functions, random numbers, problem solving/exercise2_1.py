import math
#Box Volume
first_slide= float(input("Give me the first slide:\n"))
second_slide= float(input("Give me the second slide:\n"))
third_slide= float(input("Give me the third slide:\n"))
print(f"Box Volume: {round(first_slide*second_slide*third_slide,2)} m3")

#Sphere Volume
sphere_radius= int(input("Give me the sphere radius:\n"))
print(f"Box Volume: {round(4/3*math.pi*math.pow(sphere_radius,3),2)} m3")