import math

x = int(input("Enter your first triangle side: "))
y = int(input("Enter your second triangle side: "))
z = int(input("Enter your third triangle side: "))

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

if is_triangle(x, y, z):
    print("This is a true triangle.")
else:
    print("This is not a true triangle.")
    
def is_right_triangle(a, b, c):
    sides = sorted([x,y,z])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

if is_right_triangle(x, y, z):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")

perimeter = x + y + z
semi = perimeter / 2

def get_area(a, b, c):
    if is_triangle(a, b, c):
        return math.sqrt(semi * (semi - x) * (semi - y) * (semi - z))
    else:
        return 0

sides = sorted([x,y,z])
smallest = sides[0]
medium = sides[1]
largest = sides[2]

print("The perimeter of the triangle is " + str(perimeter))
print("The area of the triangle is " + str(get_area(x, y, z)))
print("Smallest Side: " + str(smallest))
print("Medium Side: " + str(medium))
print("Largest Side: " + str(largest))
