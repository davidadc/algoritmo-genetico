from numpy import random, ones


def generate_random_population(length):
    f = open('input-population.txt', 'w')

    for i in range(0, length):
        p = random.dirichlet(ones(11), size=1)
        p_list = p[0].tolist()

        f.write(','.join(map(str, p_list)))

        if i != length - 1:
            f.write('\n')

    f.close()
