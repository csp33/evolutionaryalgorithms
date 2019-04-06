from random import random, randint


class graph_coloring:
    def __init__(self, adj_matrix, generations,
                 initial_population_size, mutation_chance):
        self.vertices = len(adj_matrix)
        assert(self.vertices != 0 and self.vertices!=None)
        self.generations = generations
        self.adj_matrix = adj_matrix
        self.initial_population_size = initial_population_size
        self.mutation_chance = mutation_chance
        self.colors = [i for i in range(self.vertices)]
        self.colorlist = ["color {}".format(i) for i in range(self.vertices)]
        self.create_population()

    def create_individual(self):
        individual = []
        current_color = 0
        individual.append(self.colors[current_color])
        for i in range(self.vertices - 1):
            if self.adj_matrix[i][i + 1] == "1":  # We need to use other color
                current_color += 1
            individual.append(self.colors[current_color])
        return individual

    def create_population(self):
        self.population = []
        for i in range(self.initial_population_size):
            individual = self.create_individual()
            # If two colors are next to each other,
            #       discard the individual.
            while not self.is_feasible(individual):
                individual = self.create_individual()
            self.population.append(individual)

    # Calculate the number of colors
    def get_fitness(self, individual):
        result = 0
        used_colors = []
        for i in individual:
            if i not in used_colors:
                used_colors.append(i)
                result += 1
        return result

    # a<b<limit
    def get_random_pair(self, limit):
        a = randint(0, limit - 2)
        b = randint(a + 1, limit - 1)
        return a, b

    def mutate(self, individual):
        a, b = self.get_random_pair(self.vertices)
        #individual[a:b] = reversed(individual[a:b])  # Adjacency problem
        individual[a], individual[b] = individual[b], individual[a] # Schedule problem
        return individual

    def mutation(self):
        if random() <= self.mutation_chance:
            position = randint(0, len(self.population) - 1)
            new_individual = self.mutate(self.population[position])
            if self.is_feasible(new_individual):
                self.population[position] = new_individual

    def crossover(self, a, b):
        new_individual = []
        breakpoint = randint(0, self.vertices - 1)
        new_individual[:breakpoint] = a[:breakpoint]
        new_individual[breakpoint:] = b[breakpoint:]
        return new_individual

    def sort_population(self):
        fitnesses = [(self.get_fitness(i), i)
                     for i in self.population]
        self.population = [i[1] for i in sorted(fitnesses)]

    def is_feasible(self, individual):
        for i in range(0, len(individual) - 1):
            if self.adj_matrix[i][i + 1] == "1" and individual[i] == individual[i + 1]:
                return False
        return True

    def selection_and_reproduction(self):
        self.sort_population()
        a, b = self.population[0], self.population[1]
        new_individual = self.crossover(a, b)
        if self.is_feasible(new_individual):
            self.population.append(new_individual)

    def genetic_algorithm(self):
        for i in range(self.generations):
            self.selection_and_reproduction()
            self.mutation()
        self.sort_population()

    def get_population(self):
        return self.population

    def decode_individual(self,individual):
        result = []
        for i in individual:
            result.append(self.colorlist[i])
        return result
