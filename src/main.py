import numpy as np
from colorama import Fore, Back, Style
import os
from src.troops import *
from src.spells import *



class Board():

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.gunda_list=[]
        
    def board_array(self):
        # self.grid= np.empty((self.row, self.column),dtype=str)
        self.grid = [[ ' ' for i in range(self.column)] for j in range(self.row)]
                
    def initialise(self):
        for i in range(self.row):
                for j in range(self.column):
                    self.grid[i][j] = Fore.GREEN + Back.GREEN + ' ' + Style.RESET_ALL
        
        for i in range(self.row):
                for j in range(self.column):
                    if(i == 0 or i == self.row - 1 or j == 0 or j == self.column - 1 ):
                       self.grid[i][j] = Fore.BLUE + '█' + Style.RESET_ALL
                       
    def change_grid(self, i, j, val):
            self.grid[i][j] = val
                                           
    def print(self):
        
        os.system('clear')
        for i in range(self.row):
            for j in range(self.column):
                # print(Back.GREEN + Fore.BLUE + self.grid[i][j] + Style.RESET_ALL, end='')
                print( self.grid[i][j] , end='')
            print()
        
    def set_cannon(self,grid,cannon_pos):
        self.cannon_list=[]
        for i in cannon_pos:
            x = i[0]
            y = i[1]
            cur_cannon = Cannon(grid,x,y)
            self.cannon_list.append(cur_cannon)

    def set_hut(self,grid,hut_pos):
        self.hut_list=[]
        for i in hut_pos:
            x = i[0]
            y = i[1]
            cur_hut = Hut(grid,x,y)
            self.hut_list.append(cur_hut)
        
    def set_wall(self,grid,wall_pos):
        self.wall_list=[]
        for i in wall_pos:
            x = i[0]
            y = i[1]
            cur_wall = Wall(grid,x,y)
            self.wall_list.append(cur_wall)
        
    def set_townhall(self,brd, x, y):
        self.th= TownHall(brd,x,y)
        
    def set_raja(self,brd, x, y):
        self.raja= King(brd,x,y)  
    
    # def set_heal(self,brd):
    #     self.heal_spell= heal(brd)

        


        
        



