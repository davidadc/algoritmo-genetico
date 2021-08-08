class Population:
    def __init__(self):
        self.population = self.load_population()

    def load_population(self):
        file = open('input-population.txt')
        p = file.readlines()
        file.close()

        return p

    def replace_chromosome(self, new_chromosome, index):
        self.population[index] = new_chromosome
