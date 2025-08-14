
import pyxel
import var_and_const as vc
import screen        as sc

import party  as pt
import player as pl

import guild  as gd

# ####====================================
# #### CONSTANT

CASTLE_TOP_MENU_TOP = 12

# ####====================================
# #### FUNCTIONS

def draw_castle_top_menu():
    sc.line_horizontal(CASTLE_TOP_MENU_TOP-1,"- ")
    sc.text12(6,CASTLE_TOP_MENU_TOP+1,"G)uild   I)nn   S)tore   M)aze",7)
    sc.text12(12 ,CASTLE_TOP_MENU_TOP+3,"(Q) to Quit Game",7)

####====================================
#### CLASS

class Castle_Top_exe():
    
####////////////////////////////////////

    def __init__(self):
        pass

####////////////////////////////////////

    def update(self):
        if pyxel.btnp(pyxel.KEY_G):
            vc.game.state = "guild"
            vc.guild.state = "guild_top"
        elif pyxel.btnp(pyxel.KEY_I):
            vc.game.state = "inn"
            vc.inn.state = "inn_top"
        elif pyxel.btnp(pyxel.KEY_S):
            vc.game.state = "store"
            vc.store.state = "store_top"
        elif pyxel.btnp(pyxel.KEY_Q):
            vc.game.state = "quit_game"
        elif pyxel.btnp(pyxel.KEY_M):
            vc.game.state = "maze"
            vc.maze.state = "maze_entrance"

####////////////////////////////////////

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"東那グリット城 城下町",0)
        
        vc.party.list_party_members()
        draw_castle_top_menu()