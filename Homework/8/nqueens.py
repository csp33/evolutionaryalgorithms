import random
import numpy
import time
from deap import algorithms, base, creator, tools
import matplotlib.pyplot as plt


class nqueens:
    def __init__(self, n, generations, initial_population_size, mutation_chance, crossover_chance):
        self.n = n
        self.generations = generations
        self.initial_population_size = initial_population_size
        self.mutation_chance = mutation_chance
        self.crossover_chance = crossover_chance
        # Define the problem
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        # Set the toolbox
        self.toolbox = base.Toolbox()
        self.toolbox.register("permutation", random.sample,
                         range(self.n), self.n)

        # Individual and population creators
        self.toolbox.register("individual", tools.initIterate,
                         creator.Individual, self.toolbox.permutation)
        self.toolbox.register("population", tools.initRepeat,
                         list, self.toolbox.individual)

        # Fitness function
        self.toolbox.register("evaluate", self.get_fitness)

        # Crossover
        self.toolbox.register("mate", tools.cxPartialyMatched)
        # Mutation
        self.toolbox.register("mutate", tools.mutShuffleIndexes,
                         indpb=self.mutation_chance * 10 / self.n)
        # Selection
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        # Initialize random seed
        random.seed(0)

        # Define the population
        self.pop = self.toolbox.population(n=self.initial_population_size)
        # Best individual will be stored here
        self.hof = tools.HallOfFame(1)

        # Statistics
        self.stats = tools.Statistics(lambda ind: ind.fitness.values)
        self.stats.register("Avg", numpy.mean)
        self.stats.register("Std", numpy.std)
        self.stats.register("Min", numpy.min)
        self.stats.register("Max", numpy.max)

    def get_fitness(self, individual):
        # As there are permutations, we have to check only the diagonals
        # (queens won't be in the same row or column)

        # Create the diagonals
        left_right_diagonal = [0 for i in range(2 * self.n - 1)]
        right_left_diagonal = [0 for i in range(2 * self.n - 1)]
        # Add the queens to the diagonals
        for i in range(self.n):
            left_right_diagonal[i + individual[i]] += 1
            right_left_diagonal[(self.n - 1 - i) + individual[i]] += 1
        fitness = 0
        for i in range(2 * self.n - 1):
            fitness += left_right_diagonal[i] - \
                1 if left_right_diagonal[i] > 1 else 0
            fitness += right_left_diagonal[i] - \
                1 if right_left_diagonal[i] > 1 else 0
        return fitness,

    def genetic_algorithm(self):
        # Run the algorithm
        algorithms.eaSimple(self.pop, self.toolbox, cxpb=self.crossover_chance, stats=self.stats, mutpb=self.mutation_chance,
                            ngen=self.generations, halloffame=self.hof, verbose=False)

        return self.hof[0]
    def increase_generations_by(self,n):
        if n>0:
            self.generations += n

    def plot(self, individual):
        y = individual
        x = range(self.n)
        x = numpy.array(x)
        y = numpy.array(y)
        x = x + 0.5
        y = y + 0.5
        plt.figure()
        plt.scatter(x, y)
        plt.xlim(0, self.n)
        plt.ylim(0, self.n)
        plt.xticks(x - 0.5)
        plt.yticks(x - 0.5)
        plt.grid(True)
        plt.title(u"Best individual")
        plt.show()
