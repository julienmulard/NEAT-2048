# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:43:53 2017

@author: Julien
"""

import NEATPopulation as Pop

pop = Pop.NEATPopulation(2,2,1)
pop.initializePopulation()

org1 = pop.organism_list[0]
org2 = pop.organism_list[1]
org1.addGeneFull(1,1000001,1, True, -1)
pop.computeGeneInnovation(org1.genome[0])

org1.printGenomeFull()
print('------------')

org2.addGeneFull(1,1000001,1, True, -1)
org2.addGeneFull(0,1000001,1, True, -1)
org2.addGeneFull(2,1000001,1, True, -1)
pop.computeInnovation(org2)


org2.printGenomeFull()

pop = Pop.NEATPopulation(150,2,1)
pop.initializePopulation()

for i in range (100):
    pop.mutate()

pop.organism_list[0].drawOrganism()
input()
pop.killAllPopulation()
pop = Pop.NEATPopulation(150,2,1)
pop.initializePopulation()
for i in range(100):
    print('-----Gen '+str(i)+'------')    
    pop.mutate()
    pop.manageSpecies()
    pop.printSpeciesList()
    pop.prepareSpeciesForNewGen()
    
    
