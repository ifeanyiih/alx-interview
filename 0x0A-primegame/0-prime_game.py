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
    if n == 1:
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
        odd = 0
        even = 0
        count = 1
        while True:
            prime = False
            for n in round:
                if isPrime(n):
                    prime = True
                    val = n
                    round = list(filter(lambda n: (n % val) != 0, round))
                    if (count % 2) != 0:
                        odd += 1
                    else:
                        even += 1
                    break
                else:
                    continue
            if prime is False:
                if (count % 2) == 0:
                    even -= 1
                else:
                    odd -= 1
                break
            count += 1
        if odd > even:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        Winner = 'Maria'
    else:
        Winner = 'Ben'
    return Winner
