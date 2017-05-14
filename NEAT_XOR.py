# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:31:39 2017

@author: Julien
"""

import NEATPopulation as Pop
import sys

pop = Pop.NEATPopulation(150,2,1)
pop.initializePopulation()
pop.mutate()
pop.splitPopulationInSpecies()
pop.clearMutationList()
pop.max_gen_dist = 3

org1 = ""
for gen in range(100):
    print('-----------------GEN '+str(gen)+'-----------------')
    for spec in pop.species_list:
#        print(spec.name)
        for org in spec.organism_list:
        
            out1 = org.computeOutput([0,0])
            out2 = org.computeOutput([0,1])
            out3 = org.computeOutput([1,1])
            out4 = org.computeOutput([1,0])
    
            dist1 = abs(out1[0]-0)
            dist2 = abs(out2[0]-1)
            dist3 = abs(out3[0]-0)
            dist4 = abs(out4[0]-1)
            
            fit = (dist1 + dist2 + dist3 + dist4)
            fit *= fit
            org.fitness = fit            
            if(org.fitness>15.9):
                org.drawOrganism()
                org1 = org
                print(org.fitness)                
                sys.exit()
#            print(fit)
         
         
        spec.updateFitnessMaxAndAvg()   
    for spec1 in pop.species_list:
        print(spec1.name)
        print(spec1.gen_max_fitness)
        print(spec1.avg_fitness)
#    input()
    pop.createNewGenerationV2()
    pop.clearMutationList()    
#    