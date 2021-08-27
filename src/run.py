import sys
from common import generate, measureTime
from quicksort import quickSort

size = int(sys.argv[1])
array = generate(size)

print(f'Here are sorting times for array of size: {size}')
measureTime(quickSort, array, size, 'quick sort')
