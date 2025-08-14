import pyxel
import var_and_const as vc
import screen        as sc

import party  as pt
import player as pl

import guild  as gd
import inn

# ####====================================
# #### CONSTANT

INN_TOP_MENU_TOP = 12

# ####====================================
# #### FUNCTIONS

def draw_inn_top_menu():
    sc.line_horizontal(INN_TOP_MENU_TOP-1,"- ")
    sc.text12( 10,INN_TOP_MENU_TOP+1,"A) 安い部屋",7)
    sc.text12( 10,INN_TOP_MENU_TOP+2,"B) 中くらいの部屋",7)
    sc.text12( 10,INN_TOP_MENU_TOP+3,"C) 高い部屋",7)
    sc.text12( 20,INN_TOP_MENU_TOP+6,"X) to Leave",7)

####====================================
#### CLASS

class Inn_Top_exe():

####////////////////////////////////////

    def __init__(self):
        self.exit = False

####////////////////////////////////////

    def update(self):
        if pyxel.btnp(pyxel.KEY_A):
            print("安い部屋")
        elif pyxel.btnp(pyxel.KEY_B):
            print("中くらいの部屋")
        elif pyxel.btnp(pyxel.KEY_C):
            print("高い部屋")
        elif pyxel.btnp(pyxel.KEY_X):
            vc.game.state = "castle"

####////////////////////////////////////

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"やど ：イノシカ亭",0)
        
        vc.party.list_party_members()
        
        draw_inn_top_menu()