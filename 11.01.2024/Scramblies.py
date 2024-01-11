"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


def scramble(s1, s2):
    letter_count = {}
    for letter in s1:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter in s2:
        if letter in letter_count and letter_count[letter] > 0:
            letter_count[letter] -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    print(scramble('scriptjava', 'javascript'))
