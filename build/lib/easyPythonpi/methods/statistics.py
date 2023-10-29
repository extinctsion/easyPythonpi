# statistics.py contains all functions for statistical operations

def calculate_average(datas: 'list'):
    total_sum = 0
    count = len(datas)
    
    for value in datas:
        total_sum += value
    
    average = total_sum / count
    return average
