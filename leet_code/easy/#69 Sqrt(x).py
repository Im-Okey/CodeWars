"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    elif x == 2:
        return 1
    for i in range(x):
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1


if __name__ == '__main__':
    print(mySqrt(8))
