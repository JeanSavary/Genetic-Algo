# -- Define all global variables for the projetct -- #

GENERATIONS = 30
MUTATION_RATE = .15 # 30% chance that a specific individual mutate during a generation
POPULATION_SIZE = 20
ELITE_SIZE = int(.2 * POPULATION_SIZE ) # 20% of our population size
CITIES = {
    "A": (5, 10), 
    "B": (3, 8), 
    "C": (4.7, 6), 
    "D": (4.3, 4), 
    "E": (5.3, 8.2), 
    "F": (6, 4.4)
}
