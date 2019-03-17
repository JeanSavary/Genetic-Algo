#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- External imports -- #
import os
import numpy as np 
import pandas as pd
from random import uniform, sample
import matplotlib.pyplot as plt


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

def mutation(route, mutation_rate) :

    '''
        Description: Perfom a random mutation (with low probability) to an individual to avoir local convergence
        Params: route (Route), mutation_rate (float between 0 and 1)
        Output: route (Route)
    '''

    if (uniform(0,1) < mutation_rate) : # if the condition is valid then we will expose the individual to mutations

        mutation_index = sample([i for i in range(len(route.cities))], 2)
        mutated_cities = route.cities 

        print("Perform mutation between city {} and {} !".format(route.cities[mutation_index[0]].name, route.cities[mutation_index[1]].name))
        mutated_cities[mutation_index[0]], mutated_cities[mutation_index[1]] = mutated_cities[mutation_index[1]], mutated_cities[mutation_index[0]]

        return Route(mutated_cities)

    else :

        print("No mutation performed !")
        return route

def nextGeneration(routes):

    '''
        Description: Generate a new generation (population)
        Params: 
        Output:
    '''

    return 

def bestRoute(population):

    '''
        Description: Compute and retrieve the best individual (route) of the generation
        Params: population (Population)
        Output: best_route (Route)
    '''

    best_route = population.rankRoutes()[0][0]

    print("The best route is : \n{}".format(best_route.describe()))
    return best_route

def plotEvolution(best_fitness_scores):

    '''
        Description: Display the evolution of our best individual's fitness score for each generation
        Params: best_fitness_scores (list)
        Output: None
    '''

    generations = [i for i in range(1, len(fitness_scores) + 1)]

    plt.plot(generations, best_fitness_scores)
    plt.xlabel("Generation number")
    plt.ylabel("Best fitness score")
    plt.title("Evolution of the best fitness scores")
    plt.show()

    return

if __name__ == '__main__' :

    # -- Initialize our first population -- #

    cities_list = [city_name for city_name in CITIES.keys()]
    initial_routes = []

    for iteration in range(POPULATION_SIZE) :

        iteration_cities = [City(city_name, CITIES[city_name][0], CITIES[city_name][1]) for city_name in sample(cities_list, len(cities_list))]
        route = Route(iteration_cities)
        initial_routes.append(route)

    initial_population = Population(initial_routes)
    initial_population.describe()

    # -- Enter the evolution process -- #

    routeA = initial_population.routes[0]
    routeB = initial_population.routes[1]

    print(routeA.describe())
    print(routeB.describe())

    routeC = crossOver(routeA, routeB)

    print(routeC.describe())

    mutated_routeC = mutation(routeC, MUTATION_RATE)
    print(mutated_routeC.describe())

    bestRoute(initial_population)