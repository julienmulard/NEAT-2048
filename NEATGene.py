# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:27:29 2017

@author: Julien
"""

import copy
import random

class NEATGene:
    
    def __init__(self, input_node, output_node, weight, isEnable, innovation):
        
        self.input_node = input_node
        self.output_node = output_node
        self.weight = weight
        self.isEnable = isEnable
        self.innovation = innovation
    
    def copyGene(self):
        return copy.copy(self)
        
    
    def printGene(self):
        no_color_str = '\x1b[39m'
        if self.isEnable == False:
            color_str = '\x1b[31m'
        else:
            color_str = no_color_str            
        print(color_str + str(self.innovation) + ': ' + str(self.input_node) + ' -> ' + str(self.output_node) + no_color_str)
        
    def printGeneFull(self):
        self.printGene()
        print(self.weight)


    def mutateWeight(self, weight_shuffle_proba):
        if random.random() < weight_shuffle_proba:
            self.weight = random.random()*4-2
        else:
            self.weight += random.random()*0.2-0.1
            
#-------------------To Be Tested----------------#

    
            