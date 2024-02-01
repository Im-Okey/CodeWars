"""
So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken one or more of the chairs!! You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in use.

Your meeting room can take up to 8 chairs. need will tell you how many have been taken. You need to find that many.

Find the spare chairs from the array of meeting rooms. Each meeting room tuple will have the number of occupants as a string. Each occupant is represented by 'X'. The room tuple will also have an integer telling you how many chairs there are in the room.

You should return an array of integers that shows how many chairs you take from each room in order, up until you have the required amount.

example:

[['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9], ['XXX',2]] when you need 4 chairs:

result -> [0, 1, 3] no chairs free in room 0, take 1 from room 1, take 3 from room 2. no need to consider room 3 as you have your 4 chairs already.

If you need no chairs, return "Game On". If there aren't enough spare chairs available, return "Not enough!".
"""


def meeting(rooms: list, need: int) -> (list, str):
    chair_from_rooms = []
    if need == 0:
        return 'Game On'
    for room in rooms:
        if len(room[0]) < room[1] and need != 0:
            if room[1] - len(room[0]) <= need:
                need -= room[1] - len(room[0])
                chair_from_rooms.append(room[1] - len(room[0]))
            else:
                chair_from_rooms.append(need)
                need = 0
        else:
            if need != 0:
                chair_from_rooms.append(0)
            continue
    if not need:
        return chair_from_rooms
    else:
        return 'Not enough!'


if __name__ == '__main__':
    print(meeting([['XXXXXXXXX', 9], ['XXXXXXX', 4], ['XXXXXX', 10], ['XXXXXX', 6], ['XXXXX', 0], ['XXXX', 8], ['XXXXXXXX', 4], ['', 10]], 3))
