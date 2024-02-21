"""
We want to create a function that will add numbers together when called in succession.

add(1)(2) # equals 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3) # 6
add(1)(2)(3)(4); # 10
add(1)(2)(3)(4)(5) # 15
and so on.

A single call should be equal to the number passed in.

add(1) # 1
We should be able to store the returned values and reuse them.

addTwo = add(2)
addTwo # 2
addTwo + 5 # 7
addTwo(3) # 5
addTwo(3)(5) # 10
We can assume any number being passed in will be valid whole number.
"""


class AddChain:
    def __init__(self, value=0):
        self.value = value

    def __call__(self, num):
        if isinstance(num, AddChain):
            return AddChain(self.value + num.value)
        else:
            return AddChain(self.value + num)

    def __add__(self, num):
        return self.value + num

    def __eq__(self, other):
        return self.value == other


def add(num: int) -> AddChain:
    return AddChain(num)


if __name__ == '__main__':
    add(1)(2)(3)
