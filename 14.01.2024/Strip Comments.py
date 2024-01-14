"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

import re


def strip_comments(text, markers):
    pattern = '|'.join(re.escape(marker) + '.*' for marker in markers)
    text_without_comments = re.sub(pattern, '', text, flags=re.MULTILINE)
    lines = [line.rstrip() for line in text_without_comments.split('\n')]
    return '\n'.join(lines)


input_string = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]
result = strip_comments(input_string, markers)
print(result)

if __name__ == '__main__':
    print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
