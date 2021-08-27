import numpy as np
from common import swap


def quickSort(array, l, r):
    if (l < r):
        pivot, array = partition(array, l, r)
        quickSort(array, l, pivot)
        quickSort(array, pivot + 1, r)

    return array


def partition(array, l, r):
    pivot = array[r - 1]
    current = l - 1

    for i in range(l, r):
        if (array[i] <= pivot):
            current += 1
            array = swap(array, i, current)

    return current, array
