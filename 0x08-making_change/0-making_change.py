#!/usr/bin/python3
'''Main file for testing'''


def makeChange(coins, total: List[int], amount: int) -> int:
    dp = []
    for i in range(amount + 1):
        dp.append(float('inf'))
    dp[0] = 0
    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1
