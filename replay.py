from src.gameinit import *
from src.main import *
from src.building import *
from src.troops import *
# from input import *
from src.spells import *
import time
import json

num = int(input("Enter the number: "))

with open("replays.json", "r") as f:
    data = json.load(f)
    
input_data = data[num]['i']


timeout = 0.18
frames = 0
input_arr = []
rageMultiplier = 1

if __name__ == "__main__":
    for val in input_data:
        frames += 1
        input_time = time.time()
        # if timeout - (time.time() - input_time) >= 0:
        #     time.sleep(timeout - (time.time() - input_time))
        # val = input_to(Get(),timeout)
        # input_arr.append(val)
        # brd.raja.get_direction(val)
        print_board(brd,input_arr,True)
        if frames % rageMultiplier == 0:
            brd.cannon_list[0].attack(brd)
            brd.cannon_list[1].attack(brd)
        if(val == 'q' or val == 'Q'):
            break
        elif(val == 's' or val == 'S'):
            brd.raja.movedown(brd)
            
        elif(val == 'd' or val == 'D'):
            brd.raja.moveright(brd)
            
        elif(val == 'w' or val == 'W'):
            brd.raja.moveup(brd)
            
        elif(val == 'a' or val == 'A'):
            brd.raja.moveleft(brd)
            
        elif(val == '1'):
            gunda1 = Barbarians(sp1.pussyX, sp1.pussyY)
            brd.gunda_list.append(gunda1)
            gunda1.spawn(brd)
            gunda1.alive=True
            
        elif(val == '2'):
            gunda2 = Barbarians(sp2.pussyX, sp2.pussyY)
            brd.gunda_list.append(gunda2)
            gunda2.spawn(brd)
            gunda2.alive=True
            
        elif(val == '3'):
            gunda3 = Barbarians(sp3.pussyX, sp3.pussyY)
            brd.gunda_list.append(gunda3)
            gunda3.spawn(brd)
            gunda3.alive=True
            
        elif(val==' '):
            brd.raja.attack(brd)
            
        elif(val=='h' or val=='H'):
            heal1=heal()
            heal1.get_heal(brd)
            
        elif(val=='r' or val=='R'):
            rage1=rage()
            timeout/=2
            rageMultiplier*=2
            rage1.get_rage(brd)
            
        elif(val=='l' or val=='L'):
            brd.raja.leviathan_axe(brd)
            
        time.sleep(timeout)
            
        # elif(val=='c' or val=='C'):
        #     print(gunda1.find_min(brd))
        #     gunda1.move(brd)
            

    
                    