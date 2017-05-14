# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:53:28 2017

@author: Julien
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:10:48 2017

@author: Julien
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:31:39 2017

@author: Julien
"""

import NEATPopulation as Pop
import LearningGameboard as Gb
#import sys

pop = Pop.NEATPopulation(150,16,4)
pop.initializePopulation()
pop.mutate()
pop.splitPopulationInSpecies()
pop.clearMutationList()
org1 = ""
best_score_list = []
for gen in range(1000):
    print('-----------------GEN '+str(gen)+'-----------------')
    for spec in pop.species_list:
#        print(spec.name)
        for org in spec.organism_list:
    
            gb = Gb.LearningGameboard()    
            hasMove = False
            
            gb.insertTile()
            gb.insertTile()
            
            num_turn_stuck = 0
            
            output_mem = ''
#            print('------------New Org---------------')
            while gb.checkIfWinOrLoose() == False:
#                print(hasMove)
                
                    
                output_array = org.computeOutput(gb.learning_board)
                

                output = output_array.index(max(output_array))

#                gb.showBoardFancyColor()
#                input()    
                while hasMove == False and gb.checkIfWinOrLoose() == False:            
            
                    gb.memoriseBoard()
                    if output == 0:
                        gb.moveUp()
                        gb.score += 1
    #                    print("Up")
                    elif output == 1:
                        gb.moveRight()
                        gb.score += 1
    #                    print("Down")
                    elif output == 2:        
                        gb.moveDown()
                        gb.score += 1
    #                    print("Left")
                    elif output == 3:            
                        gb.moveLeft()
                        gb.score += 1
    #                    print("Right")
                    
                    hasMove = gb.checkIfAnythingChanged()
                    
                    output += 1
                    if output == 4:
                        output = 0
                
#                gb.showBoardFancyColor()
#                input()
                hasMove = False
                gb.insertTile()
            org.fitness = gb.score
#            print()
            
   

            
    pop.createNewGenerationV2()
    pop.clearMutationList()   
    
    best_score = 0   
    
    for spec1 in pop.species_list:
        
        if spec1.gen_max_fitness > best_score:
            best_score = spec1.gen_max_fitness
        
        print(spec1.name)
        print(spec1.gen_max_fitness)
        print(spec1.avg_fitness)

    best_score_list.append(best_score)

#    