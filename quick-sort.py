import sys
import time
import numpy as np
from initializer import init 


print("Hello I am quick sort, my time complexity is n2")

size = int(sys.argv[1])
numbers = init(size)

def swap(i,j):
    numbers[i], numbers[j] = numbers[j], numbers[i]


def partition(l, r):
    pivot = numbers[r-1]
    current = l 

    for i in range(l,r):
        if(numbers[i]<=pivot):
            swap(i,current)
            current += 1

    return current 


def quickSort(l, r):
    if(l<r):
        pivot = partition(l, r)
        quickSort(l, pivot-1)
        quickSort(pivot+1, r)

quickSort(0, size)
print(numbers)