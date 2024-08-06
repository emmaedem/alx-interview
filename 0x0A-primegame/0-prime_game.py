#!/usr/bin/python3

def sieve_of_eratosthenes(n):

    primes = [True] * (n + 1)

    p = 2

    while p * p <= n:

        if primes[p] == True:

            for i in range(p * p, n + 1, p):

                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n + 1) if primes[p]]

    return prime_numbers

def isWinner(x, nums):

    max_n = max(nums)

    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0

    ben_wins = 0
    
    for n in nums:

        prime_set = primes[:]

        current_player = "Maria"

        available_numbers = set(range(1, n + 1))
        
        while True:

            move_made = False

            for p in prime_set:

                if p in available_numbers:

                    available_numbers -= set(range(p, n + 1, p))

                    move_made = True

                    break
            
            if not move_made:

                if current_player == "Maria":

                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            current_player = "Ben" if current_player == "Maria" else "Maria"
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

