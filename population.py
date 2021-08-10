from random import sample

# Fitness
from fitness import Fitness

# Utils
from utils.utils import decision
from utils.files import delete_linebreak


class Population:
    def __init__(self):
        self.fitness = Fitness()

        self.main_population = self.load_population()
        self.population_fitness = self.calculate_fitness()
        self.population_length = len(self.main_population)

        # Percentages
        self.cross_probability = 0.80
        self.mutation_probability = 0.01

    def load_population(self):
        file = open('input-population.txt')
        lines = file.readlines()
        file.close()

        p = list(map(delete_linebreak, lines))

        return p

    def calculate_fitness(self):
        calc = []
        for chromosome in self.main_population:
            f = self.fitness.calculate_fitness(chromosome=chromosome)
            calc.append(f)

        return calc

    def genetic_algorithm(self):
        best_chromosomes, indexes = self.selection()

        if decision(self.cross_probability):
            self.cross(best_chromosomes, indexes)

        if decision(self.mutation_probability):
            self.mutation()

        print(best_chromosomes)
        print(indexes)

    def selection(self):
        # TODO: change to 0.15 for real tests with 220 input-population
        percentage = 0.20
        qty = int(self.population_length * percentage)

        tournament = []
        selected_population = []
        remaining_population = [*self.population_fitness]

        # TODO: change range to 6 for real tests
        for _ in range(4):
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

    def cross(self, chromosomes, indexes):
        pass

    def mutation(self):
        pass

    def substitution(self, new_chromosome, index):
        self.population[index] = new_chromosome
