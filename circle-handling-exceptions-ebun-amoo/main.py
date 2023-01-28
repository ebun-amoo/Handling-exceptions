
# please add your code here
import math
try:
    radius = input("Please enter the radius of a circle: ")
    radius = float(radius)
    Area = math.pi * radius * radius
    print(f'Area is {Area}')
except: 
    print('not a number')