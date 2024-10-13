#!/usr/bin/python3
"""DSA mODULE
"""
def makeChange(coins, total):
    """ Determine the fewest number of coins needed to meet a given total.
    
    Parameters:
    - coins: List of integers, where each integer represents the value of a coin denomination available.
    - total: Integer representing the target total amount to be achieved using the fewest number of coins.
    
    Returns:
    - Integer representing the minimum number of coins needed to meet the total.
    - If the total is 0 or less, the function returns 0.
    - If it is impossible to meet the total with the given coins, the function returns -1.
    """
    if total <= 0:
        return 0
    
    # Create a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0
    
    # Iterate through each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means we can't make the total with the coins
    return dp[total] if dp[total] != float('inf') else -1

