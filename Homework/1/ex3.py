from random import *

"""Constants"""

N=4 #Size of the grid
RIGHT=0
DOWN=1
genotipe_size=N+2
population_size=4
parents=3
mutation_chance=0.2


# Define the grid

grid = [[0 for x in range(N)] for y in range(N)]

#Fill it with the costs (random)

for x in range(N):
    for y in range(N):
        grid[x][y]=randint(1,10)

# Set start and end point costs to zero
grid[0][0]=0
grid[N-1][N-1]=0

def get_individual():
    individual = [randint(RIGHT, DOWN)
           for i in range(genotipe_size)]

    return individual

def get_population():
    population = [get_individual()
            for i in range(population_size)]
    return population

def get_fitness(individual):
    x,y = 0,0
    fitness = 0
    for i in individual:
        if i == RIGHT:
            x += 1
        else:
            y += 1
        fitness += grid[x][y]
    return fitness

def selection_and_reproduction(population):
    fitnesses = [ (get_fitness(i), i) for i in population]
    fitnesses = [i[1] for i in sorted(fitnesses)]
    population = fitnesses

    selected =  fitnesses[0:parents]


    for i in range(len(population)-parents):
        breakpoint = randint(1,genotipe_size-1)
        padre = sample(selected, 2)
        

        population[i][:breakpoint] = padre[0][:breakpoint]
        population[i][breakpoint:] = padre[1][breakpoint:]

    return population

def mutation(population):
    for i in range(len(population)-parents):
        if random() <= mutation_chance:
            breakpoint = randint(0,genotipe_size-1)
            new_value = randint(RIGHT,DOWN)
            while new_value == population[i][breakpoint]:
                new_value = randint(RIGHT,DOWN)

            population[i][breakpoint] = new_value

    return population
#Show the grid

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in grid]))


population = get_population()
print("First population: {}".format(population))

for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)


print("Final population (genotype): {}".format(population))
print("Final population (phenotype): ")
for i in population:
    for j in i:
        if j == RIGHT:
            print("RIGHT ",end='')
        else:
            print("DOWN ",end='')
    print("\n")


print("Fitnesses:")
for i in population:
    print("{} ->{}".format(i,get_fitness(i)))
