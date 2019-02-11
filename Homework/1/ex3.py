from genetic_algorithm import *
from parameters import *


# Show the grid
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in grid]))


population = get_population()

print("First population:\n{}\n".format(population))

for i in range(generations):
    population = selection_and_reproduction(population)
    population = mutation(population)

population=sort_population(population)
best_individual = population[0]
best_fitness = get_fitness(best_individual)

if best_fitness == NOT_SUITABLE:
    print("The genetic algorithm could not find a solution.")
    exit(-1)
else:
    print("Best solution: {} -> {} -> fitness = {}".format(best_individual,
                                                           get_phenotype(best_individual), best_fitness))
"""
    print("Final population (phenotype):")
    for i in population:
        print(get_phenotype(i))
    print("Fitnesses:")
    for i in population:
        print("{} ->{}".format(i, get_fitness(i)))
"""
