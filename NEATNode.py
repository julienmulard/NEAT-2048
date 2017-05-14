# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:33:02 2017

@author: Julien
"""
import copy

class NEATNode:
    
    def __init__(self, node_index, node_type, graphic_layer):
        
        self.index = node_index
        self.type = node_type
        self.value = 0
        
        self.graphic_layer = graphic_layer
        self.posx = 0
        self.isDrawn = False
        
    def printNode(self):
        print(str(self.index) + ': ' + self.type)
        
    def printNodeFull(self):
        self.printNode()
        print(self.value)
        print(str(self.graphic_layer) + ' ' + str(self.posx) + ' ' + str(self.isDrawn))

    def copyNode(self):
        return copy.copy(self)
        
#-------------To be tested--------------#
    