#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- External imports -- #
from random import sample 
import operator

# -- Internal imports -- #
from city import City
from route import Route

CITIES = {
    "A": (5, 10), 
    "B": (3, 8), 
    "C": (4.7, 6), 
    "D": (4.3, 4), 
    "E": (5.3, 8.2), 
    "F": (6, 4.4)
}

class Population:


    def __init__(self, population_size):

        cities = [city_name for city_name in CITIES.keys()]
        routes = []

        for iteration in range(population_size) :

            iteration_cities = [City(city_name, CITIES[city_name][0], CITIES[city_name][1]) for city_name in sample(cities, len(cities))]
            route = Route(iteration_cities)
            routes.append(route)

        self.routes = routes
        self.size = len(self.routes)

        pass 

    def rankRoutes(self):

        '''
            Description: Rank all the routes in the current population based on their fitness score
            Params: None
            Output: Dict
        '''

        ranked_routes = {}
        for route in self.routes: 
            ranked_route[route] = route.computeFitness()

        return sorted(
            ranked_routes.items(),
            key = operator.itemgetter(1),
            reverse = True
        )

    def describe(self) :

        print('Population composed of {} routes\n'.format(self.size))
        
        for route in self.routes :

            print(route.describe())

            
        pass
