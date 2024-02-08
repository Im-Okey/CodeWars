"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""


def sum_strings(x: str, y: str) -> str:
    max_length = max(len(x), len(y))
    x = x.zfill(max_length)
    y = y.zfill(max_length)

    result = []
    carry = 0

    for i in range(max_length - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1]).lstrip('0') or '0'


if __name__ == '__main__':
    print(sum_strings("123", "456"))