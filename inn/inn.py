import pyxel
import var_and_const as vc
import screen        as sc

import inn

#####====================================

class Inn():
    
    def __init__(self):
        self.scene = {}
        self.scene["inn_top"] = inn.inn_top.Inn_Top_exe()
        self.state = "inn_top"

#####////////////////////////////////////
 
    def update(self):
        self.scene[self.state].update()

#####////////////////////////////////////

    def draw(self):
        print("Inn.draw(self)")
        self.scene[self.state].draw()