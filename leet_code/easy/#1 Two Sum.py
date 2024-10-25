"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    checked = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in checked:
            return [checked[compliment], i]
        else:
            checked[num] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 22))