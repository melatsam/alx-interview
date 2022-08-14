#!/usr/bin/python3
'''Main file for testing'''


def makeChange(coins, total):

    dp = [0] * (sum + 1)

    for i in range(1, sum + 1):

        dp[i] = sys.maxsize

        for c in range(len(S)):
            if i - S[c] >= 0:
                result = dp[i - S[c]]

                if result != sys.maxsize:
                    dp[i] = min(dp[i], result + 1)

    return dp[sum]

