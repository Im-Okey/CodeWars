"""
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency


"""


def dbl_linear(n: int) -> int:
    u = [1]
    ix, iy = 0, 0  # Инициализация индексов для x и y
    while len(u) <= n:
        next_x, next_y = 2*u[ix] + 1, 3*u[iy] + 1
        if next_x < next_y:
            u.append(next_x)
            ix += 1
        elif next_x > next_y:
            u.append(next_y)
            iy += 1
        else:
            u.append(next_x)
            ix += 1
            iy += 1
    return u[n]


if __name__ == '__main__':
    dbl_linear(10)
