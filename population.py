from random import randint, random, sample

# Fitness
from fitness import Fitness

# Utils
from utils.utils import decision
from utils.files import delete_linebreak


class Population:
    def __init__(self):
        self.fitness = Fitness()

        self.main_population = self.load_population()
        self.population_fitness = self.calculate_fitness(population=self.main_population)
        self.population_length = len(self.main_population)

        # Percentages
        self.cross_probability = 0.80
        self.mutation_probability = 0.05

    def load_population(self):
        file = open('input-population.txt')
        lines = file.readlines()
        file.close()

        p = list(map(delete_linebreak, lines))

        return p

    def calculate_fitness(self, population):
        calc = []

        for chromosome in population:
            f = self.fitness.calculate_fitness(chromosome=chromosome)
            calc.append(f)

        return calc

    def normalize_chromosome(self, chromosome):
        sum_chromosome = sum(chromosome)
        normalized_chromosome = [float(gen / sum_chromosome) for gen in chromosome]

        return normalized_chromosome

    def genetic_algorithm(self):

        # First Step: Selection
        best_chromosomes, indexes = self.selection()

        # TODO: Activate
        # Second Step: Cross
        # if decision(self.cross_probability):
        best_chromosomes = self.cross(chromosomes=best_chromosomes)

        # Third Step: Mutation
        for index, crossed_chromosomes in enumerate(best_chromosomes):
            # TODO: Activate
            # if decision(self.mutation_probability):
            best_chromosomes[index] = self.mutation(crossed_chromosomes=crossed_chromosomes)

        # Fourth Step: Substitution
        for index, crossed_chromosomes in enumerate(best_chromosomes):
            self.substitution(
                crossed_chromosomes=crossed_chromosomes
            )

    def selection(self):
        # TODO: change to 0.15 for 220 input-population - 0.20 test for 10
        percentage = 0.15
        qty = int(self.population_length * percentage)

        tournament = []
        selected_population = []
        remaining_population = [*self.population_fitness]

        while len(remaining_population) > qty:
            sample_pop = sample(remaining_population, qty)
            selected_population = [*selected_population, *sample_pop]
            tournament.append(sample_pop)

            remaining_population = list(set(remaining_population) - set(selected_population))

        best_chromosomes = []
        indexes = []

        for x in tournament:
            best_fitness = max(x)
            best_fitness_position = self.population_fitness.index(best_fitness)
            indexes.append(best_fitness_position)
            best_chromosomes.append(self.main_population[best_fitness_position])

        return best_chromosomes, indexes

    def cross(self, chromosomes):
        remaining_chromosomes = [*chromosomes]

        crossed_chromosomes = []

        while len(remaining_chromosomes) > 0:
            sample_pop = sample(remaining_chromosomes, 2)
            remaining_chromosomes = list(set(remaining_chromosomes) - set(sample_pop))

            cross_position = randint(1, 9)

            split_a = sample_pop[0].split(',')
            split_b = sample_pop[1].split(',')

            splitted_a = split_a[0:cross_position]
            splitted_b = split_a[cross_position:]

            splitted_c = split_b[0:cross_position]
            splitted_d = split_b[cross_position:]

            crossed_chromosome_a = [*splitted_a, *splitted_d]
            crossed_chromosome_b = [*splitted_b, *splitted_c]

            crossed_chromosome_a = [float(gen) for gen in crossed_chromosome_a]
            crossed_chromosome_b = [float(gen) for gen in crossed_chromosome_b]

            crossed_chromosome_a = self.normalize_chromosome(chromosome=crossed_chromosome_a)
            crossed_chromosome_b = self.normalize_chromosome(chromosome=crossed_chromosome_b)

            crossed_chromosomes = [
                *crossed_chromosomes,
                [crossed_chromosome_a, crossed_chromosome_b]
            ]

        return crossed_chromosomes

    def mutation(self, crossed_chromosomes):
        for index, chromosome in enumerate(crossed_chromosomes):
            random_gen = randint(0, 10)
            new_gen = random()

            chromosome[random_gen] = new_gen

            crossed_chromosomes[index] = self.normalize_chromosome(chromosome=chromosome)

        return crossed_chromosomes

    def substitution(self, crossed_chromosomes):
        population = [','.join(list(map(str, chromosome))) for chromosome in crossed_chromosomes]

        calc_fitness = self.calculate_fitness(population=population)

        better_chromosome_index = calc_fitness.index(max(calc_fitness))
        worst_chromosome_in_population = self.population_fitness.index(min(self.population_fitness))

        self.main_population[worst_chromosome_in_population] = population[better_chromosome_index]
        self.population_fitness[worst_chromosome_in_population] = calc_fitness[better_chromosome_index]
