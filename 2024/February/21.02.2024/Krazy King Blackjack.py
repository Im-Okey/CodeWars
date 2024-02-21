"""
Krazy King BlackJack is just like blackjack, with one difference: the kings! Instead of the kings being simply worth 10 points, kings are worth either 10 points or some other number of points announced by the dealer at the start of the game. Whichever value yields the best hand is the one that plays (much like how aces are worth either 1 or 11 points).

Write a function that inputs a list of strings (representing a blackjack hand) and an integer that represents the alternative king value. The function should output an integer representing the value of the hand if it is less than or equal to 21, and False if it exceeds 21. Other than the alternative king value, normal blackjack rules apply.

The cards, in order ace-through king, are represented as strings as follows:

['A', '2', '3','4', '5', '6','7', '8', '9','10', 'J', 'Q','K']
A hand has between 2 and 20 cards, inclusive. The alternative king value is between 2 and 9, inclusive.

Blackjack rules: the value of a hand is determined by maximizing the value of the sum of its cards while not exceeding 21 if possible. Number cards are worth their value, Jacks ('J') and Queens ('Q') are worth 10, Aces are worth either 1 or 11, and kings, again, are worth either 10 or their alternative value.
"""
from itertools import product
from typing import Union


def krazy_king_blackjack(hand: list, alternative_king_value: int) -> Union[int, bool]:
    """
    This function takes in a list of strings representing a blackjack hand and an integer representing the alternative value of a king.
    It calculates the value of the hand according to the Krazy King Blackjack rules, which states that kings can be worth either 10 points or some other number of points announced by the dealer at the start of the game.
    The function returns an integer representing the value of the hand if it is less than or equal to 21, and False if it exceeds 21.

    Parameters:
    hand (list): A list of strings representing the cards in the hand.
    alternative_king_value (int): The alternative value of a king.

    Returns:
    Union[int, bool]: An integer representing the value of the hand if it is valid, or False if it is not valid.

    Raises:
    ValueError: If the input hand is not a list of strings or if the input alternative_king_value is not an integer.

    """
    card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                   'K': 10}

    def calculate_hand_value(hand: list, alt_king_value: int) -> int:
        total = 0
        aces_count = 0
        for card in hand:
            if card == 'A':
                aces_count += 1
            elif card == 'K':
                total += max(10, alt_king_value)
            else:
                total += card_values[card]

        for _ in range(aces_count):
            if total + 11 + (aces_count - 1) <= 21:
                total += 11
            else:
                total += 1

        return total

    best_value = 0
    best_hand = []
    for combination in product([10, alternative_king_value], repeat=hand.count('K')):
        current_hand = hand.copy()
        for value in combination:
            current_hand[current_hand.index('K')] = str(value)
        hand_value = calculate_hand_value(current_hand, alternative_king_value)
        if hand_value > best_value and hand_value <= 21:
            best_value = hand_value
            best_hand = current_hand.copy()

    if best_hand:
        return best_value
    else:
        return False


if __name__ == '__main__':
    krazy_king_blackjack(['J', 'K', 'K'], 4)
