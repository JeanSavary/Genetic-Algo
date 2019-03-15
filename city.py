import numpy as np

class City:

    def __init__(self, name, x, y):

        '''
            Description: Initialize a city, a gene of an individual (route)
            Params: name (String), x (float), y (float)
            Output: City
        '''

        self.name = name
        self.x = x
        self.y = y 

        pass

    def describe(self):
        
        '''
            Description: Retrieve the name, and coordinates of a city
            Params: None
            Output: String (description)
        '''

        return "City name : {}\n\n X coordinate : {}\n Y coordinate : {}\n".format(self.name, self.x, self.y)

    def distance(self, other_city):

        '''
            Description: Compute the distance between self and another city
            Params: City
            Output: float (distance)
        '''

        x_dist = abs(self.x - other_city.x)
        y_dist = abs(self.y - other_city.y)

        return np.sqrt((x_dist)**2 + (y_dist)**2)

    