from random import shuffle, randint, random


class TSP:
    # Constructor of the class
    def __init__(self, adj_matrix, generations, population_size, mutation_chance):
        self.cities = len(adj_matrix[0])
        self.generations = generations
        self.adj_matrix = adj_matrix
        self.population_size = population_size
        self.mutation_chance = mutation_chance
        self.create_population()

    # Create a random individual
    def get_individual(self):
        individual = [i for i in range(self.cities)]
        shuffle(individual)
        return individual

    def create_population(self):
        self.population = [self.get_individual()
                           for i in range(self.population_size)]

    # a<b<limit
    def get_random_pair(self, limit):
        a = randint(1, limit - 1)
        b = randint(a + 1, limit)
        return a, b

    # Inverse a subarray of the individual
    def inversion_mutation(self, individual):
        a, b = self.get_random_pair(self.cities)
        individual[a:b] = reversed(individual[a:b])
        return individual

    def mutation(self):
        if random() <= self.mutation_chance:
            position = randint(0, len(self.population))
            self.population[position] = self.inversion_mutation(
                self.population[position])

    def ex_crossover(self, a, b):
        child = []
        return child

    def get_fitness(self, individual):
        fitness = 0
        for i in range(self.cities - 2):
            fitness += self.adj_matrix[i][i + 1]
        # Back to the first city
        fitness += self.adj_matrix[0][self.cities - 1]
        return fitness

    # Sort according to the fitness
    def sort_population(self):
        fitnesses = [(self.get_fitness(i), i)
                     for i in self.population]
        self.population = [i[1] for i in sorted(fitnesses)]

    def selection_and_reproduction(self):
        self.sort_population()
        a, b = self.population[0], self.population[1]
        new_individual = self.ex_crossover(a, b)
        self.population.append(new_individual)

    def genetic_algorithm(self):
        print(self.population)
        for i in range(self.generations):
            self.selection_and_reproduction()
            self.mutation()
        self.sort_population()

    def get_population(self):
        return self.population
