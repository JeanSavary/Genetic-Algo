#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- External imports -- #
import os
import numpy as np 
import pandas as pd
from random import uniform

# -- Internal imports -- #
from src.city import City
from src.population import Population
from var.variables import *

# -- Global variables -- # 

def selection(ranked_population, elite_size) :
    
    selection_results = [elem[0] for elem in ranked_population[:elite_size]] # We directly select our 'elite' population
    fitness_list = [elem[1] for elem in ranked_population[elite_size:]] # Then we'll perform the "roulette wheel selection"

    df = pd.DataFrame(fitness_list, columns = ['fitness'])
    df['cum_sum'] = df.cumsum()
    df['cum_%'] = 100 * df['cum_sum'] / df['fitness'].sum()
   
    for iteration in range(len(fitness_list)):

        threshold = uniform(0, 100)
        for index, _ in enumerate(fitness_list) : 

            if threshold <= df.iloc[index]['cum_%'] : 

                chosen_route = ranked_population[elite_size + index][0]
                selection_results.append(chosen_route)
                break

    return selection_results

def crossOver() :
    return 



def mutation() :
    return 


if __name__ == '__main__' :

    initial_population = Population(POPULATION_SIZE, CITIES)
    selection(initial_population.rankRoutes(), ELITE_SIZE)
    
