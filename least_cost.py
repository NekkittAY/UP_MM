import numpy as np


def transportation_cost(supply, demand, costs):
    num_suppliers = len(supply)
    num_customers = len(demand)
    
    supply_remaining = np.array(supply)
    demand_remaining = np.array(demand)
    allocation = np.zeros((num_suppliers, num_customers))
    
    while np.sum(supply_remaining) > 0:
        supplier_index = np.argmax(supply_remaining)
        customer_index = np.argmax(demand_remaining)

        quantity = min(supply_remaining[supplier_index], demand_remaining[customer_index])
        
        allocation[supplier_index, customer_index] = quantity
        supply_remaining[supplier_index] -= quantity
        demand_remaining[customer_index] -= quantity
    
    total_cost = np.sum(allocation * costs)
    
    return allocation, total_cost


cost = np.array([
    [24, 36, 28, 16, 33],
    [42, 52, 38, 22, 46],
    [14, 58, 22, 34, 36],
    [20, 34, 40, 52, 37]
])

supply = [125, 240, 75, 330]
demand = [150, 245, 70, 340, 220]
 
allocation, total_cost = transportation_cost(supply, demand, cost)
 
print("Optimal Allocation:")
print(allocation)
print("Total Cost:", total_cost)
