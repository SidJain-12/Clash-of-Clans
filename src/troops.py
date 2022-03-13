# from turtle import update
# from click import style
from src.building import *
from colorama import Fore, Style, Back
import math
from src.game_end import * 

gend=game_end()

blank_space= Fore.GREEN + Back.GREEN + ' ' + Style.RESET_ALL

class Troops:
    def __init__(self, xcord, ycord, length, width,health):
        self.type="Troops"
        self.length=length
        self.width=width
        self.xcord= xcord
        self.ycord=ycord
        self.health=health  
        self.last_move=""

    def which_building(self,brd):
        if(self.last_move == "down"):
            return position_check(self.xcord+1,self.ycord,brd)
        elif(self.last_move == "up"):
            return position_check(self.xcord-1,self.ycord,brd)
        elif(self.last_move== "right"):
            return position_check(self.xcord,self.ycord+1,brd)
        elif(self.last_move== "left"):
            return position_check(self.xcord,self.ycord-1,brd)
        
    def attack(self,brd):
        if(self.health>0):
            if(self.which_building(brd) == "Townhall"):
                brd.th.reduce_health(self.kill,brd)
            elif(self.which_building(brd) == "cannon_0"):
                brd.cannon_list[0].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "cannon_1"):
                brd.cannon_list[1].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "hut_0"):
                brd.hut_list[0].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "hut_1"):
                brd.hut_list[1].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "hut_2"):
                brd.hut_list[2].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "hut_3"):
                brd.hut_list[3].reduce_health(self.kill,brd)
            elif(self.which_building(brd)== "hut_4"):
                brd.hut_list[4].reduce_health(self.kill,brd)
            elif(self.which_building(brd)[:4]== "wall"):
                i = int(self.which_building(brd).split("_")[1])
                brd.wall_list[i].reduce_health(self.kill,brd)
            else:
                # print("No building in that direction")
                pass

class King(Troops):
    def __init__(self,grid,xcord,ycord):
       super().__init__(xcord,ycord,1,1,100)
       self.type="King"
       
       self.color=Fore.BLACK + Back.GREEN
       
       self.kill=10

       
       if(self.health>0):
        for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'K'+ Style.RESET_ALL)
    
    def movedown(self,grid):
        self.last_move= "down"
        if(self.health>0):
            if (grid.grid[self.xcord+1][self.ycord] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)

                self.xcord=self.xcord+1
                for i in range(self.length):
                        for j in range(self.width):
                            grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'K'+Style.RESET_ALL)
                
    def moveup(self,grid):
        self.last_move="up"
        if(self.health>0):
            if (grid.grid[self.xcord-1][self.ycord] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.xcord=self.xcord-1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'K'+Style.RESET_ALL)
                
    def moveright(self,grid):
        self.last_move="right"
        if(self.health>0):
            if (grid.grid[self.xcord][self.ycord+1] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.ycord=self.ycord+1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'K'+Style.RESET_ALL)
    
    def moveleft(self,grid): 
        self.last_move="left"
        if(self.health>0):
            if (grid.grid[self.xcord][self.ycord-1] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.ycord=self.ycord-1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'K'+Style.RESET_ALL)
                        
    def damage(self,damage):
        if(self.health>0 and self.health-damage>=0):
            self.health=self.health - damage
        else:
            self.health=0
            
    def update(self,grid):
        if(self.health<=0):
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j, blank_space)
    
    def get_direction(self,val):
        if(val == 's' or val == 'S'):
            return "down"

        elif(val == 'd' or val == 'D'):
            return "right"
           
        elif(val == 'w' or val == 'W'):
            return "up"
           
        elif(val == 'a' or val == 'A'):
            return "left"     
            
    def show_health(self,brd):
        print("King's health is: ",self.health)
        print("")
        if(self.health<=0):
            self.update(brd)
            print("King has died")
        health_bar = ""
        for i in range (int(self.health/10)):
            if i < 2:
               health_bar+=Fore.RED + "██" + Style.RESET_ALL
            elif i < 5:
                health_bar+=Fore.YELLOW + "██"+ Style.RESET_ALL
            else:
                health_bar+=Fore.GREEN + "██" + Style.RESET_ALL
        print(health_bar)
        print("")
        
    def leviathan_axe(self,brd):
        if(self.health>0):
            buildings=[]
            for i in range(-5,6):
                for j in range(-5,6):
                    var= position_check(self.xcord+i,self.ycord+j,brd)
                    if(var == "Townhall"):
                        buildings.append("Townhall")
                    elif(var == "cannon_0"):
                        buildings.append("cannon_0")  
                    elif(var== "cannon_1"):
                        buildings.append("cannon_1")
                    elif(var== "hut_0"):
                        buildings.append("hut_0")
                    elif(var== "hut_1"):
                        buildings.append("hut_1")
                    elif(var== "hut_2"):
                        buildings.append("hut_2")
                    elif(var== "hut_3"):
                        buildings.append("hut_3")
                    elif(var== "hut_4"):
                        buildings.append("hut_4")
                    elif(var[:4]== "wall"):
                        x = int(var.split("_")[1])
                        brd.wall_list[x].reduce_health(self.kill,brd)
                        
            unique_buildings = set(buildings)
            for var in unique_buildings:
                if(var == "Townhall"):
                    
                    brd.th.reduce_health(self.kill,brd)
                elif(var == "cannon_0"):
                    brd.cannon_list[0].reduce_health(self.kill,brd)
                elif(var== "cannon_1"):
                    brd.cannon_list[1].reduce_health(self.kill,brd)
                elif(var== "hut_0"):
                    brd.hut_list[0].reduce_health(self.kill,brd)
                elif(var== "hut_1"):
                    brd.hut_list[1].reduce_health(self.kill,brd)
                elif(var== "hut_2"):
                    brd.hut_list[2].reduce_health(self.kill,brd)
                elif(var== "hut_3"):
                    brd.hut_list[3].reduce_health(self.kill,brd)
                elif(var== "hut_4"):
                    brd.hut_list[4].reduce_health(self.kill,brd)
                # elif(var[:4]== "wall"):
                #     i = int(var.split("_")[1])
                #     brd.wall_list[i].reduce_health(self.kill,brd)
            
    
