"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""


def balanced_parens(n):
    """
    This function generates all possible ways to balance n pairs of parentheses.

    Parameters:
    n (int): The number of pairs of parentheses to balance.

    Returns:
    A list of strings, where each string represents a way to balance the parentheses.

    Examples:
    >>> balanced_parens(0)
    ['']
    >>> balanced_parens(1)
    ['()']
    >>> balanced_parens(2)
    ['()()', '(())']
    >>> balanced_parens(3)
    ['()()()', '(())()', '()(())', '(()())', '((()))']
    """
    def generate(s, left, right, result):
        """
        This function generates all possible combinations of left and right parentheses,
        and appends them to the result list.

        Parameters:
        s (str): The current string of parentheses.
        left (int): The number of left parentheses.
        right (int): The number of right parentheses.
        result (list): The list of strings to append to.
        """
        if left == 0 and right == 0:
            # If we have reached a balanced state, append the current string to the result list.
            result.append(s)
        if left > 0:
            # If there are still left parentheses, recursively generate all possible combinations
            # with one fewer left parentheses.
            generate(s + '(', left - 1, right, result)
        if right > left:
            # If there are still right parentheses, recursively generate all possible combinations
            # with one fewer right parentheses.
            generate(s + ')', left, right - 1, result)

    result = []
    # Call the recursive generate function with the initial state of empty parentheses and the
    # desired number of parentheses to balance.
    generate('', n, n, result)
    return result


if __name__ == '__main__':
    balanced_parens(3)
