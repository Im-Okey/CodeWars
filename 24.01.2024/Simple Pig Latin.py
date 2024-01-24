"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text: str) -> str:
    words = text.split()
    pig_words = []
    for word in words:
        if word.isalpha():
            pig_word = word[1:] + word[0] + "ay"
            pig_words.append(pig_word)
        else:
            pig_words.append(word)
    return ' '.join(pig_words)


if __name__ == '__main__':
    print(pig_it('Pig latin is cool'))
