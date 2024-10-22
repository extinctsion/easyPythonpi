
"""  A python module that helps you to calculate some of the  most used calculations.....
    usage--
            Just download the file from git and unzip in ur system.
            And while using this module, just write as code-
            'from easypythonpi import *' and u r good to go...
                            ~Happy programming"""
                        

# Programmer defined exceptions go here:

# define exception for invalid Binary Strings  

# class InvalidBinaryException(Exception):
#     pass

# class InvalidNumberFibException(Exception):
#     def __init__(self, n, message="n is not valid, must be greater than or equal to 1"):
#          self.n = n
#          self.message = message
         
# class InvalidMeasurementShapeException(Exception):
#     def __init__(self, message="invalid measurement, must be greater than or equal to 0"):
#         self.message = message

"""This Python module, easypythonpi.py, is designed to help with a variety of common calculations, including basic arithmetic operations, binary-to-decimal conversion, Fibonacci sequence generation, and shape area calculations. It is built with simplicity and ease of use in mind, making it ideal for both beginners and intermediate users. The module also includes custom exceptions to handle invalid inputs gracefully."""


# Define exception for invalid binary strings
class InvalidBinaryException(Exception):
    """Raised when an invalid binary string is provided."""
    pass

# Define exception for invalid Fibonacci numbers
class InvalidNumberFibException(Exception):
    """Raised when the Fibonacci number is invalid."""
    def __init__(self, n, message="n is not valid, must be greater than or equal to 1"):
        self.n = n
        self.message = message
        super().__init__(self.message)

# Define exception for invalid measurements for shapes
class InvalidMeasurementShapeException(Exception):
    """Raised when invalid measurement values are provided for shapes."""
    def __init__(self, message="Invalid measurement, must be greater than or equal to 0"):
        self.message = message
        super().__init__(self.message)

# Functions for basic calculations

def add(num1, num2):
    """Add two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Subtract two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Divide two numbers with error handling for division by zero."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Binary string to decimal conversion
def binary_to_decimal(binary_str):
    """Convert binary string to decimal."""
    try:
        # Check if the binary string is valid
        if not set(binary_str).issubset({'0', '1'}):
            raise InvalidBinaryException(f"Invalid binary string: {binary_str}")
        return int(binary_str, 2)
    except InvalidBinaryException as e:
        return str(e)

# Fibonacci sequence generator
def fibonacci(n):
    """Generate Fibonacci sequence up to the nth number."""
    if n < 1:
        raise InvalidNumberFibException(n)
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Shape area calculators

def calculate_circle_area(radius):
    """Calculate the area of a circle given the radius."""
    if radius < 0:
        raise InvalidMeasurementShapeException("Radius must be non-negative.")
    return 3.14159 * radius * radius

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    if length < 0 or width < 0:
        raise InvalidMeasurementShapeException("Length and width must be non-negative.")
    return length * width

def calculate_square_area(side):
    """Calculate the area of a square."""
    if side < 0:
        raise InvalidMeasurementShapeException("Side must be non-negative.")
    return side * side

# Example usage:
if __name__ == "__main__":
    # Simple calculator usage
    print("Please select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n")

    try:
        select = int(input("Select operations from 1, 2, 3, 4: "))
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if select == 1:
            print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
        elif select == 2:
            print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
        elif select == 3:
            print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
        elif select == 4:
            result = divide(number_1, number_2)
            print(f"{number_1} / {number_2} = {result}")
        else:
            print("Invalid input, please select a number between 1 and 4.")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    
