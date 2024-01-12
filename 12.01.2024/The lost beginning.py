"""
Given a sequence of one or more consecutive natural numbers concatenated into a string, return the smallest possible first number in the sequence. Numbers will never be truncated.

Examples
"123" -> [1, 2, 3] -> 1
"91011" -> [9, 10, 11] -> 9
"17181920" -> [17, 18, 19, 20] -> 17
"9899100" -> [98, 99, 100] -> 98
"121122123" -> [121, 122, 123] -> 121
"1235" -> [1235] -> 1235
"101" -> [101] -> 101
Size limits
0 < length string < 140
0 < smallest number < 1 000 000 000
"""


def find(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        num = int(s[:i])
        test = s[:i]
        while len(test) < length:
            num += 1
            test += str(num)
        if test == s:
            return int(s[:i])
    return int(s)


if __name__ == '__main__':
    print(find("72637236"))

