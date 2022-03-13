from src.gameinit import *
# from game import *
from colorama import Fore, Back, Style
from copy import deepcopy

blank_space= Fore.GREEN + Back.GREEN + ' ' + Style.RESET_ALL

class Building:
    def __init__(self, xcord, ycord, length, width,health):
        # self.type="Building"
        self.length=length
        self.width=width
        self.xcord= xcord
        self.ycord=ycord
        self.health= health
        
    def reduce_health(self,damage,brd):
        if(self.health>0):
            self.health=self.health - damage
            self.update(brd)
        if(self.health<=0):
            self.health=0
   
        
class TownHall(Building):
    def __init__(self,grid, xcord, ycord,length=2, width=2,health=100):
        self.color = Fore.BLACK + Back.GREEN
        self.type="TownHall"
        super().__init__(xcord, ycord,length,width,health)
        
        with open('./src/TH.txt', 'rb') as f:
            arr = []
            cnt = 0
            mx = -1
            for line in f:
                arr.append(line)
                mx = max(mx, len(arr[cnt]))
                cnt += 1
        f.close()
        self._height = len(arr)
        self._width = mx
    
        for i in range(self._height):
            # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
            for j in range(len(arr[i])-1): 
                grid.change_grid(i+self.xcord,j+self.ycord, self.color + chr(arr[i][j]) + Style.RESET_ALL)
                
    def change_color(self):
        if(self.health>0):
            i=self.health/10
            if i <= 2:
                self.color = Fore.BLACK + Back.RED
            elif i <= 5:
                self.color = Fore.BLACK + Back.YELLOW
            else:
                self.color = Fore.BLACK + Back.GREEN
                

    def update(self,grid):
        self.change_color()
        with open('./src/TH.txt', 'rb') as f:
            arr = []
            cnt = 0
            mx = -1
            for line in f:
                arr.append(line)
                mx = max(mx, len(arr[cnt]))
                cnt += 1
        f.close()
        self._height = len(arr)
        self._width = mx
        
        if(self.health<=0):
            for i in range(self._height):
                # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
                for j in range(len(arr[i])-1): 
                    grid.change_grid(i+self.xcord,j+self.ycord, blank_space)
        
        else:
            for i in range(self._height):
                # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
                for j in range(len(arr[i])-1): 
                    grid.change_grid(i+self.xcord,j+self.ycord, self.color + chr(arr[i][j]) + Style.RESET_ALL)
    
 
            
class Hut(Building):
    def __init__(self,grid, xcord, ycord, length=3, width=4,health=50):
        self.color = Fore.BLACK + Back.GREEN
        self.type="Hut"
        super().__init__(xcord, ycord, length, width,health)
        
        with open('./src/hut.txt', 'rb') as f:
            arr = []
            cnt = 0
            mx = -1
            for line in f:
                arr.append(line)
                mx = max(mx, len(arr[cnt]))
                cnt += 1
        f.close()
        self._height = len(arr)
        self._width = mx

        for i in range(self._height):
            # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
            for j in range(len(arr[i])-1):
                grid.change_grid(i+self.xcord,j+self.ycord,self.color + chr(arr[i][j]) + Style.RESET_ALL)
                
            
    def change_color(self):
        i=self.health/5
        if i <= 2:
            self.color = Fore.BLACK + Back.RED
        elif i <= 5:
            self.color = Fore.BLACK + Back.YELLOW
        else:
            self.color = Fore.BLACK + Back.GREEN

    def update(self,grid):
        self.change_color()
        with open('./src/hut.txt', 'rb') as f:
            arr = []
            cnt = 0
            mx = -1
            for line in f:
                arr.append(line)
                mx = max(mx, len(arr[cnt]))
                cnt += 1
        f.close()
        self._height = len(arr)
        self._width = mx
        
        if(self.health<=0):
            for i in range(self._height):
                # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
                for j in range(len(arr[i])-1): 
                    grid.change_grid(i+self.xcord,j+self.ycord, blank_space)
        
        else:
           for i in range(self._height):
                # to remove last '\n' character in ascii art present already I have made loop till len(arr[i]) - 1
            for j in range(len(arr[i])-1):
                grid.change_grid(i+self.xcord,j+self.ycord,self.color + chr(arr[i][j]) + Style.RESET_ALL)
                
class Cannon(Building):
    def __init__(self,grid, xcord, ycord, length=3, width=1,health=50):
        self.color = Fore.BLACK + Back.GREEN
        self.type="Cannon"
        self.damage=2
        super().__init__(xcord, ycord, length, width,health)

        for i in range(self.length):
            for j in range(self.width):
                grid.change_grid(self.xcord+i,self.ycord+j,self.color+'C'+ Style.RESET_ALL)
  
    def change_color(self):
        i=self.health/5
        if i <= 2:
            self.color = Fore.BLACK + Back.RED
        elif i <= 5:
            self.color = Fore.BLACK + Back.YELLOW
        else:
            self.color = Fore.BLACK + Back.GREEN
            
    def update(self,grid):
        self.change_color()
        
        if(self.health<=0):
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j, blank_space)
        
        else:
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j,self.color+'C'+ Style.RESET_ALL)
                    
    def attack(self,brd):
        if(self.health>0):
            fl = False
            for i in range(-5,6):
                for j in range(-5,6):
                    if(brd.raja.xcord == self.xcord+i and brd.raja.ycord == self.ycord+j):
                        self.cannon_attacking(brd)
                        brd.raja.damage(self.damage)
                        fl = True
                        break
                    for everyGunda in brd.gunda_list:  
                        if(everyGunda.xcord == self.xcord+i and everyGunda.ycord == self.ycord+j):
                            if(everyGunda.is_dead == 0):
                                self.cannon_attacking(brd)
                                everyGunda.damage(self.damage,brd)
                                fl = True
                                break
                if(fl):
                    break
            if not fl:
                self.cannon_not_attacking(brd)
                        
    def cannon_attacking(self,grid):
        self.color=Fore.BLACK + Back.WHITE
        for i in range(self.length):
            for j in range(self.width):
                grid.change_grid(self.xcord+i,self.ycord+j,self.color+'C'+ Style.RESET_ALL)

    def cannon_not_attacking(self,grid):
        self.color=Fore.BLACK + Back.GREEN
        for i in range(self.length):
            for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j,self.color+'C'+ Style.RESET_ALL)
                    
                    
                             
                
class Wall(Building):
    def __init__(self,grid, xcord, ycord, length=1, width=1,health=50):
        self.color = Fore.BLACK + Back.GREEN
        self.type="Wall"
        super().__init__(xcord, ycord, length, width,health)

        for i in range(self.length):
            for j in range(self.width):
                grid.change_grid(self.xcord+i,self.ycord+j,self.color+ '█'+ Style.RESET_ALL)
                
            
    def change_color(self):
        i=self.health/5
        if i <= 2:
            self.color = Fore.RED 
        elif i <= 5:
            self.color = Fore.YELLOW 
        else:
            self.color = Fore.BLACK 
            
    def update(self,grid):
        self.change_color()
        
        if(self.health<=0):
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j, blank_space)
    
        else:
            for i in range(self.length):
                for j in range(self.width):
                    grid.change_grid(self.xcord+i,self.ycord+j,self.color+ '█'+ Style.RESET_ALL)
        