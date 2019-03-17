# -- External imports -- #
from random import sample 
import operator
import numpy as np

# -- Internal imports -- #
from src.city import City
from src.route import Route

class Population:

    def __init__(self, routes):

        '''
            Description: Initialize a population composed of routes
            Params: population_size (int), cities (dict({'A': (coordX, coordY), ...}))
            Output: None
        '''

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

        for route_index, route in enumerate(self.routes) :

            print("\nRoute n° {} :\n".format(route_index))
            print(route.describe())

        pass