"""
Main python file for MAP-Elites.
To run:
    # Import data
    from map_elites import Map_Elites
    
    # Fit the data
    me = MAP_Elites
    me.fit(training_data)
    
    # Print heatmap of MAP-Elites
    me.heatmap()

Notes:
    This code takes its inspiration from StefanoFioravanzo github
        https://github.com/StefanoFioravanzo/MAP-Elites

@author: Dáire Campbell <daire.d.campbell@gmail.com>

"""
import numpy as np
import math
import seaborn as sns


class MAP_Elites():
    """
    Class method to run MAP-Elites.
    """
    
    def __init__(
        self,
        verbose: bool == False,
    ):
        """
        Initialisation function for MAP_Elites.
        
        ::param verbose: (boolean) Print updates.
        """
        self.verbose = verbose
    
    def log(self, string):
        """
        Function to print statements.
        """
        if self.verbose:
            print(string)
    
    def fit(self):
        """
        Function to fit MAP-Elites on to the data.
        """
        pass
    
    def heatmap(self):
        """
        Function to print a heatmap of MAP-Elites fitted data.
        """
        pass
