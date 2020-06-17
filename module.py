"""  A python module that helps you to calculate some of the  most used calculations.....
    usage--
            Just download the file from git and unzip in ur system.
            And while using this module, just write as code-
            'from module import *' and u r good to go...
                            ~Happy programming"""

def add(x, y): # for addition of 2 numbers
    return  x+y

def sub(x, y):  # for substraction of 2 numbers
    return  x-y

def multi(x, y): # for multiplication of 2 numbers
    return  x*y

def div(x, y):   # for division of 2 numbers
    return  x/y

def mod(x, y):   #for finding the modulus of 2 numbers
    return  x%y


def factorial(n): # to find the factorial of 2 numbers
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


def Area_circle(r):  # TO find the area of a circle using a radius r
    PI = 3.142
    return PI * (r*r);


def fibonacci(n):  #To find the nth fibonacci series
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def sort(list):    # To bubble sort and array or list
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp




