#!/usr/bin/python3
'''Main file for testing'''


def makeChange(coins: List[int], total: int, solutions: List[int]) -> int:
    if total < 0:
        return -1
    if total == 0:
        return 0

    if coin[total - 1] != 0:
        return solutions[total - 1]

    optimal_solution = float('inf')

    for coin in coins:
        best_solution_for_coin = coin_change_sub(coins, total - coin, solutions)
        if 0 <= best_solution_for_coin < optimal_solution:
            optimal_solution = best_solution_for_coin + 1

    if optimal_solution == float('inf'):
        solutions[total - 1] = -1
    else:
        solutions[total - 1] = optimal_solution

    return solutions[total - 1]
    return -1
