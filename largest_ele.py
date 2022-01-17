def largest(array,l):
  
    max = array[0]
    for i in range(1, l):
        if array[i] > max:
            max = array[i]
    return max