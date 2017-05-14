# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:30:13 2017

@author: Julien
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 07:52:57 2017

@author: Julien Mulard
"""

from pylab import rand, ceil
from math import log

class LearningGameboard:
    
    def __init__ (self):
        
        #self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        #self.mem_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];
        self.mem_board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];
        self.learning_board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0];
        self.empty_tile_list = []        
        self.two_generation_proba = 0.75
        self.score = 0
        self.hasWin = False
        self.hasLoose = False
        self.isRunning = True
    
    def computeLearningBoard(self):

        _1_log_board_max = 1/log(max(self.board),2)              
        
        for i in range (16):
            self.learning_board[i] = log(self.board[i],2) * _1_log_board_max
    
    def insertTile (self):
        
        self.findAllEmptyTiles()        
        
        if self.empty_tile_list != []:       
        
            random_tile_number=[]
            for tile in self.empty_tile_list:
                random_tile_number.append(rand())
            
            inserted_tile_index = self.empty_tile_list[random_tile_number.index(max(random_tile_number))]
            
            if rand()<=self.two_generation_proba:
                self.board[inserted_tile_index] = 2
            else:
                self.board[inserted_tile_index] = 4
            
            return True
        
        else:
            self.hasLoose = True
            return False
        
    def findAllEmptyTiles(self):
                
        self.empty_tile_list = []             
        for i in range(0,16):
            if self.board[i] == 0:
                self.empty_tile_list.append(i);
                
        
    def showBoard(self):
        for line in range(0,4):
            for col in range(0,4):
                print(self.board[line*4+col], end=" ")
            print("\n")
            
    def showLearningBoard(self):
        for line in range(0,4):
            for col in range(0,4):
                print(self.learning_board[line*4+col], end=" ")
            print("\n")
    
    def showBoardFancy(self):
        total_space = 6
        print('_____________________________')
        for line in range(0,4):
            print('|      |      |      |      |')
            print('', end='|')
            for col in range(0,4):
                val_string = str(self.board[line*4+col])
                num_white_space = total_space-len(val_string)
                
                output_string = ""
                for i in range (0,int(num_white_space/2)):
                    output_string += ' '
                output_string += val_string
                for i in range(0,int(ceil(num_white_space/2))):
                    output_string += ' '
                    
                print(output_string, end="|")
                
            print()
            print('|______|______|______|______|')
            
            
    def showBoardFancyColor(self):
        total_space = 6
        print('_____________________________')
        end_color_str = '\x1b[0m'
        for line in range(0,4):
            for subline in range (0,3):
#                print('|      |      |      |      |')
#                print('', end='|')
                print('', end='|')
                for col in range(0,4):                  
                    tile_value = self.board[line*4+col]
                    color_str = self.setFormatingStringGivenTileValue(tile_value)
                    
                    if subline != 2:
                        fill_char = ' '
                    else:
                        fill_char = '_'                    
                    
                    if tile_value !=0 and subline == 1:
                        val_string = str(tile_value)
                    else:
                        val_string = fill_char
                    num_white_space = total_space-len(val_string)
                    
                    
                    
                    
                    output_string = ""
                    for i in range (0,int(num_white_space/2)):
                        output_string += fill_char
                    output_string += val_string
                    for i in range(0,int(ceil(num_white_space/2))):
                        output_string += fill_char
                        
                    print(color_str+output_string+end_color_str, end="|")
                
                print()
#            print('|______|______|______|______|')
            
    def setFormatingStringGivenTileValue(self, tile):
        if (tile == 0):
                color_str = '\x1b[1;30;48m'
        elif (tile == 2):
            color_str = '\x1b[5;48m'
        elif (tile == 4):            
            color_str = '\x1b[5;41m'
        elif (tile == 8):            
            color_str = '\x1b[5;42m'
        elif (tile == 16):
            color_str = '\x1b[5;43m'
        elif (tile == 32):            
            color_str = '\x1b[5;44m'
        elif (tile == 64):
            color_str = '\x1b[5;45m'
        elif (tile == 128):
            color_str = '\x1b[5;46m'
        elif (tile == 256):            
            color_str = '\x1b[5;47m'
        elif (tile == 512):
            color_str = '\x1b[5;31m'
        elif (tile == 1024):
            color_str = '\x1b[5;32m'
        elif (tile == 2048):            
            color_str = '\x1b[5;33m'
        return color_str
            
    def moveLeft(self):
        
        for line_number in range(0,4):
            zero_stripped_line = self.getZeroStrippedLine(line_number)
            
            line = self.resolveLineOrCol(zero_stripped_line)
                
            for i in range (0,4):
                self.board[line_number*4+i] = line[i]
    
    def moveRight(self):
         for line_number in range(0,4):
            zero_stripped_line = list(reversed(self.getZeroStrippedLine(line_number)))
            
            line = list(reversed(self.resolveLineOrCol(zero_stripped_line)))
                
            for i in range (0,4):
                self.board[line_number*4+i] = line[i]       
        
    def moveUp(self):
        for col_number in range(0,4):
            zero_stripped_col = self.getZeroStrippedCol(col_number)
            
            col = self.resolveLineOrCol(zero_stripped_col)
            
            for i in range(0,4):
                self.board[i*4+col_number] = col[i]

    def moveDown(self):
        for col_number in range(0,4):
            zero_stripped_col = list(reversed(self.getZeroStrippedCol(col_number)))
            
            col = list(reversed(self.resolveLineOrCol(zero_stripped_col)))
            
            for i in range(0,4):
                self.board[i*4+col_number] = col[i]
    
    def getZeroStrippedLine (self, line_number):
        
        zero_stripped_line = []
        line = self.board[line_number*4:line_number*4+4]
        for tile in line:
            if tile !=0:
                zero_stripped_line.append(tile)
        return zero_stripped_line
        
    def getZeroStrippedCol (self, col_number):
        
        zero_stripped_col = []
        col = self.board[col_number:16:4]
        for tile in col:
            if tile !=0:
                zero_stripped_col.append(tile)
        return zero_stripped_col
    
    def resolveLineOrCol(self, array):
        for i in range(0,len(array)-1):        
            if array[i] == array[i+1]:
                array[i] = array[i]+array[i+1]
                array[i+1] = 0;
                self.score += array[i]
                if array[i] == 2048:
                    self.hasWin = True
        
        line_or_col = []
        for tile in array:
            if tile != 0:
                line_or_col.append(tile)
        
        for i in range(len(line_or_col),4):
            line_or_col.append(0)
        
        return line_or_col
        
    def showScore(self):
        print("Score: " + str(self.score))
        
    def memoriseBoard(self):
        for i in range (0,16):
            self.mem_board[i] = self.board[i]
    
    def checkIfAnythingChanged(self):
        diff_board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]        
        for i in range (0,16):
            diff_board[i] = self.board[i] - self.mem_board[i]
            
        if min(diff_board) != 0 or max (diff_board) != 0:
            return True
        else:
            return False
    
    def checkIfWinOrLoose(self):

        self.findAllEmptyTiles()
        
        if  self.empty_tile_list == []:
            self.hasLoose = True
        
        if self.hasLoose == True:
#            print("\n~~~~~~~~~ Game Over ~~~~~~~~~")
            self.isRunning = False;
            return True
        elif self.hasWin == True:
            print("\n~~~~~~~~~ Well Done ~~~~~~~~~")
            self.isRunning = False
            return True
        else:
            return False