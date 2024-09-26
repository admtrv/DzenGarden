# mutation.py

import random
import config
from generation import generate_coordinates

# Generation parameters
mutation_rate = config.mutation_rate

def mutation(population):
    new_population = []

    for individual in population:
        new_individual = (individual[0][:],individual[1][:],individual[2])

        # Start position mutation
        for i in range(len(new_individual[0])):
            if random.random() < mutation_rate:
                pos = generate_coordinates()
                new_individual[0][i] = pos

        # Turns mutation
        for i in range(len(new_individual[1])):
            if random.random() < mutation_rate:
                if random.choice([True, False]):
                    new_individual[1][i] = "r"
                else:
                    new_individual[1][i] = "l"

        new_population.append(new_individual)

    return new_population
