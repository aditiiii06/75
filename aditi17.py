PI = 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))
Volume = PI * radius * radius * height
surface_area = 2 * PI * radius * (radius + height)
print(" The Volume of a Cylinder = %.2f" %Volume)
print("\n The Surface area of a Cylinder = %.2f" %surface_area)