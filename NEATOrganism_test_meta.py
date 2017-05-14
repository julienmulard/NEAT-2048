# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:54:36 2017

@author: Julien
"""

import NEATOrganism as Org

print("Test of the more global or high-level function of the NEATOrganism class")
input()

print("Mutate function test")
input()

print("Organism is 10 ins, 10 outs, no genes yet")
org = Org.NEATOrganism(10,10)
org.initializeNodes()
org.printGenome()

print("Reminder: probas = weight_mut, weight_shuffle, add_gene, add_node")
print("Let's mutate 10 times by adding genes! proba = 0, 0, 1, 0")
print("Note: Less than 10 genes can be expected, as any duplicate generation will be aborted")
input()
for i in range (10):
    org.mutate(0, 0, 1, 0)

org.printGenome()

print("Okay, now for some node stuff")
input()
for i  in range(10):
    org.mutate(0 , 0 , 0 , 1)

org.printGenome()
print()

print("For the weights mutations")
org = Org.NEATOrganism(1,1)
org.initializeNodes()
org.addGeneFull(0,1000001,1,True,0)
org.addGeneFull(1,1000001,1,True,1)
print("The organism:")
input()
org.printGenomeFull()

print("After 1 mutation with proba = 1,0,0,0")
input()
org.mutate(1,0,0,0)

org.printGenomeFull()
input()

print("After 1 mutation with proba = 1,1,0,0")
input()
org.mutate(1,1,0,0)

org.printGenomeFull()
input()

print("Now let's mutate in real conditions!")
print("With a new organism 10x10:")
org = Org.NEATOrganism(10,10)
org.initializeNodes()
org.printGenome()

print("Lets mutate 10 times!")
print("proba = 0.8, 0.1, 0.2, 0.2")
for i in range(10):
    org.mutate(0.8,0.1,0.2,0.2)
    org.printGenomeFull()
    print()
    input()
    
    
