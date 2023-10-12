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


def calculate_average(*args, **kwargs):
    total_sum = sum(args)
    count = len(args) + len(kwargs.values())
    
    for value in kwargs.values():
        total_sum += value
    
    average = total_sum / count
    return average

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
#A method to convert Hexadecimal input to binary numbers
def hex2bin(x:'hex')->'bin':
    x=str(x)
    r=''
    for i in x:
        if i=='A':
            r=r+'1010'
        elif i=='B':
            r=r+'1011'
        elif i=='C':
            r=r+'1100'
        elif i=='D':
            r=r+'1101'
        elif i=='E':
            r=r+'1110'
        elif i=='F':
            r=r+'1111'
        else:
            h=bin(int(i))
            n=h[2:]
            for j in range(4):
               if len(n)<4:
                    n='0'+n
                    
            r=r+n
    return r
    

#A method to convert Octal input to binary numbers
def oct2bin(x:'oct')->'bin':       
    r='' 
    x=str(x)
    for i in x:        
        h=bin(int(i))
        n=h[2:]
        for i in range(3):
                if len(n)<3:
                    n='0'+n
        r=r+n            
    return r

#A method to convert binary input to decimal numbers
def bin2dec(x:'bin')->'int': 
    x=list(str(x))
    l=len(x)
    a=0
    r=0
    for i in range(l-1,-1,-1):
            
            r=r+(int(x[i])*(2**a))
        
            a=a+1
    return r                  

# A function that converts a binary string to hexadecimal
def bin2hex(x:'bin')->'hex': 
    """Converts a binary string to a hexadecimal string.

    This function converts a binary string to hexadecimal. If the binary
    string's length is a multiple of 4, simply break up the string into 
    substrings of 4 binary digits and determine their hexadecimal digit.
    If the binary string's length not a multiple of 4 prepend the 
    necessary number of 0's to make the string a multiple of 4.

    Args:
        x ('bin') : Binary string to convert to hexadecimal.

    Returns:
        The binary converted to hexadecimal.

    Raises:
        No errors 
    """

    h = ''  # hexadecimal number converted from binary and to be returned

    
    x=str(x)
    
    # Determine if the string has invalid characters
    if re.search('[^(0-1)]', x):
        raise pi.InvalidBinaryException 

    # Get the length of the string
    l=len(x)

    # Begin the process of converting x to its hexadecimal number

    # If the length is not a multiple of 4, prepend 0's before converting
    if l % 4 != 0:
        numZerosPrepended = 4 - ( l % 4 ) # number of zeros to prepend 
        x = (numZerosPrepended * '0') + x # concatenate numZerosPrepended to x

    
    for i in range(len(x)-1, 0, -4):
        substring = x[i-3:i+1]    # The substring converted to a hex character

        # Determine the binary substring's hex and prepend to h
        if substring == '0000':
            h = '0' + h
        elif substring == '0001':
            h = '1' + h
        elif substring == '0010':
            h = '2' + h
        elif substring == '0011':
            h = '3' + h            
        elif substring == '0100':
            h = '4' + h
        elif substring == '0101':
            h = '5' + h
        elif substring == '0110':
            h = '6' + h
        elif substring == '0111':
            h = '7' + h
        elif substring == '1000':
            h = '8' + h
        elif substring == '1001':
            h = '9' + h
        elif substring == '1010':
            h = 'A' + h
        elif substring == '1011':
            h = 'B' + h
        elif substring == '1100':
            h = 'C' + h
        elif substring == '1100':
            h = 'C' + h
        elif substring == '1101':
            h = 'D' + h
        elif substring == '1110':
            h = 'E' + h
        elif substring == '1111':
            h = 'F' + h
            
    return h 


def bin2oct(x:'bin')->'oct':  
    o = ''  # hexadecimal number converted from binary and to be returned

    x=str(x)
    
    # Determine if the string has invalid characters
    if re.search('[^(0-1)]', x):
        raise pi.InvalidBinaryException 

    # Get the length of the string
    l=len(x)

    # Begin the process of converting x to its hexadecimal number

    # If the length is not a multiple of 3, prepend 0's before converting
    if l % 3 != 0:
        numZerosPrepended = 3 - ( l % 3 ) # number of zeros to prepend 
        x = (numZerosPrepended * '0') + x # concatenate numZerosPrepended to x

    for i in range(len(x), 0, -3):
        substring = x[i-3:i]

        if substring == '000':
            o = '0' + o
        elif substring == '001':
            o = '1' + o
        elif substring == '010':
            o = '2' + o
        elif substring == '011':
            o = '3' + o
        elif substring == '100':
            o = '4' + o                        
        elif substring == '101':
            o = '5' + o        
        elif substring == '110':
            o = '6' + o
        elif substring == '111':
            o = '7' + o    

    return o


def ispalindrome(x:'str')->'str':        # To check if the given parameter is palindrome or not
    x=str(x)  #explicitly convert into string data type so as to iterate through each character
    r=''
    for i in range(len(x)-1,-1,-1):
                r=r+x[i]
    if x==r:    # if the parameter get matched with its reverse then returns true othewise false
            return True
    else:
            return False
                   
                   

def even_or_odd(data:'int'):
    try : 
        if data%2==0:
                    return 'even'
        else:
                    return 'odd'
        
    except:
        print("\nError occured, parameter passed should be purely numeric") 


                                            
def remove_punctuation(my_str:'str')->'str':
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuations from the string
    no_punct = ""
    #run a for loop and traverse every element in a string and check ,if char is not match with punctuations char then it will add in no_punct
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    #return no_punct
    return no_punct

def count_vowels(ip_str:'str')->'int':
    # string of vowels
    vowels = 'aeiou'
    # make it suitable for comparisions
    ip_str = ip_str.casefold()

    # make a dictionary with each vowel a key and value 0
    count = {}.fromkeys(vowels,0)

    # count the vowels
    for char in ip_str:
        if char in count:
            count[char] += 1
            
    #return the count dictionary
    return count

