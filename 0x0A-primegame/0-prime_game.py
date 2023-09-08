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
    isPrime = True
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
    return isPrime


def isWinner(x, nums):
    """Returns the name of the player
    that wins the most rounds of the prime game

    Args:
        x (int): rounds
        nums (list): array of n
    Returns:
        winner name: str
    """
    rounds = [list(range(1, i + 1)) for i in nums]
    Maria = 0
    Ben = 0
    Winner = None
    for i in range(x):
        round = rounds[i]
        count = 1
        round_iterator = iter((p for p in round if isPrime(p)))
        while True:
            prime = next(round_iterator, None)
            if prime is None:
                if count % 2 == 0:
                    Maria += 1
                else:
                    Ben += 1
                break
            count += 1
    if Maria > Ben:
        Winner = 'Maria'
    else:
        Winner = 'Ben'
    return Winner
