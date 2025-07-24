import numpy as np
import pygad
import math

def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

def fitness_func(ga_instance, solution, solution_idx):
    x, y, z, u, v, w = solution
    return endurance(x, y, z, u, v, w)

gene_space = {'low': 0.0, 'high': 1.0}

ga_instance = pygad.GA(
    num_generations=100,
    num_parents_mating=10,
    fitness_func=fitness_func,
    sol_per_pop=20,
    num_genes=6,
    gene_space=gene_space,
    mutation_percent_genes=20,
    parent_selection_type='sss',
    keep_parents=2,
    crossover_type='single_point',
    mutation_type='random'
)

ga_instance.run()

solution, solution_fitness, _ = ga_instance.best_solution()
print("Najlepsze proporcje metaliL:", solution)
print("Maksymalna wytrzymałość (endurance):", solution_fitness)

ga_instance.plot_fitness()