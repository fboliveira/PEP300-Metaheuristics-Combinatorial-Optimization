import random

def createRandom(dimension):

    print("Construção aleatória - dimensão: ", dimension)
    solution = [*range(1, dimension + 1)] # [inicial, final[
    random.shuffle(solution)

    return solution

def nearestNeighborhood(dimension, distances):
    pass