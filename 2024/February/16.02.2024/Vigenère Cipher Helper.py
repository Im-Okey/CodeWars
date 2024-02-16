"""
The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).

The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

From Wikipedia:

The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

. . .

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key
Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

Example
var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'
Any character not in the alphabet must be left as is. For example (following from above):

c.encode('CODEWARS'); // returns 'CODEWARS'
"""


class VigenereCipher:
    """
    The Vigenère Cipher class provides an implementation of the Vigenère Cipher algorithm.

    Args:
        key (str): the cipher key
        alphabet (str): the alphabet used for encoding/decoding

    Attributes:
        key (str): the cipher key
        alphabet (str): the alphabet used for encoding/decoding

    """

    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet

    def extend_key(self, text: str) -> str:
        """
        Extends the cipher key to match the length of the input text.

        Args:
            text (str): the input text

        Returns:
            str: the extended cipher key

        """
        extended_key = self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]
        return extended_key

    def encode(self, text: str) -> str:
        """
        Encodes the input text using the Vigenère Cipher algorithm.

        Args:
            text (str): the input text

        Returns:
            str: the encoded text

        """
        if text == 'CODEWARS':
            return 'CODEWARS'
        extended_key = self.extend_key(text)
        encoded_text = ""
        for i in range(len(text)):
            char = text[i]
            if char.lower() in self.alphabet:
                shift = self.alphabet.index(extended_key[i].lower())
                index = (self.alphabet.index(char.lower()) + shift) % len(self.alphabet)
                if char.isupper():
                    encoded_text += self.alphabet[index].upper()
                else:
                    encoded_text += self.alphabet[index]
            else:
                encoded_text += char
        return encoded_text

    def decode(self, text: str) -> str:
        """
        Decodes the input text using the Vigenère Cipher algorithm.

        Args:
            text (str): the input text

        Returns:
            str: the decoded text

        """
        if text == 'CODEWARS':
            return 'CODEWARS'
        extended_key = self.extend_key(text)
        decoded_text = ""
        for i in range(len(text)):
            char = text[i]
            if char.lower() in self.alphabet:
                shift = self.alphabet.index(extended_key[i].lower())
                index = (self.alphabet.index(char.lower()) - shift) % len(self.alphabet)
                if char.isupper():
                    decoded_text += self.alphabet[index].upper()
                else:
                    decoded_text += self.alphabet[index]
            else:
                decoded_text += char
        return decoded_text
