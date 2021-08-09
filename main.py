from fitness import Fitness
from population import Population


if __name__ == '__main__':
    population = Population()
    fitness = Fitness()

    print(population.selection())
