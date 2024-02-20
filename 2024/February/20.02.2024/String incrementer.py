"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


import re


def increment_string(strng: str) -> str:
    match = re.search(r'(\d*)$', strng)  # find any digits at the end of the string
    if match:
        number = match.group(0)
        number_len = len(number)
        if number:
            new_number = str(int(number) + 1).zfill(number_len)  # increment the number and pad with leading zeros
            return strng[:-number_len] + new_number
        else:
            return strng + '1'
    else:
        return strng + '1'


if __name__ == '__main__':
    increment_string("foobar001")
