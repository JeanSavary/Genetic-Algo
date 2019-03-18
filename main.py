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

def selection(ranked_population, elite_size):
    
    '''
        Description: Perform a roulette wheel selection, including an elite population
        Params: ranked_population ( list( (Route, fitness_score) ) )
        Output: list( Route )
    '''

    selection_results = [elem[0] for elem in ranked_population[:elite_size]] # We directly select our 'elite' population
    fitness_list = [elem[1] for elem in ranked_population] # Then we'll perform the "roulette wheel selection"

    df = pd.DataFrame(fitness_list, columns = ['fitness'])
    df['cum_sum'] = df.cumsum()
    df['cum_%'] = 100 * df['cum_sum'] / df['fitness'].sum()
   
    for iteration in range(len(fitness_list) - elite_size):

        threshold = uniform(0, 100)
        for index, _ in enumerate(fitness_list) : 

            if threshold <= df.iloc[index]['cum_%'] : 

                chosen_route = ranked_population[index][0]
                selection_results.append(chosen_route)
                break

    return selection_results

def crossOver(first_parent, second_parent):

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

    #print("\nStart : {} / End : {}\n".format(start_point, end_point))

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

        #print("Perform mutation between city {} and {} !".format(route.cities[mutation_index[0]].name, route.cities[mutation_index[1]].name))
        mutated_cities[mutation_index[0]], mutated_cities[mutation_index[1]] = mutated_cities[mutation_index[1]], mutated_cities[mutation_index[0]]

        return Route(mutated_cities)

    else :

        #print("No mutation performed !")
        return route

def makeCouples(parents):

    '''
        Description: Each parent will be involved in 2 couples, so that each parent will contribute to the next generation
        respecting the previous generation size
        Params: parents (list(Route))
        Output: couples (list(tuple(Route, Route)))
    '''
    parents_pool = []
    for iteration in range(2):

        iteration_parents_pool = np.array(parents)
        np.random.shuffle(iteration_parents_pool)
        parents_pool += list(iteration_parents_pool)

    parents_pool = np.array(parents_pool).reshape(len(parents_pool) // 2, 2)

    couples = [(first_parent, second_parent) for (first_parent, second_parent) in parents_pool]
    
    return couples 

def nextPopulation(current_population, elite_size, mutation_rate):

    '''
        Description: Generate a new generation (population)
        Params: 
        Output:
        NB: We can also directly pass the elite population to the next gen without using them in crossOver()

    '''

    ranked_current_population = current_population.rankRoutes() #rank individuals inside our current population
    selected_routes = selection(ranked_current_population, elite_size) #list of routes

    couples = makeCouples(selected_routes)

    children = []

    for (first_parent, second_parent) in couples :

        child = crossOver(first_parent, second_parent)
        mutated_child = mutation(child, mutation_rate)
        children.append(mutated_child)

    return Population(children)
    
def bestRoute(population):

    '''
        Description: Compute and retrieve the best individual (route) of the generation
        Params: population (Population)
        Output: best_route (Route)
    '''

    best_route = population.rankRoutes()[0][0]
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

    # -- Enter the evolution process -- #

    fitness_scores = []
    current_population = initial_population

    for generation in range(GENERATIONS) :

        print("Generation {}\n".format(generation + 1))

        current_population = nextPopulation(current_population, ELITE_SIZE, MUTATION_RATE)

        current_best_individual = bestRoute(current_population).describe()

        print("""
        \tCurrent best distance : {}\n
        \tCurrent best fitness : {}\n
        \tCurrent best path : {}\n
        """.format(
            current_best_individual["Distance"],
            current_best_individual["Fitness"],
            current_best_individual["Cities"]
        ))
        
        fitness_scores.append(current_best_individual["Fitness"])
    
    print("""
    We have our champion !\n
    \tHere is the best path : {}\n
    \tWith a distance of : {}\n
    \tAnd a fitness of : {}
    """.format(
        current_best_individual["Cities"],
        current_best_individual["Distance"],
        current_best_individual["Fitness"])
    )

    plotEvolution(fitness_scores)