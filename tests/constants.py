import numpy as np
import sys

sys.path.append(
    '/Users/dymitrlubczyk/Repositories/python-algorithms/sorting/src')
from common import generate

testCases = [
    np.array([]),
    np.array([2, 1, 3]),
    np.array([1, 1, 1]),
    np.array([6, 2, 4, 8, 2, 1, 3, 4, 5]),
    np.array([1, 2, 3, 4, 5]),
    np.array([5, 4, 3, 2, 1]),
    generate(100),
    generate(1000),
    generate(10000)
]
