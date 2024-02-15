"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""

from collections import deque
from typing import List


class Node:
    """
    A class to represent a node in a binary tree.

    Parameters:
        L (Node): The left child of the node.
        R (Node): The right child of the node.
        n (int): The value of the node.
    """

    def __init__(self, L=None, R=None, n=None):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(root: Node) -> List[int]:
    """
    Returns a list of elements in a binary tree by levels, where the root element comes first, then the root's children in left-to-right order, and so on.

    Parameters:
        root (Node): The root of the binary tree.

    Returns:
        List[int]: The list of elements in the binary tree by levels.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':
    tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))
