#!/usr/bin/env python
#-*- coding: utf-8 -*-


# Matrix problems

def matrix_add(array1:'list',array2:'list')->'list':
    import numpy as np
    
    result=np.array(array1)+np.array(array2)
    return result


def matrix_sub(array1:'list',array2:'list')->'list':
    import numpy as np
    
    result=np.array(array1)-np.array(array2)
    return result

 # Multiplication of two                   
def matrix_mul(matrix1:'list',matrix2:'list')->'list':
    import numpy as np
    matrix1=np.array(matrix1)  # converting list into array
    matrix2=np.array(matrix2)  
    a=list(matrix1.shape)      # getting the shape of the array
    b=list(matrix2.shape)
    if len(a)==1:
        k=a[0]              # suppose if row is one , for eg [1,2,3] ,then shape returns (3,) instead of [1,3].. 
        a[1]=k    
        a[0]=1              # here first element becomes last element and in place of first element , 1 is appended..
    if a[1]==b[0]:       # from matrix multiplication convention, number of columns of first matrix needs to be equal to number of rows of second matrix
        tt=[]
        for i in range(b[0]):
            u=[]
            for j in range(b[0]):
                u.append(matrix2[j][i])
            tt.append(u)
        t=np.array(tt)   # arrays of coloumn of second matrix
        pp=[]
        
        for k in range(b[0]):
            ar=[]
            for l in range(b[0]):
                y=matrix1[k]*t[l]  # multiplication of rows and columns
                ar.append(list(y)) # appending the result into a list
            pp.append(ar)
        l=[]        
        for i in pp:
            zz=[]
            for j in i:
                sum1=0
                for c in j:
                  sum1=sum1+c  # sum all the element of each row each column
                zz.append(sum1) 
            l.append(zz)    # appending the sum of each row and column of result matrix into a list
        l=np.array(l)  # convert the list of result matrix into array
        return l         
            
            

def matrix_shape(matrix1:'list')->'list':
    import numpy as np
    matrix1=np.array(matrix1)  
    a=list(matrix1.shape)      
    if len(a)==1:
            k=a[0]             
            a[1]=k    
            a[0]=1                                                                                                            
    return a                 #returns shape of a matrix              
                      
                          
                      

def matrix_transpose(matrix1:'list')->'list':
    import numpy as np
    matrix1=np.array(matrix1)  # converting list into array
    a=list(matrix1.shape)      # getting the shape of the array
    tt=[]
    for i in range(a[0]):
                u=[]
                for j in range(len(a)):
                        u.append(matrix1[j][i])
                tt.append(u)
    t=np.array(tt)   # get a transpose of matrix1
    return t       


