"""
In this task you have to code process planner.

You will be given initial thing, target thing and a set of processes to turn one thing into another (in the form of [process_name, start_thing, end_thing]). You must return names of shortest sequence of processes to turn initial thing into target thing, or empty sequence if it's impossible.

If start already equals end, return [], since no path is required.

Example:

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
];

processes('field', 'bread', test_processes) # should return ['gather', 'mill', 'bake']
processes('field', 'ferrari', test_processes) # should return []
processes('field', 'field', test_processes) # should return [], since no processes are needed
Good luck!
"""


from collections import deque
from typing import List


def processes(start_thing: str, end_thing: str, processes_list: List[List[str]]) -> List[str]:
    """
    This function takes in an initial thing, a target thing, and a list of processes that transform one thing into another. It returns the shortest sequence of processes to turn the initial thing into the target thing, or an empty list if it is impossible.

    If the start_thing is equal to the end_thing, the function returns an empty list, since no processes are required.

    Parameters:
    start_thing (str): The initial thing to be transformed.
    end_thing (str): The target thing to be transformed into.
    processes_list (List[List[str]]): A list of processes, where each process is a list containing the name of the process, the starting thing for the process, and the ending thing for the process.

    Returns:
    List[str]: The shortest sequence of processes to turn the initial thing into the target thing, or an empty list if it is impossible.
    """

    if start_thing == end_thing:
        return []

    process_map = {}
    for process in processes_list:
        if process[1] not in process_map:
            process_map[process[1]] = []
        process_map[process[1]].append((process[0], process[2]))

    queue = deque([(start_thing, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end_thing:
            return path
        if current in visited:
            continue
        visited.add(current)
        if current in process_map:
            for p, next_thing in process_map[current]:
                queue.append((next_thing, path + [p]))

    return []


test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
]


if __name__ == '__main__':
    processes('gather', 'field', test_processes)



