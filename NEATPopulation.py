# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:14:51 2017

@author: Julien
"""

import NEATOrganism as Org
import NEATMutation as Mut
import NEATSpecies as Spe

class NEATPopulation:
    
    def __init__(self,num_organism, num_input, num_output):
        
        self.num_organism = num_organism
        self.organism_list = []

        self.num_input = num_input
        self.num_output = num_output        
        
        self.species_index = 0
        self.species_list = []
        self.max_gen_dist = 10
        
        self.mutation_index = 0        
        self.mutation_list = []

        self.weight_mutate_proba = 0.8
        self.weight_shuffle_proba = 0.1
        self.add_node_proba = 0.2
        self.add_gene_proba = 0.2
    
    def initializePopulation(self):
        
        for i in range(self.num_organism):
            self.addNewOrganism()
            
        return
    
    def addNewOrganism(self):
        
        org = Org.NEATOrganism(self.num_input, self.num_output)
        org.initializeNodes() 
        org.initializeGenome()
        
        self.organism_list.append(org)
        
    def mutate(self):
        
        for org in self.organism_list:
            org.mutate(self.weight_mutate_proba, self.weight_shuffle_proba, self.add_gene_proba, self.add_node_proba)
            self.computeInnovation(org)
        

#-----------------Innovation--------------------#
    def computeInnovation(self, org):

        for gene in org.genome:
            if gene.innovation == -1:
                self.computeGeneInnovation(gene)
                
        
    def computeGeneInnovation(self, gene):
        
        gene_exists = False        
        
        if self.mutation_list != []:        
            for mut in self.mutation_list:
                if gene.input_node == mut.input_node and gene.output_node == mut.output_node:
                    gene.innovation = mut.innovation
                    gene_exists = True
                    break
            
            if gene_exists == False:   
                gene.innovation = self.mutation_index
                self.addMutationFromGene(gene)
        else:
            gene.innovation = self.mutation_index
            self.addMutationFromGene(gene)
            

    def addMutationFromGene(self, gene):

        mut = Mut.NEATMutation(gene.input_node, gene.output_node, gene.innovation)
        
        self.mutation_index += 1
        self.mutation_list.append(mut)
        
    def clearMutationList(self):
        
        for i in range (len(self.mutation_list)):
            self.mutation_list.pop(0)
    
#-------------Species------------#
    
    def killAllPopulation(self):
        for i in range(len(self.organism_list)):
            self.organism_list.pop(0)          
    
    def manageSpecies(self):
    
        for org in self.organism_list:
            if self.species_list == []: 
               self.addNewSpecies(org)
            else:
                isAssignedToSpecies = False
                #self.sortSpeciesListByIndexReverse()
                for species in self.species_list:
                    orgBelongsToSpecies = species.checkIfOrganismBelongsToSpecies(org)
                    if orgBelongsToSpecies == True:
                        species.addOrganism(org)
                        isAssignedToSpecies = True
                        break
                
                if isAssignedToSpecies == False:
                    self.addNewSpecies(org)
                    
                    
    
    
    def splitPopulationInSpecies(self):
        self.manageSpecies()
        self.killAllPopulation()
            
    def addNewSpecies(self, rep):
        
        new_species = Spe.NEATSpecies(rep, self.max_gen_dist, self.species_index)            
        self.species_list.append(new_species)
        self.species_index += 1
     
    def printSpeciesList(self):
        
        for species in self.species_list:
            species.printSpecies()
        
    def prepareSpeciesForNewGen(self):
        for species in self.species_list:
            species.prepareForNewGeneration()
            
    def sortSpeciesListByIndex(self):
        self.species_list.sort(key = lambda spe: spe.index)
        
    def sortSpeciesListByIndexReverse(self):
        self.species_list.sort(key = lambda spe: spe.index, reverse = True)

            
    def getPopulationInSpecies(self):
        for spec in self.species_list:
            for org in spec.organism_list:
                self.organism_list.append(org)
            spec.clearSpecies()
        
    def printOrganismList(self):
        for org in self.organism_list:
            org.printGenome()
            print('-------')
            
    def printOrganismInSpecies(self):
        for spec in self.species_list:
            spec.printSpecies()
            spec.printOrganismList()
            
    def printMutationList(self):
        for mut in self.mutation_list:
            mut.printMutation()
            
    def createNewGeneration(self):
        self.prepareSpeciesForNewGen()
        self.getPopulationInSpecies()        
        self.mutate()
        self.splitPopulationInSpecies()


    def createNewGenerationV2(self):
    
    
        for spec in self.species_list:
            if spec.checkIfStale():
                if len(self.species_list) > 1:
                    self.species_list.remove(spec)
                    print(spec.name + ' is stale!')    
    
        total_avg_fitness = self.computeTotalAvgFitness()

        self.splitOffspringsInSpecies(total_avg_fitness)
        
        for spec in self.species_list:
            spec.keepOnlyTheBestHalf()
            spec.setRandomRep()
        
        self.generateNewPopulation()
        
        for spec in self.species_list:
            spec.clearSpecies()
        
        self.mutate()        
        
        self.splitPopulationInSpeciesV2()
        
        
        
                
    def computeTotalAvgFitness(self):
        
        total_avg_fitness = 0        
        for spec in self.species_list:
            spec.updateFitnessMaxAndAvg()
            total_avg_fitness += spec.avg_fitness
        
        return total_avg_fitness
        
    def splitOffspringsInSpecies(self, total_avg_fitness):
        
        num_total_offspring = 0           
        for spec in self.species_list:
            if total_avg_fitness == 0:
                spec.num_offspring = 0
            else:
                spec.num_offspring = int(spec.avg_fitness/total_avg_fitness*self.num_organism)
            num_total_offspring += spec.num_offspring
        
        remainder = self.num_organism-num_total_offspring
        
        if remainder < 0:
            input("C'est la merde!!!!")
        else:
            for spec in self.species_list:
                spec.num_offspring += 1
                remainder -= 1
                if remainder <= 0:
                    break
    
    def generateNewPopulation(self):
        
        for spec in self.species_list:
            spec.buildParentProbaList()
            if len(spec.parent_proba_list) > 0:
                for i in range(spec.num_offspring):
                    new_org = spec.generateNewOrgV2()                
                    self.organism_list.append(new_org)
                
    
    def manageSpeciesV2(self):
        for org in self.organism_list:
            if self.species_list == []: 
               self.addNewSpecies(org)
            else:
                isAssignedToSpecies = self.assigneToClosestSpecies(org)
                #self.sortSpeciesListByIndexReverse()
                
                if isAssignedToSpecies == False:
                    self.addNewSpecies(org)
                    
    def assigneToClosestSpecies(self, org):
        min_dist = self.max_gen_dist
        species_index = 0
        isAssigned = False
        for i in range(len(self.species_list)):
            species = self.species_list[i]
            dist = species.rep.computeGeneticDistance(org)
            if dist < min_dist:
                min_dist = dist
                species_index = i
                isAssigned = True
        
        if isAssigned == True:
            self.species_list[species_index].addOrganism(org)
        
        return isAssigned            
            
    def splitPopulationInSpeciesV2(self):
        self.manageSpeciesV2()
        self.killAllPopulation()
        
    
