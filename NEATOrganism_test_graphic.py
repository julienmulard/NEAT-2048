# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 06:29:32 2017

@author: Julien
"""

import NEATOrganism as Org
#
#org = Org.NEATOrganism(2,2)
#org.initializeNodes()
#
#input("Graphic methods test")
#print()
#input("Insert graphic layer test")
#input("Init org:")
#org.printNodesFull()
#print()
#
#input("Get max graphic layer")
#print(org.getMaxGraphicLayer())
#print()

#
#input("We insert at layer = 1:")
#org.insertNewGraphicLayer(1)
#org.printNodesFull()
#print()
#
#
#input("Get max graphic layer")
#print(org.getMaxGraphicLayer())
#print()
#
#input("We insert at layer = 0:")
#org.insertNewGraphicLayer(0)
#org.printNodesFull()
#print()
#
#print("Get max graphic layer")
#input()
#print(org.getMaxGraphicLayer())
#print()
#
#input()
#print("Get num nodes in graphic layer test")
#input("layer = 0")
#print(org.getNumNodesInGraphicLayer(0))
#input('layer=1')
#print(org.getNumNodesInGraphicLayer(1))
#input('layer=2')
#print(org.getNumNodesInGraphicLayer(2))
#input('layer=3')
#print(org.getNumNodesInGraphicLayer(3))
#print()
#
#input("Compute new graphic layer test")
#
#input("Init org:")
#org = Org.NEATOrganism(2,2)
#org.initializeNodes()
#org.printNodesFull()
#
#input("If layer1 = 0 and layer2 = 1")
#input("We want the output to be 1, and having a new layer inserted in 1")
#print(org.computeNewGraphicLayer(0,1))
#org.printNodesFull()
#
#input("If layer1 = 0 and layer2 = 2")
#input("We want the output to be 1, and having no new layer inserted in 1")
#print(org.computeNewGraphicLayer(0,2))
#org.printNodesFull()
#
#input("If layer1 = 0 and layer2 = 3")
#input("We want the output to be 2, and having a new layer inserted in 2")
#print(org.computeNewGraphicLayer(0,3))
#org.printNodesFull()
#
#input("If layer1 = 0 and layer2 = 1")
#input("We want the output to be 1, and having a new layer inserted in 1")
#print(org.computeNewGraphicLayer(0,1))
#org.printNodesFull()



input("Draw gene test")

input("Init org:")
org = Org.NEATOrganism(2,2)
org.initializeNodes()
org.printNodesFull()
org.drawOrganism()

input("Add a connexion between 1 and 1000001")
org.addGeneFull(1,1000001,3,True,0)
org.drawOrganism()

input("Add a connexion between 2 and 1000002")
org.addGeneFull(2,1000002,-3,True,0)
org.drawOrganism()

input("Add a node between 1 and 1000001")
org.addNodeInGene(org.genome[0])
org.printNodesFull()
org.drawOrganism()

input("Add a node between 1 and 1000001")
org.addNodeInGene(org.genome[1])
org.printNodesFull()
org.drawOrganism()

input("Add a connexion between 3 and 3")
org.addGeneFull(3,3,-3,True,0)
org.printNodesFull()
org.drawOrganism()


input("Add a connexion between 4 and 4")
org.addGeneFull(4,4,3,True,0)
org.printNodesFull()
org.drawOrganism()


#input("Draw gene test 2:")
#org = Org.NEATOrganism(2,2)
#org.initializeNodes()
#org.drawOrganism()
#for i in range(20):
#    org.mutate(0.8, 0.1, 0.2, 0.2)
#    org.drawOrganism()