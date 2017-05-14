# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:18:51 2017

@author: Julien
"""
import random
import NEATOrganism as Org

class NEATSpecies:
    
    def __init__(self, rep, max_genetic_distance, species_index):
        
        self.num_organism = 1
        self.organism_list = [rep]
        self.num_killed = 0
        
        self.rep = rep.copyOrganism()
        
        self.max_genetic_distance = max_genetic_distance
        
        self.name = self.generateSpeciesName()
        
        self.index = species_index
        
        self.avg_fitness = 0
        self.gen_max_fitness = 0
        self.overall_max_fitness = 0
        
        self.isStale = False
        self.stale_count = 0
        self.stale_count_max = 30
        
        self.num_offspring = 0
        
        self.parent_proba_list = []
        
    def addOrganism(self, org):
        
        self.organism_list.append(org)
        self.num_organism += 1
        
    def checkIfOrganismBelongsToSpecies(self, org):
        
        if self.rep.computeGeneticDistance(org) < self.max_genetic_distance:
            return True
        
        else:
            return False
    
    
    
    def generateSpeciesName(self):
        
        vowels = ['a','e','i','o','u','y',
        'an','en','in','on','un','yn',
        'ai','ei','oi','ui',
        'ae','oe','ue',
        'au','eu','iu','ou',
        'ay','oy']
        
        consonnants = ['b','c','d','f','g','h','j','k','l','m','p','qu','r','s','t','v','w','x','z',]
        
        name = ''
        for i in range(int(random.random()*4)+1):
            name += consonnants[int(random.random()*len(consonnants))]
            name += vowels[int(random.random()*len(vowels))]
            
        name += ' '
                
        for i in range(int(random.random()*4)+1):
            name += consonnants[int(random.random()*len(consonnants))]
            name += vowels[int(random.random()*len(vowels))]
            
        return name
    
    def printSpecies(self):
        
        print(str(self.index) +': ' +self.name+': '+str(self.num_organism))
        
    def drawSpecies(self):
        
        self.printSpecies
        self.rep.drawOrganism()
        
    def clearSpecies(self):
        for i in range(self.num_organism):
            self.organism_list.pop(0)
            
        self.num_organism = 0
        self.num_killed = 0
        
    def setRandomRep(self):
        if self.num_organism != 0:
            rand_index = int(random.random()*self.num_organism)
            self.setRep(self.organism_list[rand_index])
    
    
    def setRep(self, org):
        self.rep = org.copyOrganism()
    
    def prepareForNewGeneration(self):
        self.keepOnlyTheBestHalf()        
        self.setRandomRep()
#        self.clearSpecies()
        self.generateNewHalf()
    
    def prepareForNewGenerationV2(self):
        self.updateFitnessMaxAndAvg()
      
    def sortOrganismListByFitness(self):
        self.organism_list.sort(key = lambda org: org.fitness)
        
    def keepOnlyTheBestHalf(self):
        self.sortOrganismListByFitness()
        for i in range(int(self.num_organism/2)):
            self.organism_list.pop(0)
            self.num_killed += 1
            
        self.num_organism -= self.num_killed
    
    def generateNewHalf(self):
        
        for i in range(self.num_killed):
            rand_org1 = self.organism_list[int(random.random()*self.num_organism)]
            rand_org2 = self.organism_list[int(random.random()*self.num_organism)]
            
            self.addThroughCrossover(rand_org1, rand_org2)
        
        self.num_killed = 0
        return

    def addThroughCrossover(self, parent1, parent2):
        
        if parent1.fitness < parent2.fitness:
            par1 = parent2
            par2 = parent1
        else:
            par1 = parent1
            par2 = parent2
        
        new_org = self.crossover(par1, par2)
        
        self.addOrganism(new_org)
        
    def crossover(self, parent1, parent2):
        
        new_org = Org.NEATOrganism(parent1.num_input, parent1.num_output)
        new_org.initializeNodes()
        
        for gene1 in parent1.genome:
            isFoundInGene2 = False
            for gene2 in parent2.genome:
                if gene1.innovation == gene2.innovation:
                    if random.random() < 0.5:
                        new_org.addGeneFromParent(gene1, parent1)
                    else:
                        new_org.addGeneFromParent(gene2, parent2)
                    isFoundInGene2 = True
            
            if isFoundInGene2 == False:
                new_org.addGeneFromParent(gene1, parent1)
                
        return new_org
            
    def printOrganismList(self):
        for org in self.organism_list:
            org.sortGenomeByInnovation()
            org.printGenome()
            print('-------')
    
    def updateFitnessMaxAndAvg(self):
        self.computeAvgFitness()
        self.computeMaxFitness()
    
    def computeAvgFitness(self):

        sum_fitness = 0

        for org in self.organism_list:
            sum_fitness += org.fitness
         
        if len(self.organism_list) != 0: 
            self.avg_fitness = sum_fitness/len(self.organism_list)
        else:
            self.avg_fitness = 0
        
    def computeMaxFitness(self):
        
        max_fitness = 0
        
        for org in self.organism_list:
            if org.fitness > max_fitness:
                max_fitness = org.fitness
            
        self.gen_max_fitness = max_fitness
        
        if max_fitness > self.overall_max_fitness:
            self.overall_max_fitness = max_fitness
            self.stale_count = 0
            
        else:
            self.stale_count += 1
            
    def checkIfStale(self):
        if self.stale_count < self.stale_count_max:
            self.isStale = False
        else:
            self.isStale = True
        
        return self.isStale
        
    def generateNewOrg(self):
        
        parent1 = self.organism_list[int(random.random()*len(self.organism_list))]
        parent2 = self.organism_list[int(random.random()*len(self.organism_list))]
            
        if parent1.fitness < parent2.fitness:
            par1 = parent2
            par2 = parent1
        else:
            par1 = parent1
            par2 = parent2
        
        new_org = self.crossover(par1, par2)
        
        return new_org
        
    def generateNewOrgV2(self):
        
                
        parent1 = self.parent_proba_list[int(random.random()*len(self.parent_proba_list))]
        parent2 = self.parent_proba_list[int(random.random()*len(self.parent_proba_list))]
            
        if parent1.fitness < parent2.fitness:
            par1 = parent2
            par2 = parent1
        else:
            par1 = parent1
            par2 = parent2
        
        new_org = self.crossover(par1, par2)
        
        return new_org
        
    def buildParentProbaList(self):
        self.parent_proba_list.clear()
        
        n = len(self.organism_list)
        
        
        self.organism_list.sort(key = lambda org: org.fitness, reverse = True)
        
        for i in range(n):
            for j in range(i):
                self.parent_proba_list.append(self.organism_list[i])
                
        self.organism_list.sort(key = lambda org: org.fitness)