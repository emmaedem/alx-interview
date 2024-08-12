#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    
    return prime_count

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    prime_count = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
