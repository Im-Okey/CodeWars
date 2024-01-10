"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
"""


def square_digits(num: int) -> int:
    list_of_nums = [int(i) for i in str(num)]
    final_list = [str(i**2) for i in list_of_nums]
    return int(''.join(final_list))


if __name__ == "__main__":
    square_digits(8119)