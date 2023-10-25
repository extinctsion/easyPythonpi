#!/usr/bin/env python
#-*- coding: utf-8 -*-

import easyPythonpi.easyPythonpi as pi
import regex as re

def add(x:'float', y:'float')->'float': # For addition of 2 numbers
    return  x+y

def sub(x:'float', y:'float')->'float':  # For substraction of 2 numbers
    return  x-y

def multi(x:'float', y:'float')->'float': # For multiplication of 2 numbers
    return  x*y

def div(x:'float', y:'float')->'float':   # For division of 2 numbers
    return  x/y

def mod(x:'float', y:'float')->'float':   # For finding the modulus of 2 numbers
    return  x%y

def calculate_percentage(part, whole):
    if whole == 0:
        return 0  # Avoid division by zero
    return (part / whole) * 100


def factorial(n:'int')->'int': # To find the factorial of 2 numbers
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

# To compute the factord of the argument passed
def factors(n:'int')->'int':
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def Area_circle(r:'float')->'float':  # To find the area of a circle using the radius r
    PI = 3.142
    return PI * (r * r)

def Perimeter_circle(r:'float')->'float': # To find the perimeter of a circle using the radius r
    PI = 3.142
    return 2 * PI * r 

def fibonacci(n:'int')->'int':  #To find the nth fibonacci series
    """Finds the fibonacci of the nth sequence.

    This function calculates the fibonacci sequence.  This function calculates
    the nth fibonacci of a number by finding the sum of two numbers in the 
    fibonacci sequence before n

    Args:
        n ('int') : The number to find the fibonacci sequence of, assumes n >=1
                    as valid numbers to find the fibonacci of n.

    Returns:
        The fibonacci of arg n.

    Raises:
        No errors 
    """
    if n<=0:
        raise pi.InvalidNumberFibException(n)
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        fib1 = 0
        fib2 = 1

        for i in range(2,n-1):
             fibN = fib1 + fib2
             fib1 = fib2 
             fib2 = fibN

        return fib1 +fib2
                
#method to print the 1st prime number between the range
def printprime(start:'int',end:'int')->'list':
    if start<=0:
            start=2
    p=[]        
    for i in range(start,end+1):
                j=0
                for k in range(2,i):
                            if i%k==0:
                                    j=1
                                    break
                if j==0:
                        p.append(i)
                        
    return p                                           
                   
def even_or_odd(data:'int'):
    try : 
        if data%2==0:
                    return 'even'
        else:
                    return 'odd'
        
    except:
        print("\nError occured, parameter passed should be purely numeric") 
