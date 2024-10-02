# config.py

# Generation parameters
population_size = 100
generations_size = 100
mutation_rate = 0.01
elitism_rate = 0.1
future_generation = 0.6
selection_type = "tournament_selection" # tournament_selection, rank_based_selection, roulette_wheel_selection
crossover_type = "single_point_crossover" # single_point_crossover, two_point_crossover, uniform_crossover

# Garden properties
length = 12
height = 10
rocks = [(2, 1), (4, 2), (3, 4), (1, 5), (6, 8), (6, 9)]
