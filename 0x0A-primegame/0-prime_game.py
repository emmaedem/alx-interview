#!/usr/bin/python3
"""
Module 0-prime_game

This module contains a function to determine the winner of the
prime number game played between Maria and Ben.
"""


def sieve_of_eratosthenes(n):
    """
    Generates all prime numbers up to a given number n using
    the Sieve of Eratosthenes algorithm.

    Parameters:
    n (int): The upper limit to generate prime numbers.

    Returns:
    list: A list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime number game played between
    Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the upper limit of
    the numbers in each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
    None: If there is no winner.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        primes_in_range = [
            p for p in primes if p <= n
        ]
        moves = 0

        while primes_in_range:
            moves += 1
            prime = primes_in_range[0]
            primes_in_range = [
                p for p in primes_in_range if p % prime != 0
            ]

        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
