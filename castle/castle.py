
import pyxel
import font as ft
import var_and_const as vc
import screen as sc
import player

####====================================

MAIN_CASTLE_KEYS = [pyxel.KEY_G,    # GUILD
                    pyxel.KEY_I,    # INN
                    pyxel.KEY_S,    # STORE
                    pyxel.KEY_M,    # MAZE
                    pyxel.KEY_Q]    # QUIT GAME

####====================================

class Castle:
    def __init__(self, g):
        
        self.game = g

        self.state = "castle_top"
        
        self.scene = {}
        self.scene["castle_top"] = castle.castle_top.Castle_Top_exe()

####////////////////////////////////////

    def update(self):
        self.scene[self.state].update()

####////////////////////////////////////

    def draw(self):
        self.scene[self.state].draw()