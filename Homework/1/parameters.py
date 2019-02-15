from random import randint

N = 5  # Size of the grid
RIGHT = 0
DOWN = 1
NOT_SUITABLE = 1000000
genotype_size = 2 * N - 2
population_size = 10
parents_size = 3
mutation_chance = 0.2
generations = 10
grid = [[randint(1, 10) for x in range(N)] for y in range(N)]
grid = [[1 if x == N-1 or y == 0 else grid[x][y] for x in range(N)] for y in range(N)]
grid[0][0] = grid[N-1][N-1] = 0
optimal_solution = 2*N - 3
