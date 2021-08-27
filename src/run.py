import sys
from common import generate, measureTime
from quicksort import quickSort
from mergesort import mergeSort

size = int(sys.argv[1])
array = generate(size)

print(f'Here are sorting times for array of size: {size}')
measureTime(array, quickSort, 'quick sort')
measureTime(array, mergeSort, 'merge sort')
