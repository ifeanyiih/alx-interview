#!/usr/bin/python3
"""This module simulates an interview question"""


def canUnlockAll(boxes):
    """Function is determines if all boxes can be opened
    A box is a list of lists
    A key with the same number as a box opens that box
    The first box boxes[0] is unlocked

    Args:
        boxes (list): a list of lists
    Returns:
        bool: return True if all boxes can be opened
        bool: return False otherwise
    """
    unlocked = {0}
    keys = {0}
    locked = []
    for i in range(len(boxes)):
        if i in keys:
            unlocked.add(i)
            for n in boxes[i]:
                keys.add(n)
        else:
            locked.append(i)

    for k in locked:
        if k in keys:
            unlocked.add(k)
            for n in boxes[k]:
                keys.add(n)

    locked = [n for n in locked if n not in keys]
    if len(unlocked) == len(boxes):
        return True
    return False
