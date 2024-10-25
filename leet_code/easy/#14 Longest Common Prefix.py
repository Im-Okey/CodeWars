"""
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    common_prefix = ''
    min_word = min(strs, key=len)
    for letter_index in range(len(min_word)):
        for word in strs:
            if min_word[letter_index] != word[letter_index]:
                return common_prefix
        common_prefix += min_word[letter_index]
    return common_prefix


if __name__ == '__main__':
    print(longestCommonPrefix(["aa","ab"]))
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))