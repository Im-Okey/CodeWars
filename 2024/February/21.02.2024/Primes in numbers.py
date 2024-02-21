"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def prime_factors(n: int) -> str:
    i, factors = 2, {}
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return ''.join(['({}{})'.format(k, '**'+str(v) if v > 1 else '') for k, v in sorted(factors.items())])


if __name__ == '__main__':
    prime_factors(7775460)
