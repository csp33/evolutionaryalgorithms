from tsp import TSP
from math import inf

generations = 10
population_size = 4
mutation_chance = 0.2
adj_matrix = [[inf, 10, 8, 3],
              [10, inf, 4, 2],
              [8, 4, inf, 1],
              [3, 2, 1, inf]]


instance = TSP(adj_matrix, generations, population_size, mutation_chance)
instance.genetic_algorithm()
population = instance.get_population()

print("Number of generations: {}\nSize of the population:{}\nMutation chance:{}".format(
    generations, population_size, mutation_chance))

print("The best individual is {} and its fitness is {}".format(
    population[0], instance.get_fitness(population[0])))
