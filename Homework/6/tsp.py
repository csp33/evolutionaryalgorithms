from random import shuffle, randint, random
from math import inf


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
            position = randint(0, len(self.population) - 1)
            self.population[position] = self.inversion_mutation(
                self.population[position])

    def create_neighbours_lists(self):
        lists = [[0 for x in range(self.cities)] for y in range(self.cities)]
        for city in range(self.cities):
            for neighbour in range(self.cities):
                if self.adj_matrix[city][neighbour] != inf and city != neighbour:
                    lists[city].append(neighbour)
        return lists

    def remove_from_lists(self, element, lists):
        for i in range(1, len(lists)):
            if element in lists[i]:
                lists[i].remove(element)
        return lists

    def random_node(self, lists, child):
        correct = False
        while not correct:
            node = randint(self.cities)
            if node not in child:
                correct = True
        return node

    def fewest_neighbours(self, lists, current):
        min = inf
        result = None
        for i in lists[current]:
            if len(lists[i]) < min:
                min = len(lists[i])
                result = lists[i]
        return result[0]

    def ex_crossover(self, a, b):
        lists = self.create_neighbours_lists()
        chosen_parent = a if random() % 2 == 0 else b
        current = chosen_parent[0]
        child = []
        while len(child) != self.cities:
            child.append(current)
            lists = self.remove_from_lists(current, lists)
            if len(lists[current]) == 1:
                new = self.random_node(lists, child)
            else:
                new = self.fewest_neighbours(lists, current)
            current = new
        return child

    def get_fitness(self, individual):
        fitness = 0
        for i in range(self.cities - 1):
            fitness += self.adj_matrix[individual[i]][individual[i + 1]]
        # Back to the first city
        fitness += self.adj_matrix[individual[0]][individual[self.cities - 1]]
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
        print("Initial population: {}".format(self.population))
        for i in range(self.generations):
            self.selection_and_reproduction()
            self.mutation()
        self.sort_population()

    def get_population(self):
        return self.population
