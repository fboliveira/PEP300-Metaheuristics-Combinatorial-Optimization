import math
import numpy

def readTSPLibFiles(sourceFile):
    print("Reading files...")
    print("Source: ", sourceFile)

    data = open(sourceFile)

    name = ''
    dimension = 0

    for i, line in enumerate(data):
        ln = line.split()

        # print(ln)

        # NAME:
        if i == 0:
            name = ln[1]
        # DIMENSION:        
        elif i == 3:
            dimension = int(ln[ len(ln) - 1 ])
            points = numpy.zeros(shape=(dimension, 3))
        elif i > 5:

            if ln[0] == "EOF":
                break

            id = int(ln[0])
            x = float(ln[1])
            y = float(ln[2])            

            points[id - 1][0] = id
            points[id - 1][1] = x
            points[id - 1][2] = y


    print("Name: ", name)
    print("Dimension: ", dimension)
    # print("Points", points)

    distances = calculateDistances(dimension, points)

    # print("Distances", distances)


    return name, dimension, distances


def calculateDistances(dimension, points):
    distances = numpy.zeros(shape=(dimension, dimension))

    for i in range(dimension):
        for j in range(dimension):
            dij = euclideanDistance(points[i][1], points[i][2], points[j][1], points[j][2])
            distances[i][j] = dij

    return distances

def euclideanDistance(px, py, qx, qy):
    xd = pow(px - qx, 2);
    yd = pow(py - qy, 2);

    dij = int(round( math.sqrt( xd + yd) ))

    return dij


def calculateCost(solution, distance):

    # print("Solução: ", solution)

    cost = 0

    for i in range(len(solution) - 1):
        # 0 -> n - 1
        cost += distance[solution[i] - 1][solution[i + 1] - 1]

    # Last to first - close TSP cycle
    cost += distance[solution[ len(solution) - 1 ] - 1][solution[0] - 1]

    return cost