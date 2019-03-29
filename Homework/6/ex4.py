from tsp import TSP

generations = 10
population_size = 3
mutation_chance = 0.2
adj_matrix = [1, 0, 0], [0, 1, 0], [0, 0, 1]


instance = TSP(adj_matrix, generations, population_size, mutation_chance)
instance.genetic_algorithm()
population = instance.get_population()

print("The best individual is {} and its fitness is {}".format(
    population[0], instance.get_fitness(population[0])))
