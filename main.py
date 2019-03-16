#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- External imports -- #
import os

# -- Internal imports -- #
from src.city import City
from src.population import Population
from var.variables import *

# -- Global variables -- # 

def selection() :
    return 

def crossOver() :
    return 

def mutation() :
    return 


if __name__ == '__main__' :

    population = Population(4, CITIES)
    population.describe()

    print('\n', population.rankRoutes())