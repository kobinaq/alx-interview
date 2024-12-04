#!/usr/bin/python3

def makeChange(coins, total):
"""
    Determine the fewest number of coins needed to meet a given total amount.

"""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount up to 'total'.
    # We use 'float('inf')' to represent an initial state where the amount cannot be reached.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: Zero coins are needed to make a total of 0.

    # Loop through all amounts from 1 to 'total' to build up the solution.
    for amount in range(1, total + 1):
        # Check each coin to see if it can contribute to the current amount.
        for coin in coins:
            if coin <= amount:
                # If the coin value is less than or equal to the current amount,
                # update the dp array with the minimum number of coins needed.
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still 'inf', it means the amount cannot be formed with the given coins.
    return dp[total] if dp[total] != float('inf') else -1

