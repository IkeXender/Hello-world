Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
>>> radius = float(input("Enter the radius: "))
Enter the radius: 5
>>> diameter = 2 * radius
>>> circumference = 2 * math.pi * radius
>>> surface_area = 4 * math.pi * radius ** 2
>>> volume = (4 / 3) * math.pi * radius ** 3
>>> 
>>> print("Diameter:", diameter)
Diameter: 10.0
>>> print("Circumference:", circumference)
Circumference: 31.41592653589793
>>> print("Surface Area:", surface_area)
Surface Area: 314.1592653589793
>>> print("Volume:", volume)
Volume: 523.5987755982989
