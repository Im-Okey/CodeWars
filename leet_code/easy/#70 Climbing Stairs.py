"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


if __name__ == '__main__':
    print(climbStairs(44))
