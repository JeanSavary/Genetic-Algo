# -- External imports -- #
from random import sample 
import operator
import numpy as np

# -- Internal imports -- #
from src.city import City
from src.route import Route

class Population:

    def __init__(self, population_size, cities):

        '''
            Description: Initialize a population composed of routes
            Params: population_size (int), cities (dict({'A': (coordX, coordY), ...}))
            Output: None

            NB: modifier cette classe pour n'avoir en paramètre qu'une liste de routes
        '''

        cities_list = [city_name for city_name in cities.keys()]
        routes = []

        for iteration in range(population_size) :

            iteration_cities = [City(city_name, cities[city_name][0], cities[city_name][1]) for city_name in sample(cities_list, len(cities_list))]
            route = Route(iteration_cities)
            routes.append(route)

        self.routes = routes
        self.size = len(self.routes)

        pass 

    def rankRoutes(self):

        '''
            Description: Rank all the routes in the current population based on their fitness score
            Params: None
            Output: List(tuple)
        '''

        ranked_routes = {}
        for route in self.routes: 
            ranked_routes[route] = route.computeFitness()

        return sorted(
            ranked_routes.items(),
            key = operator.itemgetter(1),
            reverse = True
        )

    def describe(self) :

        '''
            Description: Display all routes contained in the current population
            Params: None
            Output: None
        '''

        
        print("debug plz")