"""
This is a hard version of How many are smaller than me?. If you have troubles solving this one, have a look at the easier kata first.

Write

function smaller(arr)
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
"""
from typing import List


def smaller(nums: List[int]):
    """
    This function takes in a list of integers and returns a list of integers where each element represents the number of integers in the input list that are smaller than the corresponding element in the output list.

    Parameters:
    nums (List[int]): The input list of integers

    Returns:
    List[int]: The output list of integers, where each element represents the number of integers in the input list that are smaller than the corresponding element in the output list.
    """

    def sort(enum):
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller


if __name__ == '__main__':
    smaller([5, 4, 3, 2, 1])
