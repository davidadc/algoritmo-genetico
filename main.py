from population import Population


if __name__ == '__main__':
    population = Population()

    for _ in range(30):
        population.genetic_algorithm()

    f = open('output-population.txt', 'w')

    for i in range(0, population.population_length):
        f.write(population.main_population[i])

        if i != population.population_length - 1:
            f.write('\n')

    f.close()

    f = open('output-fitness.txt', 'w')

    for i in range(0, population.population_length):
        f.write(str(population.population_fitness[i]))

        if i != population.population_length - 1:
            f.write('\n')

    f.close()
