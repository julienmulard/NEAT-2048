# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:54:13 2017

@author: Julien
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:57:29 2017

@author: Julien
"""

import NEATOrganism as Org
print('addGeneFull Test:')
org = Org.NEATOrganism(2,2)

print('Creation of gene 0: 1 -> 2, w = 3, enable')
input()
org.addGeneFull(1,2,3,True,0)
org.printGenomeFull()
print()
print('Creation of gene 10: 3 -> 4, w = 5, not enable')
input()
org.addGeneFull(3,4,5,False,10)
org.printGenomeFull()

print('checkIfGeneExistsFromIndex test')
input()
org = Org.NEATOrganism(0,1)
org.initializeNodes()
print('Creation of gene 0: 1 -> 2, w = 3, enable')
org.addGeneFull(1,2,3,True,0)
print('Creation of gene 10: 3 -> 4, w = 5, not enable')
org.addGeneFull(3,4,5,False,10)
print()
print('Check if gene 1 -> 2 exists: (True)')
input()
a = org.checkIfGeneExistsFromIndex(1,2)
print(a)
print('Check if gene 1 -> 3 exists: (False)')
input()
a = org.checkIfGeneExistsFromIndex(1,3)
print(a)
print('Check if gene 2 -> 4 exists: (False)')
input()
a = org.checkIfGeneExistsFromIndex(2,4)
print(a)
print('Check if gene 3 -> 4 exists: (True)')
input()
a = org.checkIfGeneExistsFromIndex(3,4)
print(a)

print('checkIfGeneExistsFromNode test')
input()
org = Org.NEATOrganism(0,1)
org.initializeNodes()
print('Creation of gene 0: 1 -> 2, w = 3, enable')
org.addGeneFull(1,2,3,True,0)
print('Creation of gene 10: 3 -> 4, w = 5, not enable')
org.addGeneFull(3,4,5,False,10)
nod1 = Org.Nod.NEATNode(1, "",1)
nod2 = Org.Nod.NEATNode(2, "",1)
nod3 = Org.Nod.NEATNode(3, "",1)
nod4 = Org.Nod.NEATNode(4, "",1)
print('Check if gene 1 -> 2 exists: (True)')
input()
a = org.checkIfGeneExistsFromNode(nod1, nod2)
print(a)
print('Check if gene 1 -> 3 exists: (False)')
input()
a = org.checkIfGeneExistsFromNode(nod1,nod3)
print(a)
print('Check if gene 2 -> 4 exists: (False)')
input()
a = org.checkIfGeneExistsFromNode(nod2,nod4)
print(a)
print('Check if gene 3 -> 4 exists: (True)')
input()
a = org.checkIfGeneExistsFromNode(nod3,nod4)
print(a)

print('Test Random Generation 1')
input()
org = Org.NEATOrganism(10,10)
org.initializeNodes()
print('Init organism has 10 inputs, and 10 outputs, no genes')
print('We create 20 random genes (might generate less, as trying to generate an existing gene abort the generation)')
print('Input nodes should be only inputs, i.e. index in [0,10]')
print('Output nodes should be only outputs, i.e. index in [1000001,1000010]')
print('No duplicate')
input()

for i in range(20):
    org.addRandomGene()
org.printGenomeFull()
print()

print('Sort genome by input, and print simplified genome:')
input()
org.sortGenomeByInput()
org.printGenome()
print()

print('Sort genome by output and print simplified genome:')
input()

org.sortGenomeByOutput()
org.printGenome()

print()
print('Test Random Generation 2')
input()
print('Same init org (10 ins, 10 outs)')
print('First we add 10 hidden nodes:')

org = Org.NEATOrganism(10,10)
org.initializeNodes()
for i in range(10):
    org.addHiddenNode(1)
    
org.sortNodeListByIndex()
org.printNodes()
print()
input()

print('Now we generate 60 random genes')
print('Inputs should be input nodes or hidden nodes [0:20]')
print('Outputs should be hidden nodes or output nodes [11:20] and [1000000:1000010]')
print('Still no duplicate')
input()
for i in range(60):
    org.addRandomGene()
org.printGenomeFull()
print()

print('Sort genome by input, and print simplified genome:')
input()
org.sortGenomeByInput()
org.printGenome()
print()

print('Sort genome by output, and print simplified genome:')
input()
org.sortGenomeByOutput()
org.printGenome()

print()
print("getRandomGene Test")
input()
org = Org.NEATOrganism(10,10)
org.initializeNodes()
print('Creation of gene 0: 0 -> 1, w = 2, enable')
org.addGeneFull(0,1,2,True,0)
print('Creation of gene 1: 1 -> 2, w = 3, enable')
org.addGeneFull(1,2,3,True,1)
print('Creation of gene 2: 2 -> 3, w = 4, not enable')
org.addGeneFull(2,3,4,False,2)
print('Creation of gene 3: 3 -> 4, w = 5, not enable')
org.addGeneFull(3,4,5,False,3)
input()
org.printGenomeFull()

print('Get a random gene 50 times')
print('Should get all the genes, without crashing')
input()
for i in range(50):
    org.getRandomGene().printGene()
print()


print("AddNodeInGene Test")
input()
org = Org.NEATOrganism(1,1)
org.initializeNodes()
org.addGeneFull(1,1000001,2,True,0)
print("Init organism genome and nodes:")
input()
org.sortGenomeByInput()
org.printGenomeFull()
print()
org.sortNodeListByIndex()
org.printNodes()
print()

print("Add a node in the first gene:")
print("Should create 2 new genes and deactivate the old gene")
print("The 1st new gene is from the old gene input to the new node")
print("Its weight should be 1")
print("The 2nd gene should link the new node to the old gene's output")
print("Its weight should the same as the old gene")
print("No sorting, so the new genes must be the last ones")
input()
org.addNodeInGene(org.genome[0])

org.printGenomeFull()
print()

org.printNodes()
print()

print("Add another node in the first gene:")
print("Same behaviour expected, except the old gene is already deactivated")
print("Note that for the algorithm, addNodeInGene sort the nodes list!")
print("So only the new node shall be listed after the outputs")
input()
org.addNodeInGene(org.genome[0])

org.printGenomeFull()
print()

org.printNodes()
print()

print("Add a node in the second gene:")
print("You know what to expect")
input()
org.addNodeInGene(org.genome[1])

org.printGenome()
print()

org.printNodes()
print()

print("Innovation at gene level")
input()
print("By default in all the functions that create a new gene, innovation is set to -1")
print("It's so to serve as a marker to quickly find a new genetic mutation!")
print("The innovation represents the historical evolution of the genome")
print("Innovation as a concept is handled by the population class, so we'll just test things mecanically")
print("Let's start with a new organism, with 2 ins, 2 outs, everything connected:")
input()
org = Org.NEATOrganism(2,2)
org.initializeNodes()
org.addGeneFull(0,1000000,1,True,4)
org.addGeneFull(0,1000001,1,True,1)

org.addGeneFull(1,1000000,1,True,0)
org.addGeneFull(1,1000001,1,True,2)

org.addGeneFull(2,1000000,1,True,-1)
org.addGeneFull(2,1000001,1,True,3)

org.sortGenomeByInput()
org.printGenome()

print("Now sorting by innovation")
input()
org.sortGenomeByInnovation()
org.printGenome()
print("getFirstGeneWithInnovationToupdate Test")
print("Okay, so if a gene inno is -1;, it has to be updates")
print("The next fonction gets you a gene with such an innovation")
print("Or output None")
print("Let's try on our last org")
input()
gene = org.getFirstGeneWithInnovationToUpdate()
gene.printGeneFull()

print("And if we modify the gene, it appears in the org:")
input()
gene.input_node = 256
org.printGenome()
print()

input()
print("Okay, let's try on a big org with a lot to find.")
print("We update each gene with an incrementing innovation")
print("First, the organism with 10 ins, 10 outs, 10 hidden and 60 rand genes.")
print("All innovations should be -1")
org = Org.NEATOrganism(10,10)
org.initializeNodes()
for i in range(10):
    org.addHiddenNode('1')

for i in range(60):
    org.addRandomGene()
    
org.sortGenomeByInput()
org.printGenome()
print()
print("Let's update everything (sorta)!")
print("If it's getting stuck here, it's because it's a while loop.")
print("So it means something went wrong")
input()

gene = org.getFirstGeneWithInnovationToUpdate()
inno = 0
while gene != None:
    gene.innovation = inno
    inno += 1
    gene = org.getFirstGeneWithInnovationToUpdate()

print("The result")
org.sortGenomeByInput()
org.printGenome()

input()
print("Sorted by innovation")
org.sortGenomeByInnovation()
org.printGenome()

org = Org.NEATOrganism(2,2)
org.initializeNodes()
org.initializeGenome()
org.printGenome()
org.printNodes()
org.drawOrganism()

