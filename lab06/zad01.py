import pygad as pg
import numpy as np
import time

items = [
    {"name": "zegar", "value": 100, "weight": 7},
    {"name": "obraz-pejzaż", "value": 300, "weight": 7},
    {"name": "obraz-portret", "value": 200, "weight": 6},
    {"name": "radio", "value": 40, "weight": 2},
    {"name": "laptop", "value": 500, "weight": 5},
    {"name": "lampka nocna", "value": 70, "weight": 6},
    {"name": "srebrne sztućce", "value": 100, "weight": 1},
    {"name": "porcelana", "value": 250, "weight": 3},
    {"name": "figura z brązu", "value": 300, "weight": 10},
    {"name": "skórzana torebka", "value": 280, "weight": 3},
    {"name": "odkurzacz", "value": 300, "weight": 15},
]


values = [item['value'] for item in items]
weights = [item['weight'] for item in items]
weight_limit = 25

def fitness_func(ga_instance, solution, solution_idx):
    total_weight = np.sum(solution * weights)
    total_value = np.sum(solution * values)

    if total_weight > weight_limit:
        return 0
    else:
        return total_value

def on_generation(ga_instance):
    if ga_instance.best_solution()[1] == 1630:
        ga_instance.stop_generation = True

gene_space = [0, 1]
sol_per_pop = 10
num_genes = len(values)
num_parents_mating = 5
num_generations = 50
keep_parents = 2
parent_selection_type = 'sss'
crossover_type = 'single_point'
mutation_type = 'random'
mutation_percent_genes = 20

success_count = 0
total_time = 0
num_runs = 10

for run in range(num_runs):
    ga_instance = pg.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_func,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           on_generation=on_generation)

    start = time.time()
    ga_instance.run()
    end = time.time()

    solution, solution_fitness, _ = ga_instance.best_solution()

    if solution_fitness == 1630:
            success_count += 1
            total_time += (end - start)

    print("\nWybrane przedmioty:")
    for i, gene in enumerate(solution):
        if gene == 1:
            print(f"- {items[i]['name']} (wartość: {items[i]['value']} zł, waga: {items[i]['weight']} kg)")

success_rate = (success_count / num_runs) * 100
average_time = total_time / success_count if success_count > 0 else None

assert success_count <= num_runs, "Success count can't be greater than number of runs!"

print(f"\n✅ Skuteczność: {success_rate:.0f}%")
if average_time:
    print(f"⏱️ Średni czas znalezienia najlepszego rozwiązania: {average_time:.4f}s")
else:
    print("❌ Nie udało się znaleźć idealnego rozwiązania w żadnym z 10 uruchomień.")

ga_instance.plot_fitness()