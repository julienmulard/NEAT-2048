# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:15:32 2017

@author: Julien
"""

import NEATPopulation as Pop

pop = Pop.NEATPopulation(10,2,1)
pop.initializePopulation()
pop.mutate()
pop.splitPopulationInSpecies()

print('---------------Gen 0----------------------')
pop.printOrganismInSpecies()
for gen in range (10):
    
#pop.createNewGeneration() detailed:    
#    pop.prepareSpeciesForNewGen() detailed
    for species in pop.species_list:
#            species.prepareForNewGeneration()
            input("Species at the beginning of the generation")
            species.printOrganismList()            
            input("Keep only the best half")            
            species.keepOnlyTheBestHalf()        
            species.printOrganismList()   
            input("Set random rep")
            species.setRandomRep()
            species.printOrganismList()  
#        self.clearSpecies()
            input("Generate New Half")            
            species.generateNewHalf()
            species.printOrganismList()
            
    pop.getPopulationInSpecies()    
    pop.mutate()
    pop.splitPopulationInSpecies()
        
    print()
    input('---------------Gen '+str(gen+1) +'----------------------')
    pop.printOrganismInSpecies()    
    
