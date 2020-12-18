import copy 
import constructive
import refining
import sys

def grasp(dimension, distances, graspMax, alpha):
    
    bestSolution = []
    bestCost = sys.maxsize # Inf

    for iter in range(1, graspMax + 1):

        solution = createSolution(dimension, distances, alpha)
        solution, cost = localSearch(dimension, distances, solution)

        # f(s) < f(s*)
        if cost < bestCost:
            # print("Melhora: de ", bestCost, " para ", cost)
            bestSolution = copy.deepcopy(solution) # s* <- s
            bestCost = cost # f* <- f(s)

        print("Iteração: ", iter, ": ", bestCost)

    # return s* and f(s*)
    return bestSolution, bestCost

def createSolution(dimension, distances, alpha):
    # Choose one method to create the solution
    return constructive.semiGreedyNearNeighbourDistance(dimension, distances, alpha)

def localSearch(dimension, distances, solution):
    # Choose one method to refine the solution
    return refining.firstImprovementDescent(dimension, distances, solution)