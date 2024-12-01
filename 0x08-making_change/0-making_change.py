#!/usr/bin/python3
"""0-making_change module"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total.
    """
    # Edge case: If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize dp array with a value larger than the maxi possible coin count
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate through all the coin denominations
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made
    return dp[total] if dp[total] != float('inf') else -1
