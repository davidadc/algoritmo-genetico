def min_risk():
    f = open('covar.txt', 'r')
    lines = f.readlines()
    f.close()

    covar = []
    for raw_line in lines:
        split_line = raw_line.strip().split(',')
        nums_ls = [float(x) for x in split_line]
        covar.append(nums_ls)

    f = open('input-population.txt')
    population = f.readlines()
    f.close()

    riskP = []
    for chromosome in population:
        summation = 0
        gens = chromosome.split(',')

        for index_i, gen_i in enumerate(gens):
            for index_j, gen_j in enumerate(gens):
                summation += (float(gen_i) * float(gen_j) * covar[index_i][index_j])

        riskP.append(summation)

    return riskP


def calculate_max_performance():
    f = open('performance.txt', 'r')
    lines = f.readlines()
    f.close()

    def delete_linebreak(s):
        return float(s[:len(s) - 1])

    performances = list(map(delete_linebreak, lines))

    f = open('input-population.txt')
    population = f.readlines()
    f.close()

    max_performance = []
    for chromosome in population:
        summation = 0

        for index, gen in enumerate(chromosome.split(',')):
            summation += (float(gen) * performances[int(index)])

        max_performance.append(summation)

    return max_performance


def fitness():
    pass

