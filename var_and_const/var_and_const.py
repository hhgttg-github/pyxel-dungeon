
import pyxel

import guild as gd
import party.party as pt
import castle.castle
import inn.inn

####===================================
#### VARIABLES

game = None

item_db    = None
monster_db = None

guild = gd.guild.Guild()
party = pt.Party()

castle = castle.castle.Castle()
inn = inn.inn.Inn()

maze = None

####====================================
####
#### KEY_INPUT
####
#### pyxel.KEY_A=97, pyxel.KEY_Z=122
#### ord('a')   =97, ord('z')   =122
#### pyxel.KEY_A = ord('a')
#### pyxel.KEY_0=ord('0')=48, pyxel.KEY_9=ord('9')=57

KEY_CANCEL = -1

KEY_DIR = [pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_UP, pyxel.KEY_DOWN]

KEY_AZ = [x for x in range(pyxel.KEY_A,pyxel.KEY_Z+1)]
KEY_09 = [x for x in range(pyxel.KEY_0,pyxel.KEY_9)]
KEY_14 = [pyxel.KEY_1,pyxel.KEY_2,pyxel.KEY_3,pyxel.KEY_4]
# pyxel.KEY_1 = 49, k-48=n
KEY_14X = KEY_14 + [pyxel.KEY_X]
KEY_SRE = [pyxel.KEY_SPACE, pyxel.KEY_RETURN, pyxel.KEY_ESCAPE]
KEY_09AZE = KEY_09 + KEY_AZ + [pyxel.KEY_ESCAPE]
KEY_ANY = KEY_AZ + KEY_09 + KEY_SRE

####====================================

def detect_key(l):
    result=list(filter(lambda x:pyxel.btnp(x), l))
    if result:
        print(f"result={result[0]}")
        return(result[0])
    return(False)

def detect_key_yn():
    
    # y/n/xでpyxel.KEY_Y/N/C を返す
    # キーが押されなかったらFalseを返す
    
    l = [pyxel.KEY_Y,pyxel.KEY_N,pyxel.KEY_X,pyxel.KEY_ESCAPE]
    result=list(filter(lambda x:pyxel.btnp(x), l))
    if result:
        result=result[0]
        if result in l:
            return(result)

def detect_key_party_member():
    result=list(filter(lambda x:pyxel.btnp(x), KEY_14X))
    if result:
        result=result[0]
        if result==pyxel.KEY_X:
            return(result)
        elif result in KEY_14:
            n=len(party.members)
            k= result - 48 # pyxel.KEY_1=49
            if k<=n:
                return(k)
            else:
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
