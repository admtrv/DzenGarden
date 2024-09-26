# generation.py

import random
import config

# Garden properties
length = config.length
height = config.height
rocks = config.rocks

# Function to generate start coordinates
def generate_coordinates():
    if random.randint(0, 1) == 0:
        # Horizontal start
        y = random.randint(0, height - 1)
        x = random.randint(0, 1) * (length - 1)
    else:
        # Vertical start
        y = random.randint(0, 1) * (height - 1)
        x = random.randint(0, length - 1)
    start = (y, x)

    if start in [(0, 0), (height - 1, 0), (0, length - 1), (height - 1, length - 1)]:
        return generate_coordinates()

    if start in rocks:
        return generate_coordinates()

    return start

# Function to generate genes for one individual
def generate_genes():
    positions = []
    turns = []

    while len(positions) < length + height:
        coordinates = generate_coordinates()
        if coordinates not in positions:
            positions.append(coordinates)

    while len(turns) < len(rocks):
        if random.choice([True, False]):
            turns.append("r")
        else:
            turns.append("l")

    return (positions, turns, 0)

# Function to initialize population
def generate_population(size):
    population=[]

    for i in range(size):
        population.append(generate_genes())

    return population
