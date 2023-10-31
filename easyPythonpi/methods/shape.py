#!/usr/bin/env python
#-*- coding: utf-8 -*-

import easyPythonpi as pi
import regex as re
import math

# To find the perimeter of a circle using the radius r
def perimeter_circle(r:'float')->'float': 
    if r <= 0:
        raise pi.InvalidMeasurementShapeException(r)
    PI = 3.142
    return 2 * PI * r 

# To find the area of a circle using the radius r
def area_circle(r:'float')->'float':  
    if r <= 0:
        raise pi.InvalidMeasurementShapeException()
    PI = 3.142
    return PI * (r * r)

# To find the volume of a sphere using the radius r
def volume_sphere(r:'float')->'float': 
    if r <= 0:
        raise pi.InvalidMeasurementShapeException()    
    PI = 3.142
    return 4 * PI * (r**3) 

# To find the perimeter of a rectangle using the length and width
def perimeter_rectangle_square(length:'float', width:'float')->'float': 
    if length <= 0 or width <= 0:
        raise pi.InvalidMeasurementShapeException() 
    return (2 * length) + (2 * width)

def area_rectangle_square(length:'float', width:'float')->'float': 
    if length <= 0 or width <= 0:
        raise pi.InvalidMeasurementShapeException()     
    return length * width

# To find the perimeter of a rectangle using the length and width
def perimeter_triangle(side1:'float', side2:'float', side3:'float')->'float': 
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise pi.InvalidMeasurementShapeException()     
    return side1 + side2 + side3

def area_triangle(base:'float', height:'float')->'float': 
    if base <= 0 or height <= 0:
        raise pi.InvalidMeasurementShapeException()  
    return (base * height) / 2

# To find the volume of a pyramid with length and width of base and height of pyramid
def volume_pyramid(length:'float', width:'float', height:'float')->'float': 
    if length <= 0 or width <= 0 or height <= 0:
        raise pi.InvalidMeasurementShapeException()      
    return (length * width * height) / 3

# To find the volume of a cylinder with radius of the cylinder base and height of the cylinder
def volume_cylinder(radius:'float', height:'float')->'float': 
    if radius <= 0 or height <= 0:
        raise pi.InvalidMeasurementShapeException() 
    PI = 3.142
    return PI * (radius**2) * height

# To find the area of a cone with length and width of base and height of pyramid
def area_cone(radius:'float', height:'float')->'float': 
    if radius <= 0 or height <= 0:
        raise pi.InvalidMeasurementShapeException() 
    PI = 3.142
    return ((PI * radius) * (radius + (math.sqrt(height**2 + radius**2))))

# To find the volume of a cone with length and width of base and height of pyramid
def volume_cone(radius:'float', height:'float')->'float': 
    if radius <= 0 or height <= 0:
        raise pi.InvalidMeasurementShapeException()    
    PI = 3.142
    return ( PI * (radius**2) * height ) / 3

