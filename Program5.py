#Program to calculate area and circumference of circle

from math import pi
radius = 30
_area_of_circle_ = pi*radius*radius                   #calculating area and circumference
_circum_of_circle_ = 2*pi*radius
print('Area of circle with radius 30 is', _area_of_circle_ ,'and circumference of circle with radius 30 is ' , _circum_of_circle_)

r=int(input('Enter radius of circle:'))                #taking radius as input from user
area = pi * r * r

print('Area of circle with radius', r,'is :', area)


