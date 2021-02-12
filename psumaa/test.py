import problem
import sys
sys.path.insert(1, '../tsp')
import constructive

sourceFile = './instances/instpaper.dat'
solutionFile = ''

numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

solution = [3, 4, 1, 2]

cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)

print("Cost......: ", cost)

sourceFile = './instances/dados/INST0801.dat'
solutionFile = './instances/saida/inst0801.sol'

numJobs, dataJobs, dataSetup, bestValue = problem.readFiles(sourceFile, solutionFile)

solution = constructive.createRandom(numJobs)

print(solution)

cost = problem.calculateCost(solution, numJobs, dataJobs, dataSetup)

gap = problem.gap(cost, bestValue)

print("Cost......: ", cost)
print("GAP.......: ", '%.2f'%gap)

