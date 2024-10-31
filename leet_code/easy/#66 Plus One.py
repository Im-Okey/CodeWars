"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if len(digits) == 1:
                digits.insert(0, 1)
                return digits
            else:
                for j in range(i - 1, -1, -1):
                    if digits[j] != 9:
                        digits[j] += 1
                        return digits
                    else:
                        if j != 0:
                            digits[j] = 0
                        else:
                            digits[j] = 0
                            digits.insert(0, 1)
                            return digits


if __name__ == '__main__':
    print(plusOne([8,9,9,9]))
    print(plusOne([4, 3, 2, 1]))
    print(plusOne([9]))
    print(plusOne([9, 9, 9, 9]))
