#!/usr/bin/python3
'''Main file for testing'''


def makeChange(coins, total):
    matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix

# Function we'll use to optimize the default above matrix
def makeChange(coins, total):
    matrix = _change_matrix(coins, change)
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):

            if coins[c-1] == r:
                matrix[c][r] = 1

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

    return matrix[-1][-1]
