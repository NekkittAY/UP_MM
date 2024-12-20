import numpy as np


def northwest_corner_method(supply, demand, cost):
    supply = supply.copy()
    demand = demand.copy()
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols), dtype=int)

    i = j = 0
    while i < rows and j < cols:
        if supply[i] < demand[j]:
            allocation[i][j] = supply[i]
            demand[j] -= supply[i]
            i += 1
        else:
            allocation[i][j] = demand[j]
            supply[i] -= demand[j]
            j += 1

    return allocation


def print_result(allocation, cost):
    total_cost = 0
    for i in range(len(allocation)):
        for j in range(len(allocation[i])):
            total_cost += allocation[i][j] * cost[i][j]
    print("Allocation Matrix:")
    print(allocation)
    print(f"Total Transportation Cost: {total_cost} руб.")


# Данные из таблицы
cost = np.array([
    [24, 36, 28, 16, 33],
    [42, 52, 38, 22, 46],
    [14, 58, 22, 34, 36],
    [20, 34, 40, 52, 37]
])

supply = [125, 240, 75, 330]
demand = [150, 245, 70, 340, 220]

allocation = northwest_corner_method(supply, demand, cost)
print_result(allocation, cost)
