def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Parameters:
        coins (list of int): A list of the values of the coins in your possession.
            Each coin value is a positive integer.
        total (int): The target amount you want to reach using the fewest number
            of coins.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
            - Returns 0 if the total is 0 or less.
            - Returns -1 if the total cannot be met by any combination of the
              coins.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each
    # amount up to 'total'. We use 'float('inf')' to represent an initial state
    # where the amount cannot be reached.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: Zero coins are needed to make a total of 0.

    # Loop through all amounts from 1 to 'total' to build up the solution.
    for amount in range(1, total + 1):
        # Check each coin to see if it can contribute to the current amount.
        for coin in coins:
            if coin <= amount:
                # Update dp[amount] with the minimum number of coins needed.
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still 'inf', the amount cannot be formed with given coins.
    return dp[total] if dp[total] != float('inf') else -1
