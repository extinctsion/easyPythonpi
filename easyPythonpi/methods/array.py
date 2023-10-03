def createarray(length:'int',dtype='int')->'array':   # To create an array of entered length and entered data type(interger data type is a default data type)
    import numpy as np 
    a=[]  #empty list
    for i in range(length):
        # if entered dtype is an interger
            if dtype=='int':
                        e=int(input(f"Enter {i+1} element : "))
                        a.append(e)
        # if entered dtype is a string
            elif dtype=='str' or dtype=='string':
                                e=str(input("Enter {i+1} element : "))
                                a.append(e)
        # if entered dtype is a float                         
            elif dtype=='float':
                                e=float(input("Enter {i+1} element : "))
                                a.append(e)
                                
                                    
    b=np.array(a)    
    return b

def arrayrev(array:'array')->'array':        # To reverese the array elements
    import numpy as np
    r=[]
    for i in range(len(array)-1,-1,-1):
                r.append(array[i])
    a=np.array(r)
    return a

