import math

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

hypotenuse = math.sqrt((base **2) + (height **2))

print(f"The hypotenuse of the triangle is {hypotenuse}")