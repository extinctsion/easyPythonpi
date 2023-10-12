#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np 


def createarray(length:'int',dtype='int')->'list':   
    # To create an array of entered length and entered data type(interger data type is a default data type)
    new_array=[]  #empty list
    for i in range(length):
        # if entered dtype is an interger
        if dtype=='int':
            array_input=int(input(f"Enter {i+1} element : "))
            new_array.append(array_input)
        # if entered dtype is a string
        elif dtype=='str' or dtype=='string':
            array_input=str(input("Enter {i+1} element : "))
            new_array.append(array_input)
        # if entered dtype is a float                         
        elif dtype=='float':
            array_input=float(input("Enter {i+1} element : "))
            new_array.append(array_input)

    created_array = np.array(new_array)
    
    return created_array

def arrayrev(array:'list')->'list':        
    # To reverese the array elements
    temp_array=[]
    for i in range(len(array)-1,-1,-1):
        temp_array.append(array[i])
    reversed_array=np.array(temp_array)

    return reversed_array

