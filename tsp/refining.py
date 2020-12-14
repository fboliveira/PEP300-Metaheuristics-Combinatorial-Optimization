import random
import problem

def firstImprovementDescent(dimension, distances, solution):

    cost = problem.calculateCost(solution, distances)
    improvement = True

    while improvement: # Local optimal

        improvement = False

        for i in range(dimension - 1): # 0 -> n-1
            for j in range(i + 1, dimension): # i + 1 -> n
                swap(solution, i, j)
                # New cost
                # The best operation -> perform delta cost
                neighbourCost = problem.calculateCost(solution, distances)

                if neighbourCost < cost:
                    # Move to the neighbour
                    print("Melhora: de ", cost, " para ", neighbourCost)
                    cost = neighbourCost
                    improvement = True
                    break
                else:
                    # The movement is undone
                    swap(solution, i, j)

            if improvement:
                break
    
    return solution, cost

def bestImprovementDescent(dimension, distances, solution):
    
    cost = problem.calculateCost(solution, distances)
    improvement = True

    while improvement: # Local optimal

        improvement = False
        bestI = -1
        bestJ = -1
        bestNeighbourCost = cost

        for i in range(dimension - 1):
            for j in range(i + 1, dimension):
                swap(solution, i, j)
                # New cost
                # The best operation -> perform delta cost
                neighbourCost = problem.calculateCost(solution, distances)

                if neighbourCost < bestNeighbourCost:
                    # Move to the neighbour
                    bestI = i
                    bestJ = j
                    bestNeighbourCost = neighbourCost
                    improvement = True

                # The movement is undone
                swap(solution, i, j)

        if improvement:
            # Best neighbour
            swap(solution, bestI, bestJ)
            cost = bestNeighbourCost
            print("Melhora: de ", cost, " para ", bestNeighbourCost)
    
    return solution, cost    

def randomDescent(dimension, distances, solution, iterMax):
    
    iter = 0
    cost = problem.calculateCost(solution, distances)

    while iter < iterMax: # Stop criteria
        iter = iter + 1

        # Movement - swap(i, j)
        i = random.randint(0, dimension - 1)
        j = i 
        # i != j
        while i == j:
            j = random.randint(0, dimension - 1)
    
        # Neighbour - s'
        swap(solution, i, j)

        # New cost
        # The best operation -> perform delta cost
        neighbourCost = problem.calculateCost(solution, distances)

        if neighbourCost < cost:
            # Move to the neighbour
            print("Melhora: de ", cost, " para ", neighbourCost)
            cost = neighbourCost
            iter = 0
        else:
            # The movement is undone
            swap(solution, i, j)

    return solution, cost

def swap(solution, i, j):
    tmp = solution[i]
    solution[i] = solution[j]
    solution[j] = tmp