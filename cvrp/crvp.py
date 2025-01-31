'''
PEP300 - Metaheuristics Techniques for Combinatorial Optimization
https://github.com/fboliveira/PEP300-Metaheuristics-Combinatorial-Optimization

Prof. Fernando Bernardes de Oliveira, Ph.D.

CVRP - Capacitated Vehicle Routing Problem Library.

'''
import sys
import problem

def main():
    print("="*80)
    print("PEP300 - Metaheuristics Techniques for Combinatorial Optimization")
    print("CVRP")
    print("-"*80)

    sourceFile = ''

    try:
        sourceFile = sys.argv[1]
    except:
        print("Usage: cvrp.py <dataFile>")
        sys.exit(2)

    name, dimension, distances, capacity, demand, depot = problem.readCVRPLibFiles(sourceFile)

    print("-"*80)

    # Call your method here!    

if __name__ == "__main__":
    main()