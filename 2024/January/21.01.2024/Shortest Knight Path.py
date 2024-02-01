"""
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)


"""


def knight(start: str, end: str) -> int:
    start_row, start_col = 8 - int(start[1]), ord(start[0]) - 97
    end_row, end_col = 8 - int(end[1]), ord(end[0]) - 97

    delta_x = abs(start_row - end_row)
    delta_y = abs(start_col - end_col)

    if (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1):
        return 1
    else:
        board = [[0] * 8 for _ in range(8)]
        queue = [(start_row, start_col, 0)]
        while queue:
            r, c, d = queue.pop(0)
            if r == end_row and c == end_col:
                return d
            for dr, dc in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
                nr, nc = r + dr, c + dc
                if 8 > nr >= 0 == board[nr][nc] and 0 <= nc < 8:
                    board[nr][nc] = 1
                    queue.append((nr, nc, d + 1))


if __name__ == '__main__':
    print(knight('a1', 'c1'))
