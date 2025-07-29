import pyxel
import var_and_const as vc
import screen as sc

import guild as gd
import player.player as pl
import maze.maze     as mz
####====================================
#### VARIABLES & CONSTANT

PARTY_MAX = 4

####====================================
#### FUNCTIONS

PARTY_SELECT_LIST = [None,
                     None,
                     [pyxel.KEY_1,pyxel.KEY_2],
                     [pyxel.KEY_1,pyxel.KEY_2,pyxel.KEY_3],
                     [pyxel.KEY_1,pyxel.KEY_2,pyxel.KEY_3,pyxel.KEY_4]]

def select_party_member(p):
    n=len(pt.members)
    if n==0:
        return(False)
    elif n==1:
        return(1)
    else:
        l=PARTY_SELECT_LIST[n] #n=2,3,4のとき
        result=vc.detect_key(l)
        if result:
            return(result)
        else:
            return(False)
        
####====================================
#### CLASS

class Party:

    def __init__(self,g):
        
        self.game = g

        self.in_maze = False
        self.wxy = mz.INITIAL_WXY
        self.xy = mz.INITIAL_XY
        self.members = []
        self.scanned = [[False for _ in range(mz.MAZE_SIZE)] for _ in range(mz.WORLD_SIZE)]
                        # self.scanned[wxy][xy]の順番
        self.gold = 0
        self.key_item = []
        self.bag = []

    def add(self,pc):
        self.members.append(pc)
        pc.in_party = True

    def remove(self,pc):
        pc.in_party = False
        self.members.pop(pc)

    def join_from_guild(self,guild):
        for pc in guild.members:
            if pc.in_party:
                self.members.append(pc)
    
    def list_party_members(self):
        sc.line_horizontal(sc.TEXT_BOTTOM-5,'-')
        for i in range(1,PARTY_MAX):
            sc.text12(0,sc.PARTY_MEMBER_TOP+i,f"{i:2}",7)
        y = 0
        if self.members:
            for pc in self.members:
                s = f"{pc.one_string}"
                sc.text12(3, sc.PARTY_MEMBER_TOP+y, s, 7)
            y += 1
        
    def check_full(self):
        if len(self.members) >= PARTY_MAX:
            return(True)
        else:
            return(False)

    def check_empty(self):
        if len(self.members) == 0:
            retrun(True)
        else:
            return(False)

    
####====================================

    def update(self):
        pass

####====================================

    def draw(self):
        pass
