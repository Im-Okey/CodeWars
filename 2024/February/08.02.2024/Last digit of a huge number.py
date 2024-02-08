"""
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.
"""


def last_digit(lst: list) -> int:
    result = 1
    for num in reversed(lst):
        result = num ** (result if result < 4 else result % 4 + 4)
    return result % 10


if __name__ == '__main__':
    print(last_digit([499942, 898102, 846073]))
