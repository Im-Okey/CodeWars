"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
from typing import Union


def generate_hashtag(s: str) -> Union[str, bool]:
    if not s or len(s.strip()) == 0:
        return False

    hashtag = '#' + ''.join(word.capitalize() for word in s.split())

    return hashtag if len(hashtag) <= 140 else False


if __name__ == '__main__':
    generate_hashtag('Codewars')
