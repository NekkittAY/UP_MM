import numpy as np

def northwest_corner_method(supply, demand):
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


def calculate_potentials(allocation, cost):
    u = [None] * len(cost)
    v = [None] * len(cost[0])
    u[0] = 0
    
    while None in u or None in v:
        for i in range(len(cost)):
            for j in range(len(cost[i])):
                if allocation[i][j] > 0:
                    if u[i] is not None and v[j] is None:
                        v[j] = cost[i][j] - u[i]
                    elif u[i] is None and v[j] is not None:
                        u[i] = cost[i][j] - v[j]
    
    return u, v


def find_entering_variable(allocation, cost, u, v):
    min_value = 0
    entering_variable = None
    
    for i in range(len(cost)):
        for j in range(len(cost[i])):
            if allocation[i][j] == 0 and (u[i] + v[j] < cost[i][j]):
                value = cost[i][j] - (u[i] + v[j])
                if value < min_value:
                    min_value = value
                    entering_variable = (i, j)
    
    return entering_variable


def find_loop(allocation, entering_variable):
    rows, cols = len(allocation), len(allocation[0])
    loop = []
    loop.append(entering_variable)
    
    def find_path(start, direction, visited):
        if direction == 'horizontal':
            for j in range(cols):
                if allocation[start[0]][j] > 0 or (start[0], j) == entering_variable:
                    if (start[0], j) not in visited:
                        visited.append((start[0], j))
                        find_path((start[0], j), 'vertical', visited)
        elif direction == 'vertical':
            for i in range(rows):
                if allocation[i][start[1]] > 0 or (i, start[1]) == entering_variable:
                    if (i, start[1]) not in visited:
                        visited.append((i, start[1]))
                        find_path((i, start[1]), 'horizontal', visited)
    
    find_path(entering_variable, 'horizontal', loop)
    return loop


def adjust_allocation(allocation, loop):
    positions = loop[1::2]
    min_value = min(allocation[i][j] for i, j in positions)
    
    for k, (i, j) in enumerate(loop):
        if k % 2 == 0:
            allocation[i][j] += min_value
        else:
            allocation[i][j] -= min_value
    
    return allocation


def transportation_problem(supply, demand, cost):
    allocation = northwest_corner_method(supply, demand)
    
    while True:
        u, v = calculate_potentials(allocation, cost)
        entering_variable = find_entering_variable(allocation, cost, u, v)
        
        if entering_variable is None:
            break
        
        loop = find_loop(allocation, entering_variable)
        allocation = adjust_allocation(allocation, loop)
    
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

allocation = transportation_problem(supply, demand, cost)
print_result(allocation, cost)
