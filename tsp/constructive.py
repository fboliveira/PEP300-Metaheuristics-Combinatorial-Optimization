import sys
import random
import numpy as np
import copy

def createRandom(dimension):

    # print("Construção aleatória - dimensão: ", dimension)
    solution = [*range(1, dimension + 1)] # [inicial, final[
    random.shuffle(solution)

    return solution

def nearestNeighbour(dimension, distances):

    solution = []
    # An array to control inserted customers
    control = np.zeros(dimension, dtype=int)    

    # the first customer is randomly selected
    solution.append(random.randint(1, dimension))

    # Update control
    control[ solution[0] - 1 ] = 1

    for i in range(dimension - 1):
        closestCustomer = -1
        closestDistance = sys.maxsize # Inf

        # Current customer
        current = solution[i] - 1
        # Get the closest distance from current customer
        for j in range(dimension):
            # If the current customer and the candidate are different
            # AND the candidate is avalable    
            if i != j and control[j] == 0:                
                # Distance from current customer to candidate
                dist = distances[current, j]

                if dist < closestDistance:
                    closestCustomer = j
                    closestDistance = dist

        # Add closest customer to solution
        solution.append(closestCustomer + 1)
        # Update control
        control[ closestCustomer ] = 1

    # print(control)

    return solution

def semiGreedyNearNeighbour(dimension, distances, alpha):
    return createSolutionScarryVersion(dimension, distances, alpha)

def createSolutionScarryVersion(dimension, distances, alpha):

    solution = []

    # the first customer is randomly selected
    solution.append(random.randint(1, dimension))

    for i in range(dimension - 1):
        # print(solution)
        # List of distances from solution[i]:
        dimsol = copy.deepcopy(distances[solution[i] - 1, :])
        # Remove customers from solution -> set distances to max
        used = np.asarray(solution)
        dimsol[ used - 1 ] = sys.maxsize #~Inf
        # print(dimsol)
        # Set RCL size
        # rclSize = min + alpha(max - min)
        min = 1
        max = dimension - 1 - i
        rclSize = int(round(min + alpha * ( max - min )))
        # print("RCL", rclSize)
        id = random.randint(0, rclSize - 1)
        nearest = np.argsort( dimsol )[id] + 1
        # print(nearest)
        solution.append(nearest)

    return solution

def semiGreedyNearNeighbourDistance(dimension, distances, alpha):

    solution = []

    # An array to define the candidate customers
    candidate = [*range(1, dimension + 1)]

    # the first customer is randomly selected
    solution.append(random.randint(1, dimension))

    # Update candidates
    candidate.remove(solution[0])

    while(len(candidate) > 0):
        # Define gmin and gmax
        # Replace the code by min() and max() for lists or numpy.minimum(): https://numpy.org/doc/stable/reference/generated/numpy.minimum.html for a numpy array.
        gmin = sys.maxsize # Inf
        gmax = -sys.maxsize # -Inf

        # Last city (index)
        i = solution[len(solution) - 1] - 1

        # For each candidate t
        for t in candidate:
            # g(t) = dti, in which i is the last city.
            if i != (t - 1):
                if distances[i][t - 1] < gmin:
                    gmin = distances[i][t - 1]
                
                if distances[i][t - 1] > gmax:
                    gmax = distances[i][t - 1]

        gtValue = gmin + alpha * ( gmax - gmin )

        lrc = []
        # For each candidate t
        for t in candidate:
            if i != (t - 1) and distances[i][t - 1] <= gtValue:
                lrc.append(t)

        # print(lrc)
        # Select the candidate randomly - index
        choice = random.randint(0, len(lrc) - 1)
        # print(choice)

        # Insert the candidate into solution
        solution.append(lrc[choice])

        # Update the candidate list
        candidate.remove(lrc[choice])

    return solution

def test():

    dimension = 5
    distances = np.random.randint(low=10,high=30, size=(dimension,dimension))
    print(distances)
    solution = semiGreedyNearNeighbourDistance(dimension, distances,0.3)
    print(solution)