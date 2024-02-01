"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s: str) -> list:
    return [s[i] + s[i + 1] if i != len(s) - 1 else s[i] + '_' for i in range(0, len(s), 2)]


if __name__ == '__main__':
    print(solution('asdfads'))
