# Some utilities for counting

import math

def test_equal(a, b):
    if a == b:
        print("Result: PASSED")
    else:
        print("Result: FAILED")


def test_close(a, b):
    if math.isclose(a, b):
        print("Result: PASSED")
    else:
        print("Result: FAILED")