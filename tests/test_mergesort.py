import numpy as np
from numpy.testing import assert_array_equal
import unittest
import sys
import constants

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from common import checkTestCases
from mergesort import mergeSort


class TestMergesort(unittest.TestCase):
    def test_mergeSort(self):
        checkTestCases(constants.testCases, mergeSort)


if __name__ == '__main__':
    unittest.main()