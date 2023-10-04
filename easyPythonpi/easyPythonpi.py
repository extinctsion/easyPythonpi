import regex as re,os,sys
sys.path.append('/home/jugal/github/easyPythonpi/easyPythonpi')
from methods.Graph import *
from methods.search import *
from methods.sorting import *
from methods.array import *
from methods.basics import *
from methods.linkedlist import *
from methods.matrix import *
"""  A python module that helps you to calculate some of the  most used calculations.....
    usage--
            Just download the file from git and unzip in ur system.
            And while using this module, just write as code-
            'from module import *' and u r good to go...
                            ~Happy programming"""
                        

# Programmer defined exceptions go here:

# define exception for invalid Binary Strings  


class InvalidBinaryException(Exception):
    pass

class InvalidNumberFibException(Exception):
    def __init__(self, n, message="n is not valid, must be greater than or equal to 1"):
         self.n = n
         self.message = message
         
