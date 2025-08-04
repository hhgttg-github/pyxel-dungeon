import pyxel
import var_and_const as vc
import screen as sc
import guild as gd
import player as pl

####====================================
#### VARIABLES & CONSTANT
pass

####====================================
#### FUNCTIONS
pass

####====================================
#### CLASS

class Guild_Inspect_exe:

####------------------------------------

    def __init__(self):
        self.exit = False
    
####====================================

    def update(self):
        pass

####====================================

    def draw(self):
        c_top = sc.CENTER_MENU_TOP
        sc.clear_area(sc.AREA_CENTER_MENU)
        sc.text12(6,c_top+5,"誰を確認しますか？    (X) to Exit",7)