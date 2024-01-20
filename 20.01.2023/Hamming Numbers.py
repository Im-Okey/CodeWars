"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.

Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) Hamming numbers without timing out.
"""


def hamming(n: int):
    hamming = [1]
    i, j, k = 0, 0, 0

    while len(hamming) < n:
        next_hamming = min(hamming[i] * 2, hamming[j] * 3, hamming[k] * 5)
        if next_hamming == hamming[i] * 2:
            i += 1
        if next_hamming == hamming[j] * 3:
            j += 1
        if next_hamming == hamming[k] * 5:
            k += 1
        hamming.append(next_hamming)

    return hamming[-1]


if __name__ == '__main__':
    print(hamming(1))
