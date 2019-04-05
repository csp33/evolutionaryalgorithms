from graph_coloring import graph_coloring
from math import inf

generations = 100
population_size =20
mutation_chance = 0.2
adj_matrix = [[1, 0, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 1, 0],
              [1, 0, 0, 1]]

instance = graph_coloring(adj_matrix, generations,
                          population_size, mutation_chance)
instance.genetic_algorithm()
population = instance.get_population()

print("Number of generations: {}\nSize of the population:{}\nMutation chance:{}".format(
    generations, population_size, mutation_chance))

print("The best individual is {} and its fitness is {}".format(
    population[0], instance.get_fitness(population[0])))
