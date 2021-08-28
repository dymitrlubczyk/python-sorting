import sys
from common import generate, measureTime
from quicksort import quickSort
from mergesort import mergeSort
from heapsort import heapSort
from numpy import sort

size = int(sys.argv[1])
array = generate(size)

print(f'\nHere are sorting times for array of size: {size}\n')

measureTime(array, quickSort, 'quick sort')
measureTime(array, mergeSort, 'merge sort')
measureTime(array, heapSort, 'heap sort')
measureTime(array, sort, 'numpy sort')

print('')
