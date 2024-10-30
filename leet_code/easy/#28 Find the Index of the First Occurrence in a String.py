"""
Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.
"""


def strStr(haystack: str, needle: str) -> int:
    needle_len = len(needle)
    haystack_len = len(haystack)

    for i in range(haystack_len - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i

    return -1


if __name__ == '__main__':
    print(strStr("mississippi", "issip"))
