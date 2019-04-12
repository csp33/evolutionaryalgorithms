from graph_coloring import graph_coloring
import csv
import sys

WRITE_TO_FILE = True


def readcsv(file):
    matrix = [[]]
    try:
        reader = csv.reader(open(file, "r"), delimiter=",")
    except:
        print("The file {} could not be opened".format(file))
        exit()
    matrix = list(reader)
    return matrix


def write_to_file(filename, individual,fitness):
    file = open(filename, 'w')
    for i in individual:
        file.write("{} ".format(i))
    file.write("\nFitness: {}".format(fitness))
    file.close()
    return


if len(sys.argv) != 2:
    print("You have to specify the filename!")
    exit()

generations = 100
initial_population_size = 20
mutation_chance = 0.3

adj_matrix = readcsv(sys.argv[1])

instance = graph_coloring(adj_matrix, generations,
                          initial_population_size, mutation_chance)
instance.genetic_algorithm()
population = instance.get_population()

print("Number of generations: {}".format(generations))
print("Size of the initial population: {}".format(initial_population_size))
print("Size of the final population: {}".format(len(population)))
print("Mutation chance: {}".format(mutation_chance))
print("Size of the graph: {}".format(len(adj_matrix)))
best = population[0]
if not WRITE_TO_FILE:
    print("Best individual:\n{}".format(instance.decode_individual(best)))
else:
    filename = sys.argv[1]
    filename = "results/result_{}.txt".format(filename[filename.index('/') + 1:filename.index('.')])
    write_to_file(filename, best,instance.get_fitness(best))
    print("Result written to file {}".format(filename))
print("Fitness of the best individual: {}".format(instance.get_fitness(best)))
