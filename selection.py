# selection.py

import random
import config

# Functions to find best individuals

def tournament_selection(population, amount):
    new_population = []

    tournament_size = 3

    while len(new_population) < amount:
        selected = []

        for i in range(tournament_size):
            random_index = random.randint(0, len(population) - 1)
            selected.append(population[random_index])

        best_individual = selected[0]
        for individual in selected:
            if individual[2] > best_individual[2]:
                best_individual = individual

        best_individual_copy = (best_individual[0][:], best_individual[1][:], best_individual[2])
        new_population.append(best_individual_copy)

    return new_population

def rank_based_selection(population, amount):

    population_copy = []
    for individual in population:
        population_copy.append((individual[0][:], individual[1][:], individual[2]))

    for i in range(len(population_copy) - 1):
        for j in range(i + 1, len(population_copy)):
            if population_copy[i][2] < population_copy[j][2]:
                population_copy[i], population_copy[j] = population_copy[j], population_copy[i]

    new_population = []

    for i in range(amount):
        individual = population_copy[i]
        individual_copy = (individual[0][:], individual[1][:], individual[2])
        new_population.append(individual_copy)

    return new_population

def roulette_wheel_selection(population, amount):

    total_fitness = 0
    for individual in population:
        total_fitness += individual[2]

    new_population = []

    while len(new_population) < amount:
        roulette = random.uniform(0, total_fitness)

        cumulative_fitness = 0

        for individual in population:
            cumulative_fitness += individual[2]
            if cumulative_fitness >= roulette:
                individual_copy = (individual[0][:], individual[1][:], individual[2])
                new_population.append(individual_copy)
                break

    return new_population
