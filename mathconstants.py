import math


print(math.pi)

print(math.e)

print(math.sqrt(25))

print(math.ceil(9.1)) #round up = 10
print(math.floor(9.1)) #round down = 9


#circumference
radius = float(input("Enter radius: "))

circumference = 2 * math.pi * radius
print("The circumference is",circumference)
print("The circumference is", round(circumference, 2))

#circle area
circle_area = math.pi * pow(radius, 2)
print(f"The area is: {round(circle_area,2)} cm^2")

