import numpy as np


def least_cost_method(supply, demand, cost):
    supply = supply.copy()
    demand = demand.copy()
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols), dtype=int)

    while np.sum(allocation) != np.sum(supply):
        min_value = float('inf')
        min_pos = (0, 0)
        
        # Найти минимальный элемент в матрице стоимости
        for i in range(rows):
            for j in range(cols):
                if cost[i][j] < min_value and supply[i] > 0 and demand[j] > 0:
                    min_value = cost[i][j]
                    min_pos = (i, j)
        
        i, j = min_pos
        
        # Распределить как можно больше на найденную позицию
        allocation_amount = min(supply[i], demand[j])
        allocation[i][j] = allocation_amount
        supply[i] -= allocation_amount
        demand[j] -= allocation_amount
        
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

allocation = least_cost_method(supply, demand, cost)
print_result(allocation, cost)