class Barbarians(Troops):
    def __init__(self,xcord,ycord):
        super().__init__(xcord,ycord,1,1,20)
        self.color=Fore.BLACK + Back.GREEN
        self.last_move = "up"
        self.alive = False
        self.is_dead= 0
        self.kill=5
     
    def spawn(self,grid):
        for i in range(self.length):
            for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'B' + Style.RESET_ALL)
                    
    
    def distance(self,build):
        return math.sqrt((self.xcord-build.xcord)**2 + (self.ycord-build.ycord)**2)
        
    
    def find_min(self,grid):
   
        # closest=Wall(grid,10000,10000)
        d=10000
        fl1=False
        for building in grid.hut_list:
            if(building.health>0):
                curr_dist=self.distance(building)
                if( curr_dist<d):
                    d=curr_dist
                    closest=building
                    fl1=True
            
        for building in grid.cannon_list:
            if(building.health>0):
                curr_dist=self.distance(building)
                if( curr_dist<d):
                    d=curr_dist
                    closest=building 
                    fl1=True         
       
        if(grid.th.health>0):
            curr_dist=self.distance(grid.th)
            if(curr_dist<d):
                d=curr_dist
                closest=grid.th
                fl1=True
            
        if(fl1):
            return closest
        else:
            # gend.win(grid)
            return False
    
    def changeColor(self, grid):
        if(self.health>0):
            i=self.health/2
            if i <= 2:
                self.color = Fore.BLACK + Back.RED
            elif i <= 5:
                self.color = Fore.BLACK + Back.YELLOW
            else:
                self.color = Fore.BLACK + Back.GREEN
    
    def movedown(self,grid):
        self.last_move= "down"
        if(self.health>0):
            if (grid.grid[self.xcord+1][self.ycord] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)

                self.xcord=self.xcord+1
                for i in range(self.length):
                        for j in range(self.width):
                            grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'B'+Style.RESET_ALL)
                
    def moveup(self,grid):
        self.last_move="up"
        if(self.health>0):
            if (grid.grid[self.xcord-1][self.ycord] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.xcord=self.xcord-1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'B'+Style.RESET_ALL)
                
    def moveright(self,grid):
        self.last_move="right"
        if(self.health>0):
            if (grid.grid[self.xcord][self.ycord+1] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.ycord=self.ycord+1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'B'+Style.RESET_ALL)
    
    def moveleft(self,grid): 
        self.last_move="left"
        if(self.health>0):
            if (grid.grid[self.xcord][self.ycord-1] == blank_space):
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,blank_space)
                self.ycord=self.ycord-1
                for i in range(self.length):
                    for j in range(self.width):
                        grid.change_grid(self.xcord+i,self.ycord+j,self.color + 'B'+Style.RESET_ALL)
    
    def move(self,grid):
        
        target=self.find_min(grid)
        if target:
            x=target.xcord
            y=target.ycord
            # print(x,y)
            
            if(self.xcord < x):
                self.movedown(grid)
            elif(self.xcord > x):
                self.moveup(grid)
            
            elif(self.ycord<y):
                self.moveright(grid)
            elif(self.ycord>y):
                self.moveleft(grid)
                
            self.attack(grid)
            return True
        else:
            return False
        
    def damage(self,damage,grid):
        if(self.health>0 and self.health-damage>=0):
            self.health=self.health - damage
            self.changeColor(grid)
        else:
            self.update(grid)
            self.health=0
            
    def update(self,grid):
        if(self.health<=0):
            self.is_dead= 1
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j, blank_space)
        
                                       
def position_check(xcord, ycord,brd):
    
    if(brd.th.xcord<=xcord<=brd.th.xcord + brd.th._height and brd.th.ycord<=ycord<=brd.th.ycord+brd.th._width):
        return "Townhall"
    
    elif(brd.cannon_list[0].xcord<=xcord<=brd.cannon_list[0].xcord + brd.cannon_list[0].length and 
         brd.cannon_list[0].ycord<=ycord<=brd.cannon_list[0].ycord+brd.cannon_list[0].width):
        return "cannon_0"
    
    elif(brd.cannon_list[1].xcord<=xcord<=brd.cannon_list[1].xcord + brd.cannon_list[1].length and 
         brd.cannon_list[1].ycord<=ycord<=brd.cannon_list[1].ycord+brd.cannon_list[1].width):
        return "cannon_1"
    
    elif(brd.hut_list[0].xcord<=xcord<=brd.hut_list[0].xcord + brd.hut_list[0].length and 
         brd.hut_list[0].ycord<=ycord<=brd.hut_list[0].ycord+brd.hut_list[0].width):
        return "hut_0"

    elif(brd.hut_list[1].xcord<=xcord<=brd.hut_list[1].xcord + brd.hut_list[1].length and 
         brd.hut_list[1].ycord<=ycord<=brd.hut_list[1].ycord+brd.hut_list[1].width):
        return "hut_1"
    
    elif(brd.hut_list[2].xcord<=xcord<=brd.hut_list[2].xcord + brd.hut_list[2].length and 
         brd.hut_list[2].ycord<=ycord<=brd.hut_list[2].ycord+brd.hut_list[2].width):
        return "hut_2"
    
    elif( brd.hut_list[3].xcord<=xcord<=brd.hut_list[3].xcord + brd.hut_list[3].length and 
         brd.hut_list[3].ycord<=ycord<=brd.hut_list[3].ycord+brd.hut_list[3].width):
        return "hut_3"
    
    elif(brd.hut_list[4].xcord<=xcord<=brd.hut_list[4].xcord + brd.hut_list[4].length and 
         brd.hut_list[4].ycord<=ycord<=brd.hut_list[4].ycord+brd.hut_list[4].width):
        return "hut_4"  
    
    for i in range(len(brd.wall_list)):
        wall=brd.wall_list[i]
        if(wall.xcord<=xcord<wall.xcord + wall.length and 
         wall.ycord<=ycord<wall.ycord+wall.width):
            return "wall_" + str(i)
    
    
    else:
        return "blank"
 