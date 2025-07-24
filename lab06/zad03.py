import numpy as np
import pygad
import random

CHROMOSOME_LENGTH = 30

maze = np.array([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
])

start = (0, 0)
end = (9, 9)

def random_chromosome():
    return [random.randint(0, 3) for _ in range(CHROMOSOME_LENGTH)]

def move(pos, direction):
    x, y = pos
    if direction == 0:
        x -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        y += 1
    return x, y

def apply_moves(solution):
    path = [start]
    x, y = start
    for direction in solution:
        x2, y2 = move((x, y), direction)
        if 0 <= x2 < 10 and 0 <= y2 < 10 and maze[x2][y2] == 0:
            x, y = x2, y2
            path.append((x, y))
    return path

def fitness_func(ga_instance, solution, solution_idx):
    path = apply_moves(solution)
    last_pos = path[-1]
    dist = abs(end[0] - last_pos[0]) + abs(end[1] - last_pos[1])
    if last_pos == end:
        return 1000
    return 100 - dist


gene_space = [0, 1, 2, 3]
sol_per_pop = 50
num_genes = 30

num_run = 10

for run in range(num_run):
    ga_instance = pygad.GA(
        num_generations=100,
        num_parents_mating=10,
        fitness_func=fitness_func,
        sol_per_pop=sol_per_pop,
        num_genes=num_genes,
        gene_space=gene_space,
        parent_selection_type='rank',
        keep_parents=5,
        mutation_type='random',
        mutation_percent_genes=10,
        stop_criteria=['reach_1000']
    )

    ga_instance.run()

    solution, solution_fitness, _ = ga_instance.best_solution()
    print("Najlepsza ścieżka:", apply_moves(solution))
    print("Fitness:", solution_fitness)

ga_instance.plot_fitness()