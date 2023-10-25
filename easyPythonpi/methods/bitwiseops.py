import regex as re
import easyPythonpi.easyPythonpi as pi

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