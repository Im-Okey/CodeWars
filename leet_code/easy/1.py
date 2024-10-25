from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    checked = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in checked:
            return [checked[compliment], i]
        else:
            checked[num] = i


print(twoSum([2, 7, 11, 15], 22))