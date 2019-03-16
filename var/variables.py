# -- Define all global variables for the projetct -- #

GENERATIONS = 10
MUTATION_RATE = .2
POPULATION_SIZE = int(input("Choose the size of the population :\t"))
ELITE_SIZE = int(.2 * POPULATION_SIZE )
CITIES = {
    "A": (5, 10), 
    "B": (3, 8), 
    "C": (4.7, 6), 
    "D": (4.3, 4), 
    "E": (5.3, 8.2), 
    "F": (6, 4.4)
}
