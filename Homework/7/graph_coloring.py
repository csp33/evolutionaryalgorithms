from random import random, randint
class graph_coloring:
    def __init__(self, adj_matrix, generations,
                 population_size, mutation_chance):
        self.vertices = len(adj_matrix[0])
        self.generations = generations
        self.adj_matrix = adj_matrix
        self.population_size = population_size
        self.mutation_chance = mutation_chance
        self.colors = [i for i in range(self.vertices)]
        self.create_population()

    def create_individual(self):
        individual = []
        for i in range(self.vertices):
            #Choose a random color
            position = randint(0,len(self.colors)-1)
            #Color the vertex with it
            individual.append(self.colors[position])
        return individual


    def create_population(self):
        self.population = []
        for i in range(self.population_size):
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

    def mutate(self,individual):
        return individual

    def mutation(self):
        if random() <= self.mutation_chance:
            position = randint(0, len(self.population) - 1)
            self.population[position] = self.mutate(self.population[position])

    def crossover(self,a,b):
        new_individual = []
        breakpoint = randint(0,self.vertices-1)
        new_individual[:breakpoint] = a[:breakpoint]
        new_individual[breakpoint:] = b[breakpoint:]
        return new_individual


    def sort_population(self):
        fitnesses = [(self.get_fitness(i), i)
                     for i in self.population]
        self.population = [i[1] for i in sorted(fitnesses)]

    def is_feasible(self,individual):
        for i in range(0,len(individual)-1):
            if self.adj_matrix[i][i+1] and individual[i] == individual[i+1]:
                return False
        return True


    def selection_and_reproduction(self):
        self.sort_population()
        a, b = self.population[0], self.population[1]
        new_individual = self.crossover(a, b)
        while not self.is_feasible(new_individual):
            new_individual = self.crossover(a, b)
        self.population.append(new_individual)

    def genetic_algorithm(self):
        for i in range(self.generations):
            self.selection_and_reproduction()
            self.mutation()
        self.sort_population()

    def get_population(self):
        return self.population
