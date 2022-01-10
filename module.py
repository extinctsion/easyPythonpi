"""  A python module that helps you to calculate some of the  most used calculations.....
    usage--
            Just download the file from git and unzip in ur system.
            And while using this module, just write as code-
            'from module import *' and u r good to go...
                            ~Happy programming"""

def add(x, y): # For addition of 2 numbers
    return  x+y

def sub(x, y):  # For substraction of 2 numbers
    return  x-y

def multi(x, y): # For multiplication of 2 numbers
    return  x*y

def div(x, y):   # For division of 2 numbers
    return  x/y

def mod(x, y):   # For finding the modulus of 2 numbers
    return  x%y

def factorial(n): # To find the factorial of 2 numbers
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

def Area_circle(r):  # To find the area of a circle using the radius r
    PI = 3.142
    return PI * (r * r)

def Perimeter_circle(r): # To find the perimeter of a circle using the radius r
    PI = 3.142
    return 2 * PI * r 

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
                

def printprime(start,end):
            if start<=0:
                    start=1
            for i in range(start,end+1):
                        j=0
                        for k in range(2,i):
                                  if i%k==0:
                                         j=1
                        if j==0:
                              return i
                              

def hex2bin(x):
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
          


def oct2bin(x):       
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


def bin2dec(x): 
           x=list(str(x))
           l=len(x)
           a=0
           r=0
           for i in range(l-1,-1,-1):
                    
                    r=r+(int(x[i])*(2**a))
              
                    a=a+1
           return r                  
             


                      
                     
                                  
