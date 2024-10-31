"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    val_count = nums.count(val)
    for i in range(val_count):
        nums.remove(val)
    return len(nums)


if __name__ == '__main__':
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))