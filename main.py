#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- External imports -- #


# -- Internal imports -- #

from city import City
from population import Population

# -- Global variables -- # 

GENERATIONS = 10
MUTATION_RATE = .2
POPULATION_SIZE = 50
ELITE_SIZE = 10 # 20% of the original population size

def selection() :
    return 

def crossOver() :
    return 

def mutation() :
    return 


if __name__ == '__main__' :

    population = Population(4)
    population.describe()

    print('\n', population.rankRoutes())