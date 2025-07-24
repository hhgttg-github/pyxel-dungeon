
import pyxel

####====================================
#### VARIABLES

game = None

item_db    = None
monster_db = None

party = None
maze = None

####====================================
####
#### KEY_INPUT
####
#### pyxel.KEY_A=97, pyxel.KEY_Z=122
#### ord('A')   =65, ord('Z')   =90
#### pyxel.KEY_A = ord('A') + 32
#### pyxel.KEY_0=ord('0')=48, pyxel.KEY_9=ord('9')=57

KEY_DIR = [pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_UP, pyxel.KEY_DOWN]

KEY_AZ = [x for x in range(pyxel.KEY_A,pyxel.KEY_Z+1)]
KEY_09 = [x for x in range(pyxel.KEY_0,pyxel.KEY_9)]
KEY_SRE = [pyxel.KEY_SPACE, pyxel.KEY_RETURN, pyxel.KEY_ESCAPE]
KEY_ANY = KEY_AZ + KEY_09 + KEY_SRE + KEY_DIR

class Detect_key:
    def __init__(self):
        self.key = None
        self.key_list = None
    def update(self):
        if self.key_list==None:
            for k in KEY_ANY:
                if pyxel.btn(k):
                    self.key = k
        else:
            for k in self.key_list:
                if pyxel.btn(k):
                    self.key = k
                    self.key_list = None
    def reset(self):
        self.key_list = None
        self.key = None