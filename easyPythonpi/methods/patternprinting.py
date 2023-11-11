#!/usr/bin/env python
#-*- coding: utf-8 -*-

def print_pyramid(num_rows: 'int', char: 'str') -> 'None':
    """
    Parameters
    ----------
    num_rows : int
        The number of rows a pyramid should have
    char : str
        The character to print out when displaying the pyramid
        e.g. using method like print_pyramid(3, &) will print as below:
            &
            &&
            &&&

    Returns
    ----------
    None
    """

    for i in range(num_rows):
        for j in range(i+1):
            print(char, end="") 
        print()
        