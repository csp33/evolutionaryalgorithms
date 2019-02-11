from random import randint

N = 5  # Size of the grid
RIGHT = 0
DOWN = 1
NOT_SUITABLE = 1000000
genotype_size = 2*N - 2
population_size = 10
parents_size = 3
mutation_chance = 0.2
generations = 10
grid = [[0 if x == y == 0 or x == y == N - 1 else randint(1, 10)
         for x in range(N)] for y in range(N)]
