#!/usr/bin/python3
'''Main file for testing'''


def makeChange(coins, total: List[int], total: int) -> int:
    dp = []
    for i in range(total + 1):
        dp.append(float('inf'))
    dp[0] = 0
    for coin in range(1, total + 1):
        for coin in coins:
            if coin <= 0:
                dp[a] = min(dp[a], dp[a-coin]+1)
    return dp[total] if dp[total] != float('inf') else -1
