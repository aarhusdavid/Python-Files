#writing my own functions
import math

def area(radius_float):
    area_float = math.pi * (radius_float**2)
    return area_float

def circum(radius_float):
    circum_float = math.pi * 2 * radius_float
    return circum_float

def cylinder_vol(radius_cyl, height_cyl):
    vol = math.pi * radius ** 2 * height
    return vol

radius_float = int(input("Enter the radius to find the area and circumference of the circle: "))
radius_cyl = int(input("Enter the radius of the cylinder to find the volume: "))
height_cyl = int(input("Enter the height of the cylinder to find the volume: "))
area1 = area(radius_float)
circum1 = circum(radius_float)
vol1 = cylinder_vol(radius_cyl, height_cyl)
print("area:", area1)
print("circumference:", circum1)
print("volume of cylinder", vol1)
