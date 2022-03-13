
from src.main import *
from src.game_end import game_end
from src.building import *
from src.troops import *

from colorama import Fore, Back, Style
import time

# colorama.init()

class spawningPoints():
    def __init__(self, posX, posY):
        self.pussyY = posY
        self.pussyX = posX

brd = Board(25,50)
brd.board_array()
brd.initialise()
# brd.change_grid(1,1, Back.RED + 'R' + Style.RESET_ALL)

# th=TownHall(brd,10,18)
brd.set_townhall(brd,10,18)
brd.set_hut(brd,[(5,15),(5,20),(10,35),(15,35),(13,40)])
brd.set_cannon(brd,[(5,30),(14,12)])
brd.set_wall(brd,[(3, j) for j in range(6, 46)] 
            + [(20, j) for j in range(5, 46)] 
            + [(i, 5) for i in range(3, 20)] 
            + [(i, 45) for i in range(3, 20)])
brd.set_raja(brd,2,2)

sp1 = spawningPoints(2, 3)
sp2 = spawningPoints(1, 30)
sp3 = spawningPoints(15, 1)

# gundaList = []
# brd.set_heal(brd)

def print_board(board,input_arr, replay=False):
    os.system('clear')
    gend.lose(brd,input_arr,replay)
    gend.win(brd,input_arr,replay)
    brd.raja.show_health(brd)
    for everyGunda in brd.gunda_list:
        f = everyGunda.move(board)
        if not f:
            gend.win(brd,input_arr,replay)
    
    print("Town Hall health is: ",brd.th.health)
    # raja.get_direction()

    # print("Wall health is: ",brd.wall_list[0].health)
    for i in range(board.row):
        for j in range(board.column):
            print(board.grid[i][j] , end='')
        print()    

