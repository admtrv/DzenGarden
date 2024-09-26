# crossover.py

import random

# Functions to crossover genes

def single_point_crossover(population):
    new_population = []

    if len(population) % 2 != 0:
        last_individual = population.pop()
        new_population.append(last_individual)

    for i in range(0, len(population) - 1, 2):

        parent1 = population[i]
        parent2 = population[i+1]

        # Select gene separation point
        position_point = random.randint(0, len(parent1[0]) - 1) # Positions
        turns_point = random.randint(0, len(parent1[1]) - 1) # Turns

        child1 = (parent1[0][:position_point] + parent2[0][position_point:], parent1[1][:turns_point] + parent2[1][turns_point:], 0)
        child2 = (parent2[0][:position_point] + parent1[0][position_point:], parent2[1][:turns_point] + parent1[1][turns_point:], 0)

        new_population.append(child1)
        new_population.append(child2)

    return new_population

def two_point_crossover(population):
    new_population = []

    if len(population) % 2 != 0:
        last_individual = population.pop()
        new_population.append(last_individual)

    for i in range(0, len(population) - 1, 2):

        parent1 = population[i]
        parent2 = population[i+1]

        # Select two gene separation points
        pos_point1, pos_point2 = sorted([random.randint(0, len(parent1[0]) - 1), random.randint(0, len(parent1[0]) - 1)]) # Positions
        turns_point1, turns_point2 = sorted([random.randint(0, len(parent1[1]) - 1), random.randint(0, len(parent1[1]) - 1)]) # Turns

        # Children
        child1_positions = parent1[0][:pos_point1] + parent2[0][pos_point1:pos_point2] + parent1[0][pos_point2:] # Child 1
        child1_turns = parent1[1][:turns_point1] + parent2[1][turns_point1:turns_point2] + parent1[1][turns_point2:]
        child1 = (child1_positions, child1_turns, 0)

        child2_positions = parent2[0][:pos_point1] + parent1[0][pos_point1:pos_point2] + parent2[0][pos_point2:] # Child 2
        child2_turns = parent2[1][:turns_point1] + parent1[1][turns_point1:turns_point2] + parent2[1][turns_point2:]
        child2 = (child2_positions, child2_turns, 0)

        new_population.append(child1)
        new_population.append(child2)

    return new_population

def uniform_crossover(population):
    new_population = []

    if len(population) % 2 != 0:
        last_individual = population.pop()
        new_population.append(last_individual)

    for i in range(0, len(population) - 1, 2):

        parent1 = population[i]
        parent2 = population[i + 1]

        # Empty children
        child1_positions = []
        child1_turns = []
        child2_positions = []
        child2_turns = []

        # Positions
        for j in range(len(parent1[0])):
            if random.choice([True, False]):
                child1_positions.append(parent1[0][j])
                child2_positions.append(parent2[0][j])
            else:
                child1_positions.append(parent2[0][j])
                child2_positions.append(parent1[0][j])

        # Turns
        for j in range(len(parent1[1])):
            if random.choice([True, False]):
                child1_turns.append(parent1[1][j])
                child2_turns.append(parent2[1][j])
            else:
                child1_turns.append(parent2[1][j])
                child2_turns.append(parent1[1][j])

        # Children
        child1 = (child1_positions, child1_turns, 0)
        child2 = (child2_positions, child2_turns, 0)

        new_population.append(child1)
        new_population.append(child2)

    return new_population
