import numpy as np
from numpy.testing import assert_array_equal
import unittest
import sys
import constants

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from quicksort import partition, quickSort
from common import checkTestCases


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
        checkTestCases(constants.testCases, quickSort)


if __name__ == '__main__':
    unittest.main()
