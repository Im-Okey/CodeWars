"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

Good Work :)
"""

import re


def simplify(poly: str) -> str:
    """
    Simplifies a multilinear non-constant polynomial in integers coefficients.

    Parameters:
    -----------
    poly : str
        The input polynomial as a string.

    Returns:
    --------
    str
        The simplified polynomial as a string.
    """

    monomials = re.findall(r'[-+]?\d*[a-z]+', poly)
    monomial_dict = {}

    for monomial in monomials:
        match = re.match(r'([+-]?\d*)([a-z]+)', monomial)
        coeff, variables = match.groups() if match.groups()[0] else ('1', match.groups()[1])
        coeff = int(coeff) if coeff not in ['+', '-'] else 1 if not coeff.startswith('-') else -1
        variables = ''.join(sorted(variables))
        monomial_dict[variables] = monomial_dict.get(variables, 0) + coeff

    result = ''
    for vars in sorted(monomial_dict, key=lambda x: (len(x), x)):
        if monomial_dict[vars] != 0:
            if monomial_dict[vars] > 0 and result:
                result += '+'
            elif monomial_dict[vars] < 0:
                result += '-'
            if abs(monomial_dict[vars]) != 1:
                result += str(abs(monomial_dict[vars]))
            result += vars

    return result if result else '0'


if __name__ == '__main__':
    simplify("a+ca-ab")
