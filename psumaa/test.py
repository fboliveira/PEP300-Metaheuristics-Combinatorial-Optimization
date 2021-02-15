import problem
import sys
import random

sourceFile = './instances/instpaper.dat'
solutionFile = ''

numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

solution = [3, 4, 1, 2]

cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)

print("Cost......: ", cost)

sourceFile = './instances/dados/INST0801.dat'
solutionFile = './instances/saida/inst0801.sol'

numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

# Generate a random solution
solution = [*range(1, numJobs + 1)] # [inicial, final[
random.shuffle(solution)

print(solution)

cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)

gap = problem.gap(cost, bestValue)

print("Best value......: ", bestValue)
print("Solution Cost...: ", cost)
print("GAP.............: ", '%.2f'%gap)