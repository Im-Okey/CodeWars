"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


def next_smaller(n: int) -> int:
    digits = list(str(n))
    length = len(digits)

    i = length - 1
    while i > 0 and digits[i] >= digits[i - 1]:
        i -= 1

    if i == 0:
        return -1

    j = i - 1
    while j + 1 < length and digits[j + 1] < digits[i - 1]:
        j += 1

    digits[i - 1], digits[j] = digits[j], digits[i - 1]

    result = int(''.join(digits[:i] + digits[i:][::-1]))

    return result if (length == len(str(result))) and (result < n) else -1


if __name__ == '__main__':
    print(next_smaller(907))
