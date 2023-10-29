import easyPythonpi as pi
import regex as re

def remove_punctuation(my_str:'str')->'str':
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuations from the string
    no_punct = ""
    #run a for loop and traverse every element in a string and check ,if char is not match with punctuations char then it will add in no_punct
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

def count_vowels(ip_str:'str')->'dict':
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

# To check if the given parameter is palindrome or not
def is_palindrome(x:'str')->'bool':        
    # convert into string data type so as to iterate through each character
    x=str(x)  

    # remove whitespace, lower case letters, and then remove punctuations
    x = x.replace(" ", "")
    x = x.lower()
    x = remove_punctuation(x)

    # Convert original string to its reversed version
    r=''
    for i in range(len(x)-1,-1,-1):
        r=r+x[i]

    # if the parameter get matched with its reverse then returns true othewise false
    if x==r:    
        return True
    else:
        return False 