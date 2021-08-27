import time
import numpy as np

def generate(size):
    numbers = np.array([])
    for i in range(size):
        numbers = np.append(numbers, np.random.randint(size))

    return numbers

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


def measureTime(sort, array, size, name):
    start = time.time()
    sort(array, 0, size)
    end = time.time()
    print(f'{name} time: {round(1000*(end-start))}ms')


def isSorted(array, size):
    for i in range(size):
        if(array[i]>array[i+1]):
            return False
    return True