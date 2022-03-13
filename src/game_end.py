import numpy as np
import os
from colorama import Fore, Back, Style
import json

class game_end():
    def replay_store(self,input_arr):
        with open('replays.json', 'r+' ) as f:
            data = json.loads(f.read())
            data.append({'i': input_arr})
            f.seek(0)
            f.write(json.dumps(data))
    
    def lose(self,brd,input_arr,replay):
        
        aisiye=True
        for everyGunda in brd.gunda_list:
            if(everyGunda.is_dead == 0):
                aisiye=False
                
            
        if(brd.raja.health==0 and aisiye==True):
            os.system('clear')
            os.system("stty echo")
            if not replay:
                self.replay_store(input_arr)
            f = open('./src/lose.txt', 'r')
            content = f.read()
            print(content)
            f.close()
            exit()

    def win(self,brd,input_arr,replay):
        if(brd.th.health==0 and brd.hut_list[0].health==0 and 
           brd.hut_list[1].health==0 and brd.hut_list[2].health==0 and 
           brd.hut_list[3].health==0 and brd.hut_list[4].health==0 and 
           brd.cannon_list[0].health==0 and brd.cannon_list[1].health==0):
            os.system('clear')
            os.system("stty echo")  
            if not replay:       
                self.replay_store(input_arr)
            f = open('./src/win.txt', 'r')
            content = f.read()
            print(Fore.RED+ content)
            f.close()
            exit()