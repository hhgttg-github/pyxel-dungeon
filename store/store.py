
import pyxel
import var_and_const as vc
import screen        as sc
import player
import store

####====================================
#### CONSTANT

####====================================
#### FUNCTIONS

####====================================

class Store():
    def __init__(self):
        self.scene = {}
        self.state = "store_top"

        self.scene["store_top"] = store.store_top.Store_Top_exe()
        self.scene["store_buy"] = store.store_buy.Store_Buy_exe()
        self.scene["store_sell"] = store.store_sell.Store_Sell_exe()

#####////////////////////////////////////
 
    def update(self):
        self.scene[self.state].update()

#####////////////////////////////////////

    def draw(self):
        self.scene[self.state].draw()