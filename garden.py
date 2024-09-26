# garden.py

import config

# Garden properties
length = config.length
height = config.height
rocks = config.rocks

# Function to create garden and set rocks
def create_garden():
    garden = []

    for i in range(height):
        row = []
        for j in range(length):
            row.append(0)
        garden.append(row)

    for (y, x) in rocks:
        garden[y][x] = -1

    return garden

# Function to print garden
def print_garden(garden):
    for row in garden:
        print(' '.join(f'{cell:3}' for cell in row))
    print()
