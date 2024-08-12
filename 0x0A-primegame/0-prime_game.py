#!/usr/bin/python3

def sieve_of_eratosthenes(n):
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

        primes_in_range = [p for p in primes if p <= n]
        moves = 0

        while primes_in_range:
            moves += 1
            prime = primes_in_range[0]
            primes_in_range = [p for p in primes_in_range if p % prime != 0]

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
