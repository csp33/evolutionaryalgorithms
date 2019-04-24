import sys
from nqueens import *

MEASURE_TIME = False


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print("You must specify the number of queens.")
        exit(-1)
    n = int(sys.argv[1])
    initial_population_size = 200
    mutation_chance = 0.2
    crossover_chance = 0.5

    fitness = 1
    generations = 1
    instance = nqueens(n, generations, initial_population_size,
                       mutation_chance, crossover_chance)
    while fitness > 0:
        instance.increase_generations_by(10)
        start = time.time()
        best = instance.genetic_algorithm()
        end = time.time()
        fitness = best.fitness.values[0]
    if MEASURE_TIME:
        print("{} {}".format(n, end - start))
    else:
        print("The best individual is:\n{}".format(best))
        print("Its fitness is {}".format(best.fitness.values[0]))
        print("Number of necessary generations: {}".format(instance.generations))
        instance.plot(best)
