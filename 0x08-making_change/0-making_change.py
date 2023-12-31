#!/usr/bin/python3
"""Making Change Interview question"""


def makeChange(coins: list, total: int) -> int:
    """Determine the fewest number of coins
    needed to meet a given total amount"""
    count = 0
    rem = total
    sortDesc = sorted(coins, reverse=True)
    if total <= 0:
        return 0
    for coin in sortDesc:
        rel = rem // coin
        if rel <= 0:
            continue
        rem = rem % coin
        count += rel
    if rem > 0:
        return -1
    return count
