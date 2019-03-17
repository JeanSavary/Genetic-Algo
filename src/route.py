# -- Internal imports -- #
from src.city import City

class Route:

    def __init__(self, cities):
        
        '''
            Description: Initialize a route, which will be a individual in our population
            Params: list( City() )
            Output: None
        '''

        self.cities = cities
        self.distance = 0
        self.fitness = 0
        
        pass

    def computeDistance(self):

        '''
            Description: Compute the total distance of the route
            Params: None
            Output: self.distance (float)
        '''
        
        if self.distance == 0 :

            total_distance = 0

            for city_index, city in enumerate(self.cities) : 

                if not city_index == len(self.cities) - 1 :

                    total_distance += city.distance(self.cities[city_index + 1])

            self.distance = total_distance
        
        return self.distance 

    def computeFitness(self):
        
        '''
            Description: Compute the route fitness (fitness of an individual in our population)
            Params: None
            Output: self.fitness (float)
        '''

        if self.fitness == 0 :

            self.fitness = 1 / self.computeDistance()

        return self.fitness

    def describe(self) :

        '''
            Description: Retrieve information about the route
            Params: None
            Output: Dict
        '''

        return {
            "Cities": [city.name for city in self.cities], 
            "Distance": self.computeDistance(), 
            "Fitness": self.computeFitness()
        }