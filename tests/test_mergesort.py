import numpy as np
from numpy.testing import assert_array_equal
import unittest
import sys
import constants

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from common import checkTestCases
from mergesort import mergeSort, merge


class TestMergesort(unittest.TestCase):
    def test_merge(self):

        left = np.array([1])
        right = np.array([2])
        expected = np.array([1, 2])
        assert_array_equal(merge(left, right), expected)

        left = np.array([1, 2])
        right = np.array([2, 2])
        expected = np.array([1, 2, 2, 2])
        assert_array_equal(merge(left, right), expected)

        left = np.array([1, 1, 1])
        right = np.array([2])
        expected = np.array([1, 1, 1, 2])
        assert_array_equal(merge(left, right), expected)

        left = np.array([1, 2])
        right = np.array([])
        expected = np.array([1, 2])
        assert_array_equal(merge(left, right), expected)

        left = np.array([1, 2, 4, 6, 9])
        right = np.array([3, 5, 7, 8])
        expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert_array_equal(merge(left, right), expected)

    def test_mergeSort(self):
        checkTestCases(constants.testCases, mergeSort)


if __name__ == '__main__':
    unittest.main()