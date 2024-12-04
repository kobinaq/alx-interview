#!/usr/bin/python3

  """
    Determine the fewest number of coins needed to meet a given total amount.

    Parameters:
    coins (list of int): A list of the values of the coins in your possession.
                         Each coin value is a positive integer.
    total (int): The target amount you want to reach using the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total amount.
         - Returns 0 if the total is 0 or less.
         - Returns -1 if the total cannot be met by any combination of the coins.

    """

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

