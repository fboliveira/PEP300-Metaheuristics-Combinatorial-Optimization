import copy 
import constructive
import refining
import sys

def multiStart(dimension, distances, iterMax):
    
    iter = 0
    i = 0

    bestSolution = []
    bestCost = sys.maxsize # Inf

    while iter < iterMax:
        iter = iter + 1

        solution = createSolution(dimension, distances)
        solution, cost = localSearch(dimension, distances, solution)

        # f(s) < f(s*)
        if cost < bestCost:
            # print("Melhora: de ", bestCost, " para ", cost)
            bestSolution = copy.deepcopy(solution) # s* <- s
            bestCost = cost # f* <- f(s)
            iter = 0

        i = i + 1
        print("Iteração: ", i, ": ", bestCost)

    # return s* and f(s*)
    return bestSolution, bestCost

def createSolution(dimension, distances):
    # Choose one method to create the solution
    return constructive.createRandom(dimension)


def localSearch(dimension, distances, solution):
    # Choose one method to refine the solution
    return refining.firstImprovementDescent(dimension, distances, solution)