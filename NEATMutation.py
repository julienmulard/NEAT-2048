# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:10:41 2017

@author: Julien
"""

class NEATMutation:
    
    def __init__(self, input_node, output_node, innovation):
        
        self.input_node = input_node
        self.output_node = output_node
        self.innovation = innovation

    def printMutation(self):
        
        print(str(self.innovation) + ': ' + str(self.input_node) + "->" + str(self.output_node))