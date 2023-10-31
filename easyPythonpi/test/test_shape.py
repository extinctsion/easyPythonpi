import unittest
import math

# Import the function you want to test
from  methods.shape import *
from easyPythonpi import InvalidMeasurementShapeException

class TestShape(unittest.TestCase):
    # Test cases to calculate the perimeter of a circle
    def test_perimeter_circle_radius_zero(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_circle(0)  
    def test_perimeter_circle_radius_invalid(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_circle(-1)  
    def test_perimeter_circle_radius_greater_than_zero(self):
        result = perimeter_circle(10)
        self.assertEqual(round(result,3), 62.840)   

    # Test cases to calculate the area of a circle   
    def test_area_circle_radius_zero(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_circle(0)   
    def test_area_circle_radius_invalid(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_circle(-1)  
    def test_area_circle_radius_greater_than_zero(self):
        result = area_circle(1)
        self.assertEqual(result, 3.142)  

    # Test cases to calculate the volume of a sphere
    def test_volume_sphere_radius_zero(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_sphere(0)  
    def test_volume_sphere_radius_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_sphere(-1)  
    def test_volume_sphere_radius_greater_than_zero(self):
        result = volume_sphere(2)
        self.assertEqual(round(result,3), 100.544) 

    # Test cases to calculate the perimeter of a rectangle  
    def test_perimeter_rectangle_square_length_and_width_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_rectangle_square(-1, -9.9)  
    def test_perimeter_rectangle_square_length_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_rectangle_square(-1,5.51)  
    def test_perimeter_rectangle_square_width_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_rectangle_square(63,-8) 
    def test_perimeter_rectangle_square_length_and_width_positive_num(self):
        result = perimeter_rectangle_square(5, 3)
        self.assertEqual(result, 16)

    # Test cases to calculate the area of a rectangle   
    def test_area_rect_square_with_positive_length_and_width(self):
        self.assertEqual(area_rectangle_square(9.9, 3.7), 36.63)
    def test_area_rect_square_with_zero_length(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_rectangle_square(0, 3)
    def test_area_rect_square_with_zero_width(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_rectangle_square(5, 0)
    def test_area_rect_square_with_negative_length(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_rectangle_square(-5, 3)
    def test_area_with_negative_width(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_rectangle_square(5, -3) 

    # Test cases to calculate the perimeter of a triangle    
    def test_perimeter_triangle_with_positive_sides(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
    def test_perimeter_triangle_with_zero_side1(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(0, 4, 5)
    def test_perimeter_triangle_with_zero_side2(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(3, 0, 5)
    def test_perimeter_triangle_with_zero_side3(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(3, 4, 0)
    def test_perimeter_triangle_with_negative_side1(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(-3, 4, 5)
    def test_perimeter_triangle_with_negative_side2(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(3, -4, 5)
    def test_perimeter_triangle_with_negative_side3(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            perimeter_triangle(3, 4, -5)    

    #test cases to find area of a triangle
    def test_area_triangle_valid_lengths(self):
        # Test for an equilateral triangle
        result = area_triangle(67, 4)
        self.assertEqual(result, (67 * 4) / 2)
    def test_area_triangle_zero_base(self):
        # Test with a zero side length
        with self.assertRaises(InvalidMeasurementShapeException):
            area_triangle(0, 4)    
    def test_area_triangle_negative_base_length(self):
        # Test with a negative side length
        with self.assertRaises(InvalidMeasurementShapeException):
            area_triangle(-99, 4) 
    def test_area_triangle_zero_height_length(self):
        # Test with a zero side length
        with self.assertRaises(InvalidMeasurementShapeException):
            area_triangle(4, 0)    
    def test_area_triangle_negative_height_length(self):
        # Test with a negative side length
        with self.assertRaises(InvalidMeasurementShapeException):
            area_triangle(5, -47) 

    # Test cases to find the volume of a pyramid
    def test_volume_pyramid_valid_dimensions(self):
        result = volume_pyramid(4, 6, 3)
        self.assertEqual(result, 24.0) 
    def test_volume_pyramid_zero_length(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(0, 6, 3)      
    def test_volume_pyramid_negative_length(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(-76, 6, 3)  
    def test_volume_pyramid_zero_width(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(55, 0, 12)  
    def test_volume_pyramid_negative_width(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(55, -99, 12)  
    def test_volume_pyramid_zero_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(55, 49, 0)  
    def test_volume_pyramid_negative_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_pyramid(55, 49, -77)

    # test cases to find the volume of a cone
    def test_volume_cone_valid_dimensions(self):
        result = volume_cone(2, 9.5)
        self.assertEqual(round(result,3), 39.799)     
    def test_volume_cone_zero_radius(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cone(0, 49)
    def test_volume_cone_negative_radius(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cone(-10, 49)
    def test_volume_cone_negative_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cone(77, -33) 
    def test_volume_cone_zero_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cone(212, 0)   

    # test cases to find the volume of a cylinder
    def test_volume_cylinder_valid_dimensions(self):
        result = volume_cylinder(8, 10.99)
        self.assertEqual(round(result,3), 2209.957) 
    def test_volume_cylinder_zero_radius(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cylinder(0, 49)
    def test_volume_cylinder_negative_radius(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cylinder(-10, 49)
    def test_volume_cylinder_negative_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cylinder(77, -33) 
    def test_volume_cylinder_zero_height(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            volume_cylinder(212, 0)

    # test cases to find the area of a cone
    def test_area_cone_valid_dimensions(self):
        result = area_cone(25, 4.99)
        self.assertEqual(round(result,3), 3966.236) 
    def test_area_cone_radius_zero(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_cone(0, 5)
    def test_area_cone_radius_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_cone(4, -5) 
    def test_area_cone_height_zero(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_cone(5, 0)
    def test_area_cone_height_negative(self):
        with self.assertRaises(InvalidMeasurementShapeException):
            area_cone(4, -99) 
