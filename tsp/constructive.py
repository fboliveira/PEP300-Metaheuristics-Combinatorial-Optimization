import sys
import random
import numpy as np
import copy

def createRandom(dimension):

    print("Construção aleatória - dimensão: ", dimension)
    solution = [*range(1, dimension + 1)] # [inicial, final[
    random.shuffle(solution)

    return solution

def nearestNeighborhood(dimension, distances):
    return createSolution(dimension, distances, 0.0)

def semiGreedyNearNeighborhood(dimension, distances, alpha):
    return createSolution(dimension, distances, alpha)

def createSolution(dimension, distances, alpha):

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

def test():

    dimension = 5
    distances = np.random.randint(low=10,high=30, size=(dimension,dimension))
    print(distances)
    solution = nearestNeighborhood(dimension, distances)
    print(solution)