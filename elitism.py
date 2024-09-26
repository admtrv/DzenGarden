# elitism.py

import config

# Generation parameters
elitism_rate = config.elitism_rate


def elitism(population):

    elite_count = int(len(population) * elitism_rate)

    population_copy = []
    for individual in population:
        population_copy.append((individual[0][:], individual[1][:], individual[2]))

    for i in range(len(population_copy) - 1):
        for j in range(i + 1, len(population_copy)):
            if population_copy[i][2] < population_copy[j][2]:
                population_copy[i], population_copy[j] = population_copy[j], population_copy[i]

    elite_population = []
    for i in range(elite_count):
        elite_individual = (population_copy[i][0][:], population_copy[i][1][:], population_copy[i][2])
        elite_population.append(elite_individual)

    return elite_population
