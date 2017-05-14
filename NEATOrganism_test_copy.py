# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:31:48 2017

@author: Julien
"""

import NEATOrganism as Org

org1 = Org.NEATOrganism(2,2)
org1.initializeNodes()
org1.addGeneFull(1,1000001,3,True,0)
org1.addGeneFull(2,1000002,3,True,0)
org1.addNodeInGene(org1.genome[0])
org1.drawOrganism()

org2 = org1.copyOrganism()
org2.drawOrganism()
org2.genome[2].weight = -3

org1.drawOrganism()
org2.drawOrganism()

org1.genome[1].weight = -3
org1.drawOrganism()
org2.drawOrganism()

org1 = Org.NEATOrganism(2,2)
org1.initializeNodes()
org2 = org1.copyOrganism()

for i in range(10):
    org1.mutate(0.8,0.1,0.5,0.5)
    
for i in range (10):
    org2.mutate(0.8,0.1,0.5,0.5)
    
org1.drawOrganism()
org2.drawOrganism()