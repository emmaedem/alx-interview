#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """To generate list that tells if a number is prime up to max_n."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime


def prime_count_up_to_n(max_n, is_prime):
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """This determines who is the winner after x rounds."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    prime_count = prime_count_up_to_n(max_n, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
