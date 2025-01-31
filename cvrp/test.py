import problem
import constructive

sourceFile = './instances/A-n10-k2-test.vrp'

name, dimension, distances, capacity, demand, depot = problem.readCVRPLibFiles(sourceFile)
solution = constructive.createRandom(dimension, capacity, demand)
print("Solution..:", solution)

cost = problem.calculateCost(solution, distances)
print("Cost......: ", cost)

print("-"*80)

sourceFile = './instances/A-n32-k5.vrp'

name, dimension, distances, capacity, demand, depot = problem.readCVRPLibFiles(sourceFile)
solution = constructive.createRandom(dimension, capacity, demand)
print("Solution..:", solution)

cost = problem.calculateCost(solution, distances)
print("Cost......: ", cost)

print("-"*80)