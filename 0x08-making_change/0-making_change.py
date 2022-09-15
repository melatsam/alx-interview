#!/usr/bin/python3
"""fewest number of coins needed to meet"""


def makeChange(coins, total):
    """the value of coin will always be an integer greater than 0
    you can assume you have an infinite number of each denomination of coin"""
    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1
