#!/usr/bin/python3
"""Module contains a function isWinner that
returns the name of the winner of multiple rounds of
the prime game"""


def isPrime(n):
    """Test if a number is prime
    Args:
        n (int): number to test
    Returns:
        Bool: True or False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Returns the name of the player
    that wins the most rounds of the prime game

    Args:
        x (int): rounds
        nums (list): array of n
    Returns:
        winner name: str
    """
    rounds = [iter((n for n in range(i + 1) if isPrime(n))) for i in nums]
    Maria = 0
    Ben = 0
    Winner = None
    for i in range(x):
        count = 1
        while True:
            prime = next(rounds[i], None)
            if prime is None:
                if count % 2 == 0:
                    Maria += 1
                else:
                    Ben += 1
                break
            count += 1
    if Maria > Ben:
        Winner = 'Maria'
    if Ben > Maria:
        Winner = 'Ben'
    return Winner
