# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:16:13 2017

@author: Julien
"""

import NEATPopulation as Pop

#print("New Generation Test")
#
#print("Let's do some basic test:")
#print("We have a pop of 10 org, each of 2 ins and 1 out")
#pop = Pop.NEATPopulation(10,2,1)
#
#input("We initialize the population, i.e we initialize each org node_list")
#input("Before:")
#for org in pop.organism_list:
#    org.printNodeList()
#    print('-------')
#
#input("After:")
#pop.initializePopulation()
#for org in pop.organism_list:
#    org.printNodes()
#    print('-------')
#
#
#input("The genomes are still empty though:")
#pop.printOrganismList()
#
#input("Now, let's add some genetic info in the first 2 organismes")
#input("We do this manually by getting each organism from the pop")
#org1 = pop.organism_list[0]
#org2 = pop.organism_list[1]
#
#org1.addGeneFull(0,1000001,1,True,-1)
#org1.addGeneFull(1,1000001,-1,True,-1)
#
#org2.addGeneFull(1,1000001,1,True,-1)
#org2.addGeneFull(2,1000001,-1,True,-1)
#
#input("Org1 = ")
#org1.printGenome()
#
#
#input("Org2 = ")
#org2.printGenome()
#    
#input("Population = ")
#pop.printOrganismList()
#
#input("Okay, now we are sure the changes are accounted for by the population")
#input("Now, lets update the innovation")
#input("Two genes are considered different if they connect different nodes.")
#input("The weight or the fact a gene is enable or not does not matter")
#input("Each gene will now recieve a unique innovation number")
#input("Only identical genes will have the same innovation")
#input("Let's proceed:")
#
#for org in pop.organism_list:
#    pop.computeInnovation(org)
#
#pop.printOrganismList()
#
#input("The results are stocked in a list of mutations:")
#pop.printMutationList()
#
#input("Let's set species")
#pop.splitPopulationInSpecies()
#pop.printOrganismInSpecies()
#
#input("Note that no organism are left in the population, they all have been dispatched in species")
#pop.printOrganismList()
#
#input("Okay now we are working on the species")
#input("Let's compute the avg fitness")
#spec = pop.species_list[0]
#spec.computeAvgFitness()
#print(spec.avg_fitness)
#
#input("Let's set the fitness of our two org and compute the avg fitness again")
#org1.fitness = 10
#org2.fitness = 10
#spec.computeAvgFitness()
#print(spec.avg_fitness)
#
#
#input("Now let's kill the 'bad' half of the species population")
#input("Before")
#spec.printOrganismList()
#
#input("After")
#spec.keepOnlyTheBestHalf()
#spec.printOrganismList()
#
#print("Note that the orgs are sorted from worst to best regarding fitness")




input("Okay now we are going to make babies :3 ")

pop = Pop.NEATPopulation(10,2,1)
pop.initializePopulation()
org1 = pop.organism_list[0]
org2 = pop.organism_list[1]
org1.addGeneFull(0,1000001,1,True,-1)
org1.addGeneFull(1,1000001,-1,True,-1)
org2.addGeneFull(1,1000001,1,True,-1)
org2.addGeneFull(2,1000001,-1,True,-1)
for org in pop.organism_list:
    pop.computeInnovation(org)
pop.splitPopulationInSpecies()
spec = pop.species_list[0]
spec.computeAvgFitness()
org1.fitness = 10
org2.fitness = 9
spec.computeAvgFitness()
#spec.keepOnlyTheBestHalf()

#input("Let's make a baby between org1 and himself?")
#input("Reminder:")
#org1.printNodes()
#print('---------')
#org1.printGenomeFull()
#
#input("The result:")
#org11 = spec.crossover(org1,org1)
#
#org11.printNodes()
#print('---------')
#org11.printGenomeFull()
#
#input("As expected, they are the same!")
#
#input("Same thing with org2!")
#input("Reminder:")
#org1.printNodes()
#print('---------')
#org2.printGenomeFull()
#
#input("The result:")
#org22 = spec.crossover(org2,org2)
#
#org22.printNodes()
#print('---------')
#org22.printGenomeFull()
#
#input("As expected, they are the same!")
#
#input("Now org1 and org2!")
#input("As org1 is more fit than org2, the 2 -> 10000001 connexion should be lost")
#input("But the 1->10000001 should stay")
#
#input("Reminder:")
#print("Org1")
#org1.printNodes()
#print('---------')
#org1.printGenomeFull()
#print("Org2")
#org2.printNodes()
#print('---------')
#org2.printGenomeFull()
#input("The result:")
#org12 = spec.crossover(org1,org2)
#
#org12.printNodes()
#print('---------')
#org12.printGenomeFull()
#
#input("As expected ! Note that the weight for the second gene can be either -1 or 1")
#
#input("Okay, now let's fill our species back with babies :3")
#input("Before")
#spec.printOrganismList()
#input("After")
#spec.generateNewHalf()
#
#spec.printOrganismList()
#
#input("Let's get everything back into the pop")
#pop.getPopulationInSpecies()
#
#pop.printOrganismList()
#print('#################')
#pop.printOrganismInSpecies()
#
#
#input("We mutate")
#pop.mutate()
#
#pop.printOrganismList()
#
#input("We split in species")
#pop.splitPopulationInSpecies()
#
#
#pop.printOrganismList()
#print('#################')
#pop.printOrganismInSpecies()
#
#print("Let's do all that again")
#pop.prepareSpeciesForNewGen()
#pop.printOrganismList()
#print('#################')
#pop.printOrganismInSpecies()
#print()
#print()
#print()
#pop.getPopulationInSpecies()
#pop.printOrganismList()
#print('#################')
#pop.printOrganismInSpecies()
#print()
#print()
#print()

