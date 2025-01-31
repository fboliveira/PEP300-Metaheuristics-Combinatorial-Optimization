import random

def createRandom(dimension, capacity, demand):

    customers = [*range(2, dimension + 1)] #
    random.shuffle(customers)

    # Depot is the first and the last in route
    solution = [[1]]
    j = 0
    sum_demand = 0
    
    for i in range(len(customers)):

        customer = customers[i]
        customer_demand = demand[ customer - 1 ]

        if customer_demand + sum_demand > capacity:
            # A new route is created
            # Depot is the first and the last in route
            solution[j].append(1)
            solution.append([1])
            sum_demand = 0
            j+=1

        # Add customer to the route j
        solution[j].append(customer)
        sum_demand += customer_demand

    # Check if the last position of the last route is the depot
    if solution[-1][-1] != 1:
        solution[-1].append(1)

    return solution