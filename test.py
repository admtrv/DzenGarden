# test.py

import config
from algorithm import main as run

# Log file properties
LOG_FILE = 'temp/log.txt'
log_file = None

# Tests properties
num_runs = 100

# Function to log message in console and in file
def log_message(message):
    print(message) # Print in console
    if log_file:
        log_file.write(message + '\n')  # Print in file

# Function to change config
def update_config(new_config):
    config.population_size = new_config['population_size']
    config.generations_size = new_config['generations_size']
    config.mutation_rate = new_config['mutation_rate']
    config.elitism_rate = new_config['elitism_rate']
    config.future_generation = new_config['future_generation']
    config.selection_type = new_config['selection_type']
    config.crossover_type = new_config['crossover_type']
    # Length, height and rocks as in config.py

# Function to test one config
def test_config(conf, runs=100):
    update_config(conf)
    max_fitness = config.length * config.height - len(config.rocks)  # Max possible fitness
    successful_runs = 0

    for i in range(runs):
        fitnesses, fitness = run(need_print=False)
        print(f"Run {i+1}/{runs}: fitness = {fitness}")
        if fitness == max_fitness:
            successful_runs += 1

    success_rate = (successful_runs / runs) * 100
    return success_rate

# Function to test all configs
def test_all(configs, runs=100):
    results = []
    best_config = None
    best_success_rate = -1

    for i, conf in enumerate(configs, start=1):
        log_message(f"Testing config {i}/{len(configs)}: config = {conf}")

        success_rate = test_config(conf, runs=runs)
        results.append((conf, success_rate))

        log_message(f"Config {i} success rate: {success_rate}%\n")

        if success_rate > best_success_rate:
            best_success_rate = success_rate
            best_config = conf

    log_message(f"Best result: config = {best_config} success rate = {best_success_rate}%")
    return best_config

# Function to generate different configs
def generate_config():
    configs = []
    for population_size in [100, 200]:
        for generations_size in [100, 200]:
            for mutation_rate in [0.0, 0.01, 0.05]:
                for elitism_rate in [0.0, 0.1, 0.2]:
                    for future_generation in [0.6, 0.7, 0.8]:
                        for selection_type in ["tournament_selection"]:
                            for crossover_type in ["single_point_crossover"]:
                                config_dict = {
                                    "population_size": population_size,
                                    "generations_size": generations_size,
                                    "mutation_rate": mutation_rate,
                                    "elitism_rate": elitism_rate,
                                    "future_generation": future_generation,
                                    "selection_type": selection_type,
                                    "crossover_type": crossover_type,
                                }
                                configs.append(config_dict)
    return configs

if __name__ == "__main__":
    log_file = open(LOG_FILE, 'w')

    # Generating configs
    configs = generate_config()

    # Testing configs
    best_config = test_all(configs, runs=num_runs)

    log_file.close()
