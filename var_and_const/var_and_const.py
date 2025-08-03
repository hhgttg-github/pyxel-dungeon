
import pyxel

import guild as gd
import party.party as pt

####===================================
#### VARIABLES

game = None

item_db    = None
monster_db = None

guild = gd.guild.Guild()
party = pt.Party()
maze = None

####====================================
####
#### KEY_INPUT
####
#### pyxel.KEY_A=97, pyxel.KEY_Z=122
#### ord('A')   =65, ord('Z')   =90
#### pyxel.KEY_A = ord('A') + 32
#### pyxel.KEY_0=ord('0')=48, pyxel.KEY_9=ord('9')=57

KEY_CANCEL = -1

KEY_DIR = [pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_UP, pyxel.KEY_DOWN]

KEY_AZ = [x for x in range(pyxel.KEY_A,pyxel.KEY_Z+1)]
KEY_09 = [x for x in range(pyxel.KEY_0,pyxel.KEY_9)]
KEY_SRE = [pyxel.KEY_SPACE, pyxel.KEY_RETURN, pyxel.KEY_ESCAPE]
KEY_09AZE = KEY_09 + KEY_AZ + [pyxel.KEY_ESCAPE]

def detect_key(l):
    if l:
        result=list(filter(lambda x:pyxel.btnp(x), l))
        if True in result:
            return(l.index(True))
        return(False)

####====================================

def access_nth(l,n):
    if l:
        if n <= (len(l)-1):
            return(l[n])
        else:
            return(False)
    return(False)

####====================================
#### FUNCTIONS
