'''
PEP300 - Metaheuristics Techniques for Combinatorial Optimization
https://github.com/fboliveira/PEP300-Metaheuristics-Combinatorial-Optimization

Prof. Fernando Bernardes de Oliveira, Ph.D.

TSP application
'''
import sys
import problem
import constructive
import util

def menuRefiningHeuristics(dimension, distances, solution):
    util.line()
    print("Heurísticas de refinamento:")
    util.line("-")

    print("1 - First improvement descent")
    print("2 - Best improvement descent")
    print("3 - Random improvement descent")
    print("0 - Voltar")


    choice = int(input("Opção: "))
    util.line()

    return solution


def menuMetaHeuristics():
    util.line()
    print("Meta-heurísticas:")
    util.line("-")

    print("1 - Multi-start")
    print("2 - GRASP")
    print("3 - Simulated Annealing")
    print("4 - Busca Tabu")
    print("5 - VNS")
    print("6 - Iterated Local Search")
    print("7 - Algoritmos genéticos")
    print("8 - Colônia de Formigas")
    print("9 - Scatter Search")
    print("0 - Voltar")

    choice = int(input("Opção: "))
    util.line()

def menuConstructiveMethods(dimension, distances, solution):

    util.line()
    print("Métodos construtivos:")
    util.line("-")

    print("1 - Construção aleatória")
    print("2 - Construção gulosa - vizinho mais próximo")
    print("3 - Construção parcialmente gulosa")
    print("0 - Voltar")

    choice = int(input("Opção: "))
    util.line()
    
    if choice == 0:
        return solution
    elif choice == 1:
        solution = constructive.createRandom(dimension)
    elif choice == 2:
        solution = constructive.nearestNeighbour(dimension, distances)
    elif choice == 3:
        alpha = float(input("Informe um valor para alpha [0; 1]: "))
        solution = constructive.semiGreedyNearNeighbour(dimension, distances, alpha)
    else:
        print("Metodo ainda não implementado.")

    print("Solução: ", solution)
    return solution


def menu(name, dimension, distances):

    solution = []
    cost = sys.maxsize

    while True:

        util.line()
        print("Defina a operação: ")
        util.line()

        print("1 - Construir solução")
        print("2 - Refinar solução")
        print("3 - Aplicar meta-heurística")
        print("4 - Calcular custo")
        print("0 - Sair")

        util.line("-")
        choice = int(input("Opção: "))
        util.line()
        
        if choice == 0:
            print("The end.")
            sys.exit(0)
        elif choice == 1:
            solution = menuConstructiveMethods(dimension, distances, solution)
        elif choice == 2:
            solution = menuRefiningHeuristics(dimension, distances, solution)
        elif choice == 3:
            menuMetaHeuristics()
        elif choice == 4:
            print("Solução: ", solution)
            cost = problem.calculateCost(solution, distances)
            util.line("-")
            print("Custo: ", cost)
        else:
            print("Metodo ainda não implementado.")

def main():
    util.line()
    print("PEP300 - Metaheuristics Techniques for Combinatorial Optimization")
    print("TSPLib")
    util.line("-")

    sourceFile = ''
    resultFile = ''

    try:
        sourceFile = sys.argv[1]
    except:
        print("Usage: tsp.py <sourceFile>")
        sys.exit(2)

    name, dimension, distances = problem.readTSPLibFiles(sourceFile)

    # print("Distances", distances)

    # pcb442 -> cost: 221440 -> 1:n
    # testSolution = [*range(1, dimension + 1)]
    # print(testSolution)
    # cost = problem.calculateCost(testSolution, distances)
    # print(cost)

    menu(name, dimension, distances)

if __name__ == "__main__":
    main()
