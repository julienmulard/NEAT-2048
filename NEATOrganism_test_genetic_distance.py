# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:10:58 2017

@author: Julien
"""

import NEATOrganism as Org

print("Genetic distance test")
org1 = Org.NEATOrganism(2,2)
org1.initializeNodes()

org2 = Org.NEATOrganism(2,2)
org2.initializeNodes()

print(org1.computeGeneticDistance(org2))
print(org2.computeGeneticDistance(org1))

org1.addGeneFull(1,1000001,2,True,0)
org2.addGeneFull(1,1000001,-2,True,0)

print(org1.computeGeneticDistance(org2))
print(org2.computeGeneticDistance(org1))

org1.addGeneFull(2,1000001,2,True,1)
org2.addGeneFull(1,1000002,2,True,2)

print(org1.computeGeneticDistance(org2))
print(org2.computeGeneticDistance(org1))

org1.addGeneFull(2,1000001,2,True,3)
org2.addGeneFull(1,1000002,2,True,4)

print(org1.computeGeneticDistance(org2))
print(org2.computeGeneticDistance(org1))

org1.addGeneFull(2,1000001,2,True,3)
org2.addGeneFull(1,1000002,2,True,4)

print(org1.computeGeneticDistance(org2))
print(org2.computeGeneticDistance(org1))
