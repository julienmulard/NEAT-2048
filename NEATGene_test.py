# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:38:33 2017

@author: Julien
"""

import NEATGene as Gen

#Test init and print
print('Test init and print:')
print()
gen = Gen.NEATGene(1,2,0.5,True,0)
print('gen.PrintGene():')
gen.printGene()
print()
print('gen.PrintGeneFull()')
gen.printGeneFull()
print()
gen = Gen.NEATGene(2,3,20,False,1)
print('gen.PrintGene():')
gen.printGene()
print()
print('gen.PrintGeneFull()')
gen.printGeneFull()
print()

#Test copy
print('Test copy')
gen1 = Gen.NEATGene(1,2,3,True,0)
gen2 = gen1
print('gen1:')
gen1.printGeneFull()
print('gen2 = gen1:')
gen2 = gen1
gen2.printGeneFull()
print('if gen1/2 is modified, is gen2/1 too?')
print('gen1.weight = 4 -> gen1:')
gen1.weight = 4
gen1.printGeneFull()
print('gen2:')
gen2.printGeneFull()
print('Yes...')
print('gen2.input_node = 0 -> gen2:')
gen2.input_node = 0
gen2.printGeneFull()
print('gen1:')
gen1.printGeneFull()
print()
print('Now with copy: gen2 = gen1.copyGene()')
gen2 = gen1.copyGene()
print('gen1:')
gen1.printGeneFull()
print('gen2:')
gen2.printGeneFull()
print('gen1.output_node = 10 -> gen1:')
gen1.output_node = 10
gen1.printGeneFull()
print('gen2:')
gen2.printGeneFull()

#Test weight mutation
print("Test mutation")
gen1 = Gen.NEATGene(1,2,0,True,0)
print("Init weight = 0")
print("Proba shuffle = 0")
print("Weight should only move max +/-0.1 each time")
print("Let's try 60 times!")
input()
old_weight = 0
for i in range(60):
    old_weight = gen1.weight    
    gen1.mutateWeight(0)
    delta = gen1.weight - old_weight
    print(str(old_weight) +' -> ' + str(gen1.weight))
    print('Delta = ' + str(delta))
    if abs(delta) > 0.1:
        print('Delta out of expected range!')
input()
gen1 = Gen.NEATGene(1,2,0,True,0)
print("Init weight = 0")
print("Proba shuffle = 1")
print("Weight should be random each time, in range [-2:2]")
print("Let's try 60 times!")
input()
old_weight = 0
for i in range(60):
    old_weight = gen1.weight    
    gen1.mutateWeight(1)
    print(gen1.weight)
    if abs(gen1.weight)>2:
        print('Weight out of expected range')
input()
gen1 = Gen.NEATGene(1,2,0,True,0)
print("Init weight = 0")
print("Proba shuffle = 0.1")
print("Weight should only move max +/-0.1 most time")
print("We'll count when it's not (should be around 100)")
print("Note that their might be more shuffle")
print("But the new random weight can be close enough to the old weight not to be detected")
print("Let's try 1000 times!")
input()
old_weight = 0
num_shuffle = 0
for i in range(1000):
    old_weight = gen1.weight    
    gen1.mutateWeight(0.1)
    delta = gen1.weight - old_weight
#    print(str(old_weight) +' -> ' + str(gen1.weight))
#    print('Delta = ' + str(delta))
   
    
    if abs(delta) > 0.1:
        print('Shuffle detected')
        num_shuffle += 1
print()
print('Num shuffle detected = '+str(num_shuffle))
input()