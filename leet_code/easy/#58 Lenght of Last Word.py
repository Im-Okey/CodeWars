"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.
"""

def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])


if __name__ == '__main__':
    print(lengthOfLastWord("   fly me   to   the moon  "))