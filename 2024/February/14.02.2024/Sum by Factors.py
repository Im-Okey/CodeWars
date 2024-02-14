"""
Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_for_list(lst: list) -> list:
    primes = set()
    result = []

    for num in lst:
        n = abs(num)
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if is_prime(i):
                    primes.add(i)
        if n > 1 and is_prime(n):
            primes.add(n)

    for prime in sorted(primes):
        sum_of_factors = sum(num for num in lst if num % prime == 0)
        result.append([prime, sum_of_factors])

    return result


if __name__ == '__main__':
    sum_for_list([12, 15])
