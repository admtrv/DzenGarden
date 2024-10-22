# Zen Garden

## Overview

This project implements a genetic algorithm to solve the Zen Garden problem, simulating a monk raking a garden filled with sand and immovable rocks. The goal is to find an optimal sequence of moves to maximize the raked area under specific movement rules.

## Task

The monk starts at the edge of the garden and can rake horizontally or vertically, but not diagonally. He must avoid rocks and already raked areas. The challenge is to determine the optimal path to maximize the raked area while following these rules.

![](http://www2.fiit.stuba.sk/~kapustik/zen-s.png)

## Algorithm
The algorithm evolves a population of possible solutions, iterating through:

- **Initialization**: Generating random starting solutions.
- **Fitness Evaluation**: Measuring how much of the garden is covered.
- **Selection and Crossover**: Combining solutions to produce new generations.
- **Mutation and Elitism**: Introducing random changes to maintain diversity and keeping top solutions.

The process repeats for a set number of generations or until an optimal solution is reached.

## How to Run
1. Clone the repository:

```bash
git clone https://github.com/admtrv/ZenGarden.git
```

2. Run Key Files:
- `algorithm.py`: Implements the genetic algorithm logic
- `test.py`: Automates parameter testing to optimize the algorithm
- `graph.py`: Visualizes the impact of different parameters using graphs

## Dependencies

The only external library used is matplotlib for plotting:

```bash
pip install matplotlib
```

## Documentation
Full documentation is located in the `doc/`.