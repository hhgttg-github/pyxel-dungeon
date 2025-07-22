
import pyxel
from font import font as ft
from screen import screen as sc
from var_and_const import var_and_const as vc
from player import player

####====================================

MAIN_CASTLE_KEYS = [pyxel.KEY_G,    # GUILD
                    pyxel.KEY_I,    # INN
                    pyxel.KEY_S,    # STORE
                    pyxel.KEY_M,    # MAZE
                    pyxel.KEY_Q]    # QUIT GAME

####====================================

class Castle:
    def __init__(self):
        self.game = None

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def update(self):
        k = sc.key_input(MAIN_CASTLE_KEYS)
        match k:
            case pyxel.KEY_I:
                self.game.state = "inn"
            case pyxel.KEY_G:
                self.game.state = "guild"
            case pyxel.KEY_S:
                self.game.state = "store"
            case pyxel.KEY_M:
                self.game.state = "camp"
            case pyxel.KEY_Q:
                self.game.state = "quit"

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"東ナグリット城",0)
        player.list_party_members(vc.party)
        pass