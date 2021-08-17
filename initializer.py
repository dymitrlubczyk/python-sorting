import numpy as np
from numpy import random

def init(size):
    numbers = np.array([])
    for i in range(size):
        numbers = np.append(numbers, random.randint(size))

    print(numbers)
    return numbers
