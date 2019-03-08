import itertools
N = 8 # Size of the word

def hamming_distance(a, b):
    distance = 0
    for i in range(N):
        if a[i] != b[i]:
            distance = distance + 1
    return distance


combinations = list(map(list, itertools.product([0, 1], repeat=N)))

# Now we have all the possible combinations that can be made with N bits

codebook = []
# We attach the first combination to the codebook.
codebook.append(combinations[1])

for i in combinations:
    if all(hamming_distance(i, j) >= 3 for j in codebook):
        codebook.append(i)


print("Codebook for {}-bit words (one-bit correction):\n{}".format(N, codebook))

print("The lenght of the codebook is {}".format(len(codebook)))
