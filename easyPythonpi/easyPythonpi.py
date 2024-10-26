""" A Python module that helps you to calculate some of the most used calculations.....
    usage--
            Just download the file from git and unzip it on your system.
            And while using this module, just write as code-
            'from easypythonpi import *' and you're good to go...
                            ~Happy programming
"""

# Programmer-defined exceptions
class InvalidBinaryException(Exception):
    """Raised when an invalid binary string is provided."""
    pass

class InvalidNumberFibException(Exception):
    """Raised when the Fibonacci number is invalid."""
    def __init__(self, n, message="n is not valid, must be greater than or equal to 1"):
        self.n = n
        self.message = message
        super().__init__(self.message)

class InvalidMeasurementShapeException(Exception):
    """Raised when invalid measurement values are provided for shapes."""
    def __init__(self, message="Invalid measurement, must be greater than or equal to 0"):
        self.message = message
        super().__init__(self.message)

# Function definitions
def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, or an error message if dividing by zero."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

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
