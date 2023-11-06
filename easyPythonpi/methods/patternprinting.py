def pyramid_pattern_printing(num_rows: 'int', char: 'str') -> 'int':
    for i in range(num_rows):
        for j in range(i+1):
            print(char, end="") 
        print()
        