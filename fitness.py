# fitness.py

import config
from garden import create_garden

# Garden properties
length = config.length
height = config.height


# Fitness function to evaluate individuals
def fitness_function(individual, return_garden=False):
    positions, turns, fitness = individual
    fitness = 0

    garden = create_garden()

    step = 1
    for pos in positions:
        current_pos = pos
        direction = None
        turn_index = 0
        turn_count = 0

        # Choose starting direction
        if current_pos[0] == 0:
            direction = "d"
        elif current_pos[0] == height - 1:
            direction = "u"
        elif current_pos[1] == 0:
            direction = "r"
        elif current_pos[1] == length - 1:
            direction = "l"


        # Skip if already visited
        if garden[current_pos[0]][current_pos[1]] != 0:
            continue
        else:
            garden[current_pos[0]][current_pos[1]] = step
            fitness += 1

        while True:
            # Check if reached side
            if ((current_pos[1] == 0 and direction == "l") or
                    (current_pos[1] == length - 1 and direction == "r") or
                    (current_pos[0] == 0 and direction == "u") or
                    (current_pos[0] == height - 1 and direction == "d")):
                step += 1
                break

            moved = False

            # If can move in chosen direction
            if direction == "r" and current_pos[1] + 1 < length and garden[current_pos[0]][current_pos[1] + 1] == 0:
                current_pos = (current_pos[0], current_pos[1] + 1)
                garden[current_pos[0]][current_pos[1]] = step
                fitness += 1
                moved = True

            elif direction == "l" and current_pos[1] - 1 >= 0 and garden[current_pos[0]][current_pos[1] - 1] == 0:
                current_pos = (current_pos[0], current_pos[1] - 1)
                garden[current_pos[0]][current_pos[1]] = step
                fitness += 1
                moved = True

            elif direction == "d" and current_pos[0] + 1 < height and garden[current_pos[0] + 1][current_pos[1]] == 0:
                current_pos = (current_pos[0] + 1, current_pos[1])
                garden[current_pos[0]][current_pos[1]] = step
                fitness += 1
                moved = True

            elif direction == "u" and current_pos[0] - 1 >= 0 and garden[current_pos[0] - 1][current_pos[1]] == 0:
                current_pos = (current_pos[0] - 1, current_pos[1])
                garden[current_pos[0]][current_pos[1]] = step
                fitness += 1
                moved = True

            if moved:
                turn_count = 0
                continue

            # If no possible move, handle direction change
            else:
                if turn_index >= len(turns):
                    turn_index = 0

                # Change direction based on the current turn
                if turns[turn_index] == "l":
                    if direction == "r":
                        direction = "u"
                    elif direction == "u":
                        direction = "l"
                    elif direction == "l":
                        direction = "d"
                    elif direction == "d":
                        direction = "r"
                elif turns[turn_index] == "r":
                    if direction == "r":
                        direction = "d"
                    elif direction == "d":
                        direction = "l"
                    elif direction == "l":
                        direction = "u"
                    elif direction == "u":
                        direction = "r"

                turn_count += 1
                turn_index += 1

                # Stop after 360-degree turns
                if turn_count == 4:
                    step += 1
                    break

    evaluated_individual = (positions, turns, fitness)

    if return_garden:
        return garden
    return evaluated_individual


# Function to generate new evaluated population
def evaluation(population):
    evaluated_population = []

    for individual in population:
        new_individual = (individual[0][:], individual[1][:], 0)
        evaluated_individual = fitness_function(new_individual)
        evaluated_population.append(evaluated_individual)

    return evaluated_population
