"""
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
"""


def parse_int(s: str) -> int:
    """
    This function takes a string as input and converts it into an integer.
    The function uses a dictionary to map each word in the input string to its corresponding integer value.
    The function then iterates over the words in the input string, accumulating the values of words with a value greater than or equal to 100.
    The function returns the accumulated value plus the value of any remaining words.

    Parameters:
        s (str): The input string to be converted into an integer.

    Returns:
        int: The integer value of the input string.

    Raises:
        ValueError: If the input string contains a word that cannot be converted to an integer.

    Examples:
        >>> parse_int("one")
        1
        >>> parse_int("twenty")
        20
        >>> parse_int("two hundred forty-six")
        246
        >>> parse_int("seven hundred eighty-three thousand nine hundred and nineteen")
        783919
    """
    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
        "million": 1000000
    }

    words = s.replace('-', ' ').replace(' and ', ' ').split()
    result = 0
    temp_result = 0

    for word in words:
        if word == "and":
            continue
        num = num_dict[word]
        if num == 100:
            temp_result *= num
        elif num >= 1000:
            result += temp_result * num
            temp_result = 0
        else:
            temp_result += num

    result += temp_result
    return result


if __name__ == '__main__':
    parse_int('two hundred forty-six')
