import numpy as np
from common import swap


def quickSort(array):
    if (array.size <= 1):
        return array

    pivot, array = partition(array)
    left = quickSort(array[:pivot])
    right = quickSort(array[pivot + 1:])
    return np.concatenate((left, array[pivot], right), axis=None)


def partition(array):
    pivot = array[array.size - 1]
    current = -1

    for i in range(array.size):
        if (array[i] <= pivot):
            current += 1
            array = swap(array, i, current)

    return current, array
