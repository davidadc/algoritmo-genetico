from numpy import random, ones


f = open('input-population.txt', 'w')

for i in range(0, 100):
    p = random.dirichlet(ones(11), size=1)
    p_list = p[0].tolist()

    f.write(','.join(map(str, p_list)))
    f.write('\n')

f.close()
