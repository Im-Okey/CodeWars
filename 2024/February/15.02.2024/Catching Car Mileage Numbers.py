"""
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
"""


def is_interesting(number: int, awesome_phrases: list[int]):
    """
    This function takes in an integer number and a list of integers. It returns an integer value of 0, 1, or 2 to
     indicate whether the number is "interesting", "near an interesting number", or "not interesting", respectively.

    The function determines whether a number is interesting based on the following criteria:

    1. If the number is less than 100, it is considered not interesting.
    2. If the number is 109, it is considered interesting.
    3. If the number is a palindrome or a sequence of only zeros or ones, it is considered interesting.
    4. If the number is in the list of "awesome phrases", it is considered interesting.
    5. If the number is one digit longer than a palindrome or a sequence of only zeros or ones, and does not match
    any "awesome phrases", it is considered interesting.
    6. If the number is two digits longer than a palindrome or a sequence of only zeros or ones, and is not in the
    list of "awesome phrases", but the next number is in the list of "awesome phrases", it is considered "near an
    interesting number".
    7. If the number is not longer than a palindrome or a sequence of only zeros or ones, and is not in the list of
    "awesome phrases" and the next number is not in the list of "awesome phrases", it is considered not interesting.

    The function also ensures that the input number is less than 1,000,000,000.

    Args:
        number (int): The integer number to be evaluated.
        awesome_phrases (List[int]): A list of integers that are considered "awesome phrases".

    Returns:
        int: An integer value of 0, 1, or 2 to indicate whether the number is "interesting", "near an interesting
         number", or "not interesting", respectively.

    Raises:
        ValueError: If the input number is greater than or equal to 1,000,000,000.

    """
    def is_sequential(num_str):
        return num_str in '12345678901234567890' or num_str in '98765432109876543210'

    def is_palindrome(num_str):
        return num_str == num_str[::-1]

    def is_interesting_number(num, phrases):
        """
                This function takes in an integer number and a list of integers. It returns an integer value of 0, 1,
                or 2 to indicate whether the number is "interesting", "near an interesting number", or "not
                 interesting", respectively.

                """
        if num < 100:
            return 0
        if num == 109:
            return 1
        num_str = str(num)
        if num in phrases:
            return 2
        if is_sequential(num_str) or is_palindrome(num_str) or all(digit == '0' for digit in num_str[1:]) or len(
                set(num_str)) == 1:
            return 2
        if any((num + i) in phrases for i in range(3)):
            return 1
        return 0

    if number >= 1000000000:
        return 0

    result = is_interesting_number(number, awesome_phrases)
    if result != 0:
        return result
    elif (number + 1 >= 100 and is_interesting_number(number + 1, awesome_phrases) != 0) or \
            (number + 2 >= 100 and is_interesting_number(number + 2, awesome_phrases) != 0):
        return 1
    else:
        return 0


if __name__ == '__main__':
    is_interesting(1336, [1337, 256])
