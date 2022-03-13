

class heal:
    
    def get_heal(self,brd):
        if(brd.raja.health>0):
            if(brd.raja.health * 1.5 <= 100):
                brd.raja.health = brd.raja.health * 1.5
            else:
                brd.raja.health = 100
        for everyGunda in brd.gunda_list:
            if(everyGunda.health>0):
                if(everyGunda.health * 1.5 <= 50):
                    everyGunda.health = everyGunda.health * 1.5
            else:
                everyGunda.health = 50
            
            everyGunda.update(brd)
            
class rage:
    
    def get_rage(self,brd):
        if(brd.raja.health>0):
            brd.raja.kill = brd.raja.kill * 2
        for everyGunda in brd.gunda_list:
            everyGunda.kill = everyGunda.kill * 2

# class rage:
    
    