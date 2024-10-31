"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    for i in nums:
        if i >= target:
            if i == target:
                return nums.index(i)
            return nums.index(i)
    return len(nums)


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 4))
