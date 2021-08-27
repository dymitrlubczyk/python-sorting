import numpy as np
from numpy.core.fromnumeric import sort
from numpy.lib.function_base import append


def mergeSort(array):
    if (array.size <= 1):
        return array

    half = array.size // 2
    left = mergeSort(array[:half])
    right = mergeSort(array[half:])
    return merge(left, right)


def merge(left, right):
    sorted = np.array([])
    r = 0
    l = 0
    while (l < left.size and r < right.size):
        if (left[l] <= right[r]):
            sorted = np.append(sorted, left[l])
            l += 1
        else:
            sorted = np.append(sorted, right[r])
            r += 1

    sorted = np.append(sorted, left[l:])
    sorted = np.append(sorted, right[r:])

    return sorted