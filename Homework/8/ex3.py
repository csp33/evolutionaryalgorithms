import random
import numpy
from deap import algorithms, base, creator, tools
import matplotlib.pyplot as plt

n = 20
initial_population_size = 200
mutation_chance = 0.2
crossover_chance = 0.5
generations = 100


# Number of queens that can attack each other
def get_fitness(individual):
    # As there are permutations, we have to check only the diagonals
    # (queens won't be in the same row or column)

    # Create the diagonals
    left_right_diagonal = [0 for i in range(2 * n - 1)]
    right_left_diagonal = [0 for i in range(2 * n - 1)]
    # Add the queens to the diagonals
    for i in range(n):
        left_right_diagonal[i + individual[i]] += 1
        right_left_diagonal[(n - 1 - i) + individual[i]] += 1
    fitness = 0
    for i in range(2 * n - 1):
        fitness += left_right_diagonal[i] - \
            1 if left_right_diagonal[i] > 1 else 0
        fitness += right_left_diagonal[i] - \
            1 if right_left_diagonal[i] > 1 else 0
    return fitness,


def main():
    # Define the problem
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    # Set the toolbox
    toolbox = base.Toolbox()
    toolbox.register("permutation", random.sample,
                     range(n), n)

    # Individual and population creators
    toolbox.register("individual", tools.initIterate,
                     creator.Individual, toolbox.permutation)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Fitness function
    toolbox.register("evaluate", get_fitness)

    # Crossover
    toolbox.register("mate", tools.cxPartialyMatched)
    # Mutation
    toolbox.register("mutate", tools.mutShuffleIndexes,
                     indpb=mutation_chance * 10 / n)
    # Selection
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Initialize random seed
    random.seed(0)

    # Define the population
    pop = toolbox.population(n=initial_population_size)
    # Best individual will be stored here
    hof = tools.HallOfFame(1)

    # Statistics
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    # Run the algorithm
    algorithms.eaSimple(pop, toolbox, cxpb=crossover_chance, stats=stats, mutpb=mutation_chance,
                        ngen=generations, halloffame=hof, verbose=True)

    return hof[0]


def plot(individual):
    y = individual
    x = range(n)
    x = numpy.array(x)
    y = numpy.array(y)
    x = x + 0.5
    y = y + 0.5
    plt.figure()
    plt.scatter(x, y)
    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.xticks(x - 0.5)
    plt.yticks(x - 0.5)
    plt.grid(True)
    plt.title(u"Best individual")
    plt.show()


if __name__ == "__main__":
    best = main()
    print("The best individual is:\n{}".format(best))
    print("Its fitness is {}".format(best.fitness.values[0]))
    plot(best)
