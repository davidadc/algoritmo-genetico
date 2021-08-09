from random import sample

# Fitness
from fitness import Fitness

# Utils
from utils.files import delete_linebreak


class Population:
    def __init__(self):
        self.fitness = Fitness()
        self.main_population = self.load_population()
        self.population_length = len(self.main_population)
        self.population = self.calculate_population_and_fitness()

    def load_population(self):
        file = open('input-population.txt')
        lines = file.readlines()
        file.close()

        p = list(map(delete_linebreak, lines))

        return p

    def calculate_population_and_fitness(self):
        calc = []
        for chromosome in self.main_population:
            f = self.fitness.calculate_fitness(chromosome=chromosome)
            calc.append((chromosome, f))

        return calc

    def selection(self):
        # TODO: change to 0.15 for real tests with 220 input-population
        percentage = 0.20
        qty = int(self.population_length * percentage)

        print(qty)

        tournament = []
        selected_population = []
        remaining_population = [*self.population]

        # TODO: change range to 6 for real tests
        for _ in range(4):
            sample_pop = sample(remaining_population, qty)
            selected_population = [*selected_population, *sample_pop]
            tournament.append(sample_pop)

            remaining_population = list(set(remaining_population) - set(selected_population))

            print(sample_pop)

        print(remaining_population)

        def get_fitness(t):
            return t[1]

        best_chromosomes = []
        for x in tournament:
            only_fitness = list(map(get_fitness, x))
            best_chromosomes.append(max(only_fitness))

        return best_chromosomes

    def cross(self):
        pass

    def mutation(self):
        pass

    def substitution(self, new_chromosome, index):
        self.population[index] = new_chromosome
