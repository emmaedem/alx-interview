#!/usr/bin/python3
"""
Module that determine fewest number of coins to make a given total amount.
"""


def makeChange(coins, total):
    """
    It determines fewest number of coins required to make a given total.

    Parameters:
    coins (list): A list of coin denominations.
    total (int): The amount to be made.

    Returns:
    int: The fewest number of coins needed to make the total.
         Returns -1 if it's not possible to make total with given coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
