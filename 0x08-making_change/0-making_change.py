#!/usr/bin/python3

def makeChange(coins, total):
    count = 0
    rem = total
    sortDesc = sorted(coins, reverse=True)
    if total <= 0:
        return 0

    while rem > 0:
        for coin in sortDesc:
            rel = rem // coin
            rem = rem % coin
            count += rel
            if rel == 0 and rem != 0:
                return -1

    return count
