import numpy as np
from numpy.testing import assert_array_equal
import unittest
import sys

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from quicksort import partition, quickSort
from common import generate


class TestQuicksort(unittest.TestCase):
    def test_partition(self):

        input = np.array([0])
        pivot, array = partition(input, 0, 1)
        self.assertEqual(pivot, 0)

        input = np.array([1, 2, 0])
        expected = np.array([0, 1, 2])
        pivot, array = partition(input, 0, 3)
        self.assertEqual(pivot, 0)

        input = np.array([1, 2, 3])
        expected = np.array([1, 2, 3])
        pivot, array = partition(input, 0, 3)
        self.assertEqual(pivot, 2)
        assert_array_equal(array, expected)

        input = np.array([1, 2, 0, 3, 2])
        expected = np.array([1, 2, 0, 2, 3])
        pivot, array = partition(input, 0, 5)
        self.assertEqual(pivot, 3)
        assert_array_equal(array, expected)

        input = np.array([2, 2, 2, 2, 2])
        expected = np.array([2, 2, 2, 2, 2])
        pivot, array = partition(input, 0, 5)
        self.assertEqual(pivot, 4)
        assert_array_equal(array, expected)

    def test_quickSort(self):
        array = np.array([])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = np.array([2, 1, 3])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = np.array([1, 1, 1])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = np.array([6, 2, 4, 8, 2, 1, 3, 4, 5])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = np.array([1, 2, 3, 4, 5])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = np.array([5, 4, 3, 2, 1])
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = generate(100)
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = generate(1000)
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))

        array = generate(10000)
        assert_array_equal(quickSort(array, 0, array.size), np.sort(array))


if __name__ == '__main__':
    unittest.main()
