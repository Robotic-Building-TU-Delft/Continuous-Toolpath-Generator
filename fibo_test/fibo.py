import numpy as np

def generate_fibonacci_sequence(n):  
    if n > 0:
        number = 1 
        prev_number = 0 
        for i in range(n):
            if i < 1: 
                yield prev_number
            else:
                yield number
                number += prev_number
                prev_number = number - prev_number 

def get_fibonacci_sequence(n):
    return np.array(list(generate_fibonacci_sequence(n)))