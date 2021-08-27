import time
import numpy as np
from numpy.testing import assert_array_equal


def generate(size):
    numbers = np.array([])
    for i in range(size):
        numbers = np.append(numbers, np.random.randint(size))

    return numbers


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


def measureTime(array, sort, name):
    start = time.time()
    sorted = sort(array)
    end = time.time()

    if (isSorted(sorted)):
        print(f'{name} time: {round(1000*(end-start))}ms')
    else:
        print(f'{name} has not sorted properly: disqualification')


def isSorted(array):
    for i in range(array.size - 1):
        if (array[i] > array[i + 1]):
            return False
    return True


def checkTestCases(testCaseArray, sort):
    for testCase in testCaseArray:
        expected = np.sort(testCase)
        actual = sort(testCase)
        assert_array_equal(actual, expected)