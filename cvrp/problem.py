# CVRPLib: http://vrp.galgos.inf.puc-rio.br/index.php/en/

import math
import numpy as np

def readCVRPLibFiles(sourceFile):
    print("Reading file....")
    print("Source.........: ", sourceFile)

    data = open(sourceFile)

    name = ''
    dimension = 0
    capacity = 0
    depot = 1

    coordSection = False
    demandSection = False

    for i, line in enumerate(data):
        ln = line.split()

        # print(ln)

        # NAME:
        if i == 0:
            name = ln[ len(ln) - 1 ]
        # DIMENSION:        
        elif i == 3:
            dimension = int(ln[ len(ln) - 1 ])
            points = np.zeros(shape=(dimension, 3))
            demand = np.zeros(dimension)
        # CAPACITY
        elif i == 5:
            capacity = int(ln[ len(ln) - 1 ])
        elif i == 6:
            coordSection = True
        elif i > 6:

            if coordSection:    
                if ln[0] == "DEMAND_SECTION":
                    coordSection = False
                    demandSection = True
                    continue

                id = int(ln[0])
                x = float(ln[1])
                y = float(ln[2])

                points[id - 1][0] = id
                points[id - 1][1] = x
                points[id - 1][2] = y

            if demandSection:

                if ln[0] == "DEPOT_SECTION":
                    break

                id = int(ln[0])
                x = float(ln[1])

                # print(id, x)            

                demand[id - 1] = x

    print("Name.......: ", name)
    print("Dimension..: ", dimension)
    print("Capacity...: ", capacity)
    # print("Points.....: ", points)
    # print("Demands....: ", demand)

    distances = calculateDistances(dimension, points)

    # print("Distances", distances)
    data.close()

    return name, dimension, distances, capacity, demand, depot


def calculateDistances(dimension, points):
    distances = np.zeros(shape=(dimension, dimension))

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

    for i in range(len(solution)):
        for j in range(len(solution[i]) - 1):
            # 0 -> n - 1
            cost += distance[solution[i][j] - 1][solution[i][j + 1] - 1]

    return cost

def gap(cost, bestValue):

    return (( cost - bestValue ) / bestValue) * 100.0
