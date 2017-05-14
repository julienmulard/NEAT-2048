# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:14:16 2017

@author: Julien
"""

import NEATPopulation as Pop
print("Population and species test")
print("Initial pop:")
pop = Pop.NEATPopulation(2,2,1)
pop.initializePopulation()
for i in range(10):
   pop.mutate()
    
pop.manageSpecies()
pop.printSpeciesList()

pop.printOrganismList()
print('-----------------------------')
print("Same population, got from species")
pop.printOrganismInSpecies()

input("What happen to the pop if we change an org in species?")
input("Spoilers: it should change both")
pop.species_list[0].organism_list[0].genome[0].innovation = 123456789

pop.printOrganismList()
print('-----------------------------')
print("Same population, got from species")
pop.printOrganismInSpecies()

input("What happen to the org in species if we pop them all out of pop.organisl_list?")
input("Spoiler: nothing :)")
pop.killAllPopulation()

pop.printOrganismList()
print('-----------------------------')
print("Same population, got from species")
pop.printOrganismInSpecies()