"""
Connect Four
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]
The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.
"""
from typing import List


def who_is_winner(pieces_position_list: List[str]):
    """
    This function takes a list of strings that represent the positions of the pieces on the board, and determines
    who the winner is based on the Connect Four rules.

    Parameters:
    pieces_position_list (List[str]): A list of strings that represent the positions of the pieces on the board, in the format of "column_letter_piece_color".

    Returns:
    str: The color of the player who won the game, or "Draw" if the game ended in a draw.

    """
    grid = [[' ' for _ in range(7)] for _ in range(6)]

    def check_winner(row, col, player):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # horizontal, vertical, diagonal
        for dr, dc in directions:
            r, c = row, col
            count = 1
            for _ in range(3):
                r, c = r + dr, c + dc
                if 0 <= r < 6 and 0 <= c < 7 and grid[r][c] == player:
                    count += 1
                else:
                    break
            r, c = row, col
            for _ in range(3):
                r, c = r - dr, c - dc
                if 0 <= r < 6 and 0 <= c < 7 and grid[r][c] == player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

    players = {'A': 'Red', 'B': 'Yellow', 'C': 'Red', 'D': 'Yellow', 'E': 'Red', 'F': 'Yellow', 'G': 'Red'}

    for move in pieces_position_list:
        col, player = move.split('_')
        col_num = ord(col) - ord('A')
        if col in players:
            for row in range(5, -1, -1):
                if grid[row][col_num] == ' ':
                    grid[row][col_num] = player
                    if check_winner(row, col_num, player):
                        return player
                    break
    return "Draw"


if __name__ == '__main__':
    who_is_winner([
        "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
        "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
        "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
    ])
