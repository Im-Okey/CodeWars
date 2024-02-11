"""
Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)
Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested.
"""

from itertools import permutations


def latest_clock(*args: int) -> str:
    max_time = -1
    for h1, h2, m1, m2 in permutations(args):
        hours = h1 * 10 + h2
        mins = m1 * 10 + m2
        if 0 <= hours < 24 and 0 <= mins < 60:
            max_time = max(max_time, hours * 60 + mins)
    if max_time == -1:
        return "Invalid input"
    else:
        hours, mins = divmod(max_time, 60)
        return f"{hours:02d}:{mins:02d}"


if __name__ == "__main__":
    print(latest_clock(9, 1, 2, 5))
