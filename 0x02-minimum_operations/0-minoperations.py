#!/usr/bin/python3
"""
IF n is impossible to achieve,return 0
"""


def minOperations(n):
    """
    RETURNS an integer
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
