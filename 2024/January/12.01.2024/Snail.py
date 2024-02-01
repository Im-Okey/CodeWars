"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""


def snail(snail_map: list) -> list:
    if len(snail_map) == 0:
        return []

    result = []
    while snail_map:
        result += snail_map.pop(0)
        snail_map = list(zip(*snail_map))[::-1]
    return result


if __name__ == '__main__':
    print(
        snail(
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        )
    )
