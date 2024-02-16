"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""


class Sudoku(object):
    """
       A class to represent a Sudoku puzzle.

       Parameters
       ----------
       data : list of lists
           A 2-dimensional list representing the Sudoku puzzle, where each sublist represents a row of the puzzle.

       Attributes
       ----------
       data : list of lists
           The Sudoku puzzle represented as a 2-dimensional list.

       Methods
       -------
       is_valid()
           Returns True if the Sudoku puzzle is valid, False otherwise.

       """
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        n = len(self.data)
        sqrt_n = int(n ** 0.5)

        if n != sqrt_n * sqrt_n:
            return False

        for row in self.data:
            if len(row) != n:
                return False
            for value in row:
                if not isinstance(value, int) or value < 1 or value > n or isinstance(value, bool):
                    return False

        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                if self.data[i][j] in row_set or self.data[j][i] in col_set:
                    return False
                row_set.add(self.data[i][j])
                col_set.add(self.data[j][i])

        for i in range(0, n, sqrt_n):
            for j in range(0, n, sqrt_n):
                subgrid_set = set()
                for k in range(sqrt_n):
                    for l in range(sqrt_n):
                        if self.data[i + k][j + l] in subgrid_set:
                            return False
                        subgrid_set.add(self.data[i + k][j + l])

        return True