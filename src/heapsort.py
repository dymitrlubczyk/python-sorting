import numpy as np
from common import swap


def heapSort(array):
    heap = Heap(array)
    sorted = np.array([])

    while (heap.size):
        sorted = np.append(sorted, heap.extract())

    return sorted


class Heap:
    def __init__(self, array):
        self.size = 0
        self.elements = np.array([-1])
        for x in array:
            self.insert(x)

    def downHeap(self, i):
        smallest = i
        left = 2 * i
        right = 2 * i + 1

        if (left <= self.size
                and self.elements[left] < self.elements[smallest]):
            smallest = left

        if (right <= self.size
                and self.elements[right] < self.elements[smallest]):
            smallest = right

        if (smallest != i):
            self.elements = swap(self.elements, smallest, i)
            self.downHeap(smallest)

    def upHeap(self, i):
        parent = i // 2
        if (self.elements[parent] > self.elements[i]):
            swap(self.elements, parent, i)
            self.upHeap(parent)

    def insert(self, element):
        self.size += 1
        self.elements = np.append(self.elements, element)
        self.upHeap(self.size)

    def extract(self):
        if (self.size == 0):
            print('Heap is empty')
            return

        root = self.elements[1]
        self.elements = swap(self.elements, 1, self.size)
        self.size -= 1
        self.downHeap(1)

        return root