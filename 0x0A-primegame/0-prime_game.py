#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Generate a list of primes up to n using the Sieve of Eratosthenes. """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    prime_counts = [0] * (n + 1)
    count = 0
    
    for i in range(2, n + 1):
        if primes[i]:
            count += 1
        prime_counts[i] = count
    
    return prime_counts

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_counts = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

