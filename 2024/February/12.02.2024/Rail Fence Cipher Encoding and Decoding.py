"""
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.

"""


def encode_rail_fence_cipher(string: str, n: int) -> str:
    if n < 2:
        return string
    fence = ['' for _ in range(n)]
    rail = 0
    direction = 1

    for char in string:
        fence[rail] += char
        rail += direction
        if rail == n - 1 or rail == 0:
            direction = -direction
        rail = max(0, min(rail, n - 1))

    return ''.join(fence)


def decode_rail_fence_cipher(encoded_text: str, n: int) -> str:
    if n < 2:
        return encoded_text

    cycle = 2 * (n - 1)
    result = [''] * len(encoded_text)
    index = 0

    for i in range(n):
        j = 0
        while i + j < len(encoded_text):
            result[i + j] += encoded_text[index]
            index += 1
            if i != 0 and i != n - 1 and j + cycle - i < len(encoded_text):
                result[j + cycle - i] += encoded_text[index]
                index += 1
            j += cycle

    return ''.join(result)


if __name__ == '__main__':
    print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
    print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))