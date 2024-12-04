#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize the dp array with a value greater than any possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make total of 0
    
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

