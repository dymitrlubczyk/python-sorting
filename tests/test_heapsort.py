import numpy as np
from numpy.testing import assert_array_equal
import unittest
import sys
import constants

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from common import checkTestCases
from heapsort import Heap, heapSort


class TestHeapsort(unittest.TestCase):
    def test_downHeap(self):
        heap = Heap([1])

        heap.downHeap(1)
        assert_array_equal(heap.elements, np.array([-1, 1]))

        heap.size = 2
        heap.elements = np.array([-1, 2, 1])
        heap.downHeap(1)
        assert_array_equal(heap.elements, np.array([-1, 1, 2]))

        heap.size = 4
        heap.elements = np.array([-1, 5, 2, 3, 1])
        heap.downHeap(1)
        assert_array_equal(heap.elements, np.array([-1, 2, 1, 3, 5]))

    def test_insert(self):
        heap = Heap([])
        heap.insert(5)
        assert_array_equal(heap.elements, np.array([-1, 5]))
        heap.insert(4)
        assert_array_equal(heap.elements, np.array([-1, 4, 5]))
        heap.insert(3)
        assert_array_equal(heap.elements, np.array([-1, 3, 5, 4]))
        heap.insert(6)
        assert_array_equal(heap.elements, np.array([-1, 3, 5, 4, 6]))

    def test_init(self):
        heap = Heap([])
        assert_array_equal(heap.elements, np.array([-1]))
        self.assertEqual(heap.size, 0)

        heap = Heap([0])
        assert_array_equal(heap.elements, np.array([-1, 0]))
        self.assertEqual(heap.size, 1)

        heap = Heap([1, 2, 3])
        assert_array_equal(heap.elements, np.array([-1, 1, 2, 3]))
        self.assertEqual(heap.size, 3)

        heap = Heap([3, 2, 1])
        assert_array_equal(heap.elements, np.array([-1, 1, 3, 2]))
        self.assertEqual(heap.size, 3)

    def test_heapSort(self):
        checkTestCases(constants.testCases, heapSort)


if __name__ == '__main__':
    unittest.main()
#       5
#   2       3
#1
