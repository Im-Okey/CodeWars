"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(arr: list) -> list:
    return sorted(arr, key=lambda x: x == 0 and x is not False)


if __name__ == '__main__':
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
