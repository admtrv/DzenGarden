# graph.py

import matplotlib.pyplot as plt
import config
from algorithm import main as run

# Tests properties
parameter_name = 'crossover_type'
parameter_values = ["single_point_crossover", "two_point_crossover", "uniform_crossover"]

# Function to change config
def update_config(new_config):
    config.population_size = new_config.get('population_size', config.population_size)
    config.generations_size = new_config.get('generations_size', config.generations_size)
    config.mutation_rate = new_config.get('mutation_rate', config.mutation_rate)
    config.elitism_rate = new_config.get('elitism_rate', config.elitism_rate)
    config.future_generation = new_config.get('future_generation', config.future_generation)
    config.selection_type = new_config.get('selection_type', config.selection_type)
    config.crossover_type = new_config.get('crossover_type', config.crossover_type)
    # Length, height and rocks as in config.py

# Function to collect data
def test(parameter_name, parameter_values):
    all_fitnesses = []

    for value in parameter_values:
        new_config = {parameter_name: value}
        update_config(new_config)

        fitnesses, fitness = run(need_print=False)
        all_fitnesses.append((value, fitnesses))

    return all_fitnesses

# Function to make graph
def plot_fitnesses(all_fitnesses, parameter_name):
    plt.figure()

    for value, fitnesses in all_fitnesses:
        generations = range(1, len(fitnesses) + 1)
        plt.plot(generations, fitnesses, label=f"{parameter_name} = {value}")

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title(f'Fitness evolution depends on {parameter_name}')
    plt.legend()
    plt.grid(True)

    filename = f'fitness_evolution_{parameter_name}.png'
    plt.savefig(filename)

    plt.show()

if __name__ == "__main__":

    all_fitnesses = test(parameter_name, parameter_values)

    plot_fitnesses(all_fitnesses, parameter_name)
