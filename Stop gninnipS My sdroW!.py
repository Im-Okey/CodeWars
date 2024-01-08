"""
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""


def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in list(sentence.split())])


if __name__ == '__main__':
    print(spin_words('This is another test'))