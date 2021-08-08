from fitness import Fitness
from population import Population


if __name__ == '__main__':
    population = Population()
    fitness = Fitness()

    a = []
    for chromosome in population.population:
        f = fitness.calculate_fitness(chromosome=chromosome)
        a.append(f)

    print(a)
