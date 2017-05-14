# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:07:42 2017

@author: Julien
"""

import NEATGene as Gen
import NEATNode as Nod

import random
import copy

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from math import exp

class NEATOrganism:
    
    def __init__(self, num_input, num_output):

        self.num_input = num_input
        self.num_output = num_output
        
        self.num_hidden = 0
                
        self.genome = []
        
        self.max_num_node = 1000000       
        self.node_list = []
        
        self.node_height = 0.1
        self.node_width = 0.1
        
        self.fitness = 0
        
        self.weight_range = 20
        
#-----------Node Methodes-----------#
        
    def initializeNodes(self):
        
        self.node_list.clear()        
        
        self.addNode(0, 'bias', 0)        
        
        for i in range(self.num_input):
            self.addNode(i+1, 'input', 0)
        
        for i in range (self.num_output):
            self.addNode(i+1+self.max_num_node, 'output', 5)

    def addNode(self, node_index, node_type, graphic_layer):
        
        node = Nod.NEATNode(node_index, node_type, graphic_layer)        
        self.node_list.append(node)    
    
    
    def addHiddenNode(self, graphic_layer):
        
        hidden_node_index = 1 + self.num_input + self.num_hidden
        self.addNode(hidden_node_index, 'hidden', graphic_layer)
        self.num_hidden += 1
    
    
    def getNode(self, index):
        self.sortNodeListByIndex()
        
        first_output_index = self.getFirstOutputNodeIndex()
        
        if index > self.max_num_node:
            index = index - self.max_num_node + first_output_index -1
        
        return self.node_list[index] 

    def getRandomInputNode(self):
        
        first_output_index = self.getFirstOutputNodeIndex()
        node_index = int(random.random()*first_output_index)
        return self.node_list[node_index]

    def getRandomOutputNode(self):
        
        node_index = int(random.random()*(self.num_hidden+self.num_output)+self.num_input+1)
        return self.node_list[node_index]

        
    def getFirstOutputNodeIndex(self):
        
        self.node_list.sort(key = lambda node: node.index)
        first_output_index = 1+self.num_input + self.num_hidden
        return first_output_index

    def sortNodeListByIndex(self):
        self.node_list.sort(key = lambda node: node.index)

    def sortNodeListByGraphicLayer(self):
        self.node_list.sort(key = lambda node: node.graphic_layer)

    def printNodes(self):
        for node in self.node_list:
            node.printNode()
            
    def printNodesFull(self):
        for node in self.node_list:
            node.printNodeFull()
            print('--------')

        
#---------------Gene Methods-----------------#
    
    def addGeneFull(self, node1_index, node2_index, weight, isEnable, innovation):
                
        gene = Gen.NEATGene(node1_index, node2_index, weight,isEnable, innovation)
        self.genome.append(gene)


    def addRandomGene(self):
        
        node1 = self.getRandomInputNode()
        node2 = self.getRandomOutputNode()

        if self.checkIfGeneExistsFromNode(node1, node2) == False:

            weight = (random.random()*2-1)*self.weight_range
            isEnable = True
            
            innovation = -1
            self.addGeneFull(node1.index, node2.index, weight, isEnable, innovation)        
            
        
    def getRandomGene(self):
        if self.genome != []:        
            gene_index = int(random.random()*len(self.genome))
            return self.genome[gene_index]
            
    def printGenome(self):
        for gene in self.genome:
            gene.printGene()
            
    def printGenomeFull(self):
        for gene in self.genome:
            gene.printGeneFull()
            
    def sortGenomeByInput(self):
        self.genome.sort(key = lambda gen: gen.input_node)

    def sortGenomeByOutput(self):
        self.genome.sort(key = lambda gen: gen.output_node)

    def sortGenomeByInnovation(self):
        self.genome.sort(key = lambda gen: gen.innovation)

    def checkIfGeneExistsFromNode(self, node1, node2):
        return self.checkIfGeneExistsFromIndex(node1.index, node2.index)
    
    def checkIfGeneExistsFromIndex(self, index1, index2):
        for gene in self.genome:
            if gene.input_node == index1 and gene.output_node == index2:
                return True
        return False

    def getFirstGeneWithInnovationToUpdate(self):
        self.sortGenomeByInnovation()
        if self.genome[0].innovation == -1:
            return self.genome[0]
        else:
            return None

    def initializeGenome(self):
        for input_node_index in range(self.num_input+1):
            for output_node_index in range(self.num_output):
                
                true_output_node_index = output_node_index + 1 + self.max_num_node                
                
                weight = (random.random()*2-1)*self.weight_range
                isEnable = True
            
                innovation = -1
                self.addGeneFull(input_node_index, true_output_node_index, weight, isEnable, innovation)                  
                
#------------Gene and Node Methods--------------#
        
    def addRandomNode(self):
        if self.genome != []:
            gene = self.getRandomGene()
            self.addNodeInGene(gene)
    
    def addNodeInGene(self, gene):    
        gene.isEnable = False
        node1 = self.getNode(gene.input_node)
        node2 = self.getNode(gene.output_node)
        
        graphic_layer = self.computeNewGraphicLayer(node1.graphic_layer, node2.graphic_layer)
        
        self.addHiddenNode(graphic_layer)
        new_node = self.node_list[-1]
        
        self.addGeneFull(node1.index, new_node.index, 1, True, -1)        
        self.addGeneFull(new_node.index, node2.index, gene.weight, True, -1)
        
    
        
#-------------Meta Methods -----------------------#     

    def mutate(self, weight_mut_proba, weight_shuffle_proba, add_gene_proba, add_node_proba):
        for gene in self.genome:
            if random.random() < weight_mut_proba:
                gene.mutateWeight(weight_shuffle_proba)
        
        if random.random() < add_gene_proba:
            self.addRandomGene()
        
        if random.random() < add_node_proba:
            self.addRandomNode()
            
        return
    
    def computeGeneticDistance(self, org):
        
        num_gene_in_common = 0
        sum_delta_weight = 0
        N = max(len(self.genome), len(org.genome))
        for gene1 in self.genome:
            for gene2 in org.genome:
                if gene1.innovation == gene2.innovation:
                    num_gene_in_common += 1
                    sum_delta_weight += abs(gene1.weight-gene2.weight)
        if num_gene_in_common != 0:        
            mean_delta_weight = sum_delta_weight / num_gene_in_common
        else:
            mean_delta_weight = 0
        
        if N != 0:  
            num_gene_diff = len(self.genome) + len(org.genome) - 2*num_gene_in_common 
            dist = 3*(num_gene_diff)/N + 0.2*mean_delta_weight
        else:
            dist = 0 
        return dist
        
    def computeOutput(self, input_array):
        
        self.inputNodeSetup(input_array)
        
        self.computeForwardPropagation()

        return self.getOutputNodesValues()
       
#------------------Computation----------------#

    def inputNodeSetup(self, input_array):
        if len(input_array) != self.num_input:
            print("Input_array is not of the expected size")
            return
        
        self.sortNodeListByIndex()
        self.node_list[0].value = 1
        
        for i in range(self.num_output):
            node = self.getNode(i+1)
            node.value = input_array[i]
            

    def computeForwardPropagation(self):        
        self.sortGenomeByOutput()
    
        if self.genome != []:        
        
            node_being_processed = self.genome[0].output_node        
            acc = 0        
            for gene in self.genome:
                if gene.output_node == node_being_processed:
                    input_node = self.getNode(gene.input_node)
                    acc += gene.weight*input_node.value
                    
                else:
                    output_node = self.getNode(node_being_processed)
                    output_node.value = self.sigmoid(acc)
                    
                    node_being_processed = gene.output_node
                    input_node = self.getNode(gene.input_node)
                    acc = gene.weight*input_node.value
                
                output_node = self.getNode(node_being_processed)
                output_node.value = self.sigmoid(acc)

    def getOutputNodesValues(self):
        output_array = []                
        for i in range(self.num_output):
            node = self.getNode(i+1+self.max_num_node)
            output_array.append(node.value)
        return output_array

    def sigmoid(self, x):
        return 1/(1+exp(-4.9*x))
#---------------Other---------------#
    
    def copyOrganism(self):
        
        return copy.deepcopy(self)
        
        
    

#----------------Graphics---------------------------#
        
    def insertNewGraphicLayer(self, new_graphic_layer_index):
        
        self.sortNodeListByGraphicLayer()
        for node in self.node_list:
            if node.graphic_layer >= new_graphic_layer_index:
                node.graphic_layer += 1
    
    def getMaxGraphicLayer(self):
        
        self.sortNodeListByGraphicLayer()
        return self.node_list[-1].graphic_layer
        
    def getNumNodesInGraphicLayer(self, graphic_layer):
        
        num = 0
        for node in self.node_list:
            if node.graphic_layer == graphic_layer:
                num += 1
        
        return num
        
    def computeNewGraphicLayer(self, graphic_layer1, graphic_layer2):
        
        mean = (graphic_layer1 + graphic_layer2)/2        
        
        if mean - int(mean) > 0:
            if abs(graphic_layer1 - graphic_layer2) == 1:            
                self.insertNewGraphicLayer(int(mean)+1)
                return int(mean)+1
            elif int(mean)+1 >= self.getMaxGraphicLayer():
                self.insertNewGraphicLayer(int(mean)+1)
                return int(mean)+1
            else:
                return int(mean)+1
        else:
            return mean

    def updateNodePosX(self):

        self.sortNodeListByGraphicLayer()
        node_index = 0       
        for i in range(self.getMaxGraphicLayer()+1):
            num_in_layer = self.getNumNodesInGraphicLayer(i)
            for j in range(num_in_layer):
                self.node_list[node_index].posx = j - num_in_layer/2
                node_index += 1
        
    
    def reinitAllNodesDrawnStatus(self):
        for node in self.node_list:
            node.isDrawn = False
            node.posx = round(node.posx)
            node.graphic_layer = round(node.graphic_layer)
    
        
    def drawRect(self, x, y, axes):
        
        x0 = x-self.node_width/2
        y0 = y-self.node_height/2        
        
        axes.add_patch(patches.Rectangle((x0, y0), self.node_width, self.node_height, fill = False))
     
    def drawNode(self, node, ax):
        if node.isDrawn == False:
            randx = random.random()*0.1
            randy = random.random()*0.2
            node.posx += randx
            node.graphic_layer += randy
            self.drawRect(node.posx, node.graphic_layer, ax)
            node.isDrawn = True        
    
    def drawLink(self, node1, node2, weight, ax):
        
        if weight > 0:
            if weight > 3:
                col = (0,1,0,1)
            else:
                col = (0,1,0,weight/3)
        else:
            if abs(weight) > 3:
                col = (1,0,0,1)
            else:
                col = (1,0,0,abs(weight)/3)        
        
        if node1.index == node2.index:
            ax.plot([node1.posx, node1.posx + 0.25, node1.posx + 0.25, node1.posx, node1.posx], [node1.graphic_layer, node1.graphic_layer, node1.graphic_layer+0.25, node1.graphic_layer+0.25, node1.graphic_layer], color = col)
#        ax.plot([node1.posx, node2.posx], [node1.graphic_layer, node2.graphic_layer])
        
        ax.quiver(node1.posx, node1.graphic_layer, node2.posx-node1.posx, node2.graphic_layer - node1.graphic_layer, scale_units='xy', angles='xy', scale=1, linewidth=0.5, color = col)
   
    def drawGene(self, gene, ax):
        
        node1 = self.getNode(gene.input_node)        
        node2 = self.getNode(gene.output_node)
        self.drawNode(node1,ax)
        self.drawNode(node2,ax)
        if (gene.isEnable):
            self.drawLink(node1, node2, gene.weight,ax)
            
            
    def drawOrganism(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)        
        
        self.sortNodeListByIndex()
        self.updateNodePosX()        
        
        for gene in self.genome:
            self.drawGene(gene, ax)  

        for node in self.node_list:
            self.drawNode(node, ax)       
        
        ax.axis('tight')
#        ax.axis('equal')
        fig.show()
        self.reinitAllNodesDrawnStatus()
                
        
#    def redrawOrganism(self):
#        
#        fig = plt.gcf()
#        plt.clf()
#        ax = fig.add_subplot(111)
#        self.sortNodeListByIndex()
#        self.updateNodePosX()        
#        
#        for gene in self.genome:
#            self.drawGene(gene, ax)  
#
#        for node in self.node_list:
#            self.drawNode(node, ax)       
#        
##        ax.axis('tight')
#        ax.axis('equal')
#        fig.show()
#        self.reinitAllNodesDrawnStatus()
        
#-------------------------To Be Tested---------------------

    def addGeneFromParent(self, gene, parent):
        self.addGeneFromGene(gene)
        
        if self.checkIfNodeExist(gene.input_node) == False:
            self.addNodeFromParent(gene.input_node, parent)
            self.num_hidden += 1
        
        if self.checkIfNodeExist(gene.output_node) == False:
            self.addNodeFromParent(gene.output_node, parent)
            self.num_hidden += 1
        return
        
    def addGeneFromGene(self, gene):
        self.addGeneFull(gene.input_node, gene.output_node, gene.weight, gene.isEnable, gene.innovation)
    
    def checkIfNodeExist(self, node_index):
        for node in self.node_list:
            if node.index == node_index:
                return True
            
        return False
        
    def addNodeFromParent(self, node_index, parent):
        node = parent.getNode(node_index)
        self.addNodeFromNode(node)
        
        
    def addNodeFromNode(self, node):
        self.addNode(node.index, node.type, node.graphic_layer)
        
    def clearNodesValue(self):
        for node in self.node_list:
            node.value = 0