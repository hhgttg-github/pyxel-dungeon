
import pyxel
import font as ft
import var_and_const as vc
import screen as sc
import player

####====================================
#### CONSTANT

CASTLE_TOP_MENU_TOP = 12

####====================================
#### FUNCTIONS

def draw_castle_top_menu():
    sc.line_horizontal(CASTLE_TOP_MENU_TOP-1,"- ")
    sc.text12(3,CASTLE_TOP_MENU_TOP+1,"G)uild      I)nn      S)tore      M)aze",7)
    sc.text12(20 ,CASTLE_TOP_MENU_TOP+6,"Q) to Quit Game",7)
    
####====================================

MAIN_CASTLE_KEYS = [pyxel.KEY_G,    # GUILD
                    pyxel.KEY_I,    # INN
                    pyxel.KEY_S,    # STORE
                    pyxel.KEY_M,    # MAZE
                    pyxel.KEY_Q]    # QUIT GAME

####====================================

class Castle:
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
        print(f"vc.game.state = {vc.game.state}")

####////////////////////////////////////

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"東那グリット城 城下町",0)
        
        vc.party.list_party_members()
        draw_castle_top_menu()