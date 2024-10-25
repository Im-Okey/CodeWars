"""
Roman numerals are represented by seven
 different symbols: I, V, X, L, C, D and M.
"""


def romanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
             "CD": 400, "CM": 900}
    result = 0
    roman_result_list = []
    skip_next = False
    for letter_index in range(len(s)):
        if skip_next:
            skip_next = False
            continue

        if letter_index == len(s) - 1:
            roman_result_list.append(s[letter_index])
            continue

        match s[letter_index]:
            case 'I':
                if s[letter_index + 1] != 'V' and s[letter_index + 1] != 'X':
                    roman_result_list.append(s[letter_index])
                else:
                    roman_result_list.append(s[letter_index] + s[letter_index + 1])
                    skip_next = True

            case 'X':
                if s[letter_index + 1] != 'L' and s[letter_index + 1] != 'C':
                    roman_result_list.append(s[letter_index])
                else:
                    roman_result_list.append(s[letter_index] + s[letter_index + 1])
                    skip_next = True

            case 'C':
                if s[letter_index + 1] != 'D' and s[letter_index + 1] != 'M':
                    roman_result_list.append(s[letter_index])
                else:
                    roman_result_list.append(s[letter_index] + s[letter_index + 1])
                    skip_next = True

            case _:
                roman_result_list.append(s[letter_index])

    for number in roman_result_list:
        result += roman[number]

    return result


if __name__ == "__main__":
    print(romanToInt("III"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))
