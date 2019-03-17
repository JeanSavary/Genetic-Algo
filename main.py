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
from src.population import Route
from var.variables import *

# -- Main functions -- #
def selection(ranked_population, elite_size) :
    
    '''
        Description: Perform a roulette wheel selection, including an elite population
        Params: ranked_population ( list( (Route, fitness_score) ) )
        Output: list( Route )

        NB: We might want to also include the elite population (our top 20% in the roulette wheel selection, but here it's not the case)
    '''

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

def crossOver(first_parent, second_parent) :

    '''
        Description: Create a child after mixing information from the 2 parents
        Params: first_parent (Route), second_parent (Route)
        Output: child (Route)
    '''

    # print("\nParents : \n")
    # print(first_parent.describe())
    # print(second_parent.describe())

    child = [None] * len(first_parent.cities)

    first_gene_index = int(uniform(0,1) * len(first_parent.cities))
    second_gene_index = int(uniform(0,1) * len(second_parent.cities))
    
    start_point = min(first_gene_index, second_gene_index) #index between which we will perform the cross-over
    end_point = max(first_gene_index, second_gene_index)

    print("\nStart : {} / End : {}\n".format(start_point, end_point))

    for index in range(start_point, end_point + 1):
        child[index] = first_parent.cities[index].name
    
    queue_second_parent_cities = [city.name for city in second_parent.cities if city.name not in child]
    
    for index, city_name in enumerate(child) :
        if city_name is None :
            child[index] = queue_second_parent_cities.pop(0)

    #print(Route([City(city_name, CITIES[city_name][0], CITIES[city_name][1]) for city_name in child]).describe())
    return Route([City(city_name, CITIES[city_name][0], CITIES[city_name][1]) for city_name in child])

def mutation() :
    return 


if __name__ == '__main__' :

    initial_population = Population(POPULATION_SIZE, CITIES)
    
    routeA = initial_population.routes[0]
    routeB = initial_population.routes[1]

    print(routeA.describe())
    print(routeB.describe())

    crossOver(routeA, routeB)