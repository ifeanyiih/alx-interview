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

    for n in locked:
        if n in keys:
            for m in boxes[n]:
                keys.add(m)
            unlocked.add(n)
            locked.remove(n)
    # print('Unlocked', unlocked)
    # print('Locked', locked)
    # print('Keys', keys)
    if len(keys) == len(boxes):
        return True
    return False
