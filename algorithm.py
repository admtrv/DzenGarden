import random
import config
from generation import generate_population
from fitness import evaluation, fitness_function
from elitism import elitism
from selection import tournament_selection, rank_based_selection, roulette_wheel_selection
from crossover import single_point_crossover, two_point_crossover, uniform_crossover
from mutation import mutation
from garden import print_garden

# Generation parameters
population_size = config.population_size
generations_size = config.generations_size
mutation_rate = config.mutation_rate
elitism_rate = config.elitism_rate
future_generation = config.future_generation
selection_type = config.selection_type
crossover_type = config.crossover_type

# Garden properties
length = config.length
height = config.height
rocks = config.rocks

def main(need_print=True):

    fitnesses = []
    best_fitness = -float('inf')
    best_individual = None

    # Generate initial population
    population = generate_population(population_size)
    population_number = 1

    while True:

        # Evaluate fitness of current population
        evaluated_population = evaluation(population)

        max_fitness = -float('inf')
        max_individual = None
        for individual in evaluated_population:
            if individual[2] > max_fitness:
                max_fitness = individual[2]
                max_individual = individual
        fitnesses.append(max_fitness)

        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_individual = max_individual

        # Conditions to stop algorithm
        if population_number == generations_size: # Maximum number of generations reached
            break

        if best_fitness >= length * height - len(rocks): # Optimal solution with perfect fitness found
            break

        # Apply elitism
        next_population = elitism(evaluated_population)

        # Apply selection
        if selection_type == "tournament_selection":
            selected_population = tournament_selection(evaluated_population, int(population_size * future_generation))
        elif selection_type == "rank_based_selection":
            selected_population = rank_based_selection(evaluated_population, int(population_size * future_generation))
        elif selection_type == "roulette_wheel_selection":
            selected_population = roulette_wheel_selection(evaluated_population, int(population_size * future_generation))
        else:
            selected_population = tournament_selection(evaluated_population, int(population_size * future_generation)) # Default

        # Apply crossover
        if crossover_type == "single_point_crossover":
            crossed_population = single_point_crossover(selected_population)
        elif crossover_type == "two_point_crossover":
            crossed_population = two_point_crossover(selected_population)
        elif crossover_type == "uniform_crossover":
            crossed_population = uniform_crossover(selected_population)
        else:
            crossed_population = single_point_crossover(selected_population) # Default

        # Apply mutation
        mutated_population = mutation(crossed_population)
        next_population += mutated_population

        # Generate remaining part
        next_population += generate_population(population_size - len(next_population))

        # Update current generation
        population = next_population
        population_number += 1

    if need_print:
        best_garden = fitness_function(best_individual, return_garden=True)

        print(f"Best result: generations = {population_number}  fitness = {best_fitness}")
        print("Best garden:")
        print_garden(best_garden)

    return max(fitnesses)

if __name__ == '__main__':
    main()
