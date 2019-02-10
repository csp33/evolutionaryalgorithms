from random import randint, random, sample
from parameters import *


def is_suitable(individual):
    if sum(individual) == 0 or sum(individual) >= N:
        return False
    x, y = 0, 0
    for i in individual:
        if i == RIGHT:
            x += 1
        else:
            y += 1
        if x >= N or y >= N:
            return False
    return True


def get_individual():
    individual = [randint(RIGHT, DOWN)
                  for i in range(genotype_size)]
    # If it is not suitable, we generate a new one.
    if not is_suitable(individual):
        individual = get_individual()

    return individual


def get_population():
    population = [get_individual()
                  for i in range(population_size)]
    return population


def get_fitness(individual):
    x, y = 0, 0
    fitness = 0
    for i in individual:
        if i == RIGHT:
            x += 1
        else:
            y += 1
        if x >= N or y >= N:
            # As we try to minimize the fitness, this high value will discard the individual from future generations.
            return NOT_SUITABLE
        fitness += grid[x][y]
    return fitness


def selection_and_reproduction(population):
    fitnesses = [(get_fitness(i), i) for i in population]
    # Sort the individuals according to their fitness
    fitnesses = [i[1] for i in sorted(fitnesses)]
    population = fitnesses

    # Select the ones with the lowest fitness
    selected = fitnesses[0:parents_size]

    for i in range(len(population) - parents_size):
        breakpoint = randint(1, genotype_size - 1)  # Choose the breakpoint
        parents = sample(selected, 2)  # Select two parents

        new_individual = [0 for x in range(genotype_size)]
        # Mix the genotypes
        new_individual[:breakpoint] = parents[0][:breakpoint]
        new_individual[breakpoint:] = parents[1][breakpoint:]
        # If the individual is not suitable, we skip it.
        if is_suitable(new_individual):
            population[i] = new_individual
            print("suitable {}".format(new_individual))
    return population


def mutation(population):
    for i in range(len(population) - parents_size):
        if random() <= mutation_chance:
            point = randint(0, genotype_size - 1)
            new_individual = population[i]
            new_individual[point] = RIGHT if new_individual[point] == DOWN else DOWN
            if is_suitable(new_individual):
                population[i] = new_individual
                print("generated {}".format(new_individual))
    return population


def get_phenotype(individual):
    phenotype = ""
    for i in individual:
        if i == RIGHT:
            phenotype += "RIGHT "
        else:
            phenotype += "DOWN "
    return phenotype
