import time
import pyxel
import var_and_const as vc
import screen as sc

import party as pt
import player as pl

import guild as gd

####====================================
#### VARIABLES & CONSTANT
pass

####====================================
#### FUNCTIONS
pass

####====================================
#### CLASS

class Guild_Newbi_exe:

####====================================

    def __init__(self):
        self.exit = False

####====================================

    def exit_this(self):
        self.exit = False
        vc.guild.state = "guild_top"

####====================================

    def update(self):
        if vc.guild.check_full():
            sc.ERASE_CENTER_FRAME()
            sc.text12(4,15,"ギルドまんいん。しんき は おことわりです",7)
            pyxel.flip()
            time.sleep(2)
            vc.guild.state = "guild_top"
            return() #おことわりにつき、メインループに戻る
        #上記より、ギルドに空きがある前提で以下に進む。
        p = None
        if pyxel.btnp(pyxel.KEY_A):
            p = pl.Player(job = "fighter")
        elif pyxel.btnp(pyxel.KEY_B):
            p = pl.Player(job = "thief")
        elif pyxel.btnp(pyxel.KEY_C):
            p = pl.Player(job = "mage")
        elif pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.KEY_ESCAPE):
            self.exit = True
        if p:
            vc.guild.add_member(p)
            vc.guild.list_guild_members()
            self.exit = True

        if self.exit == True:
            self.exit_this()

####====================================

    def draw(self):
        c_top = sc.CENTER_MENU_TOP
        sc.clear_area(sc.AREA_CENTER_MENU)
        sc.text12(6,c_top+2,"職業は？    (X) to Exit",7)
        sc.text12(10,c_top+3,"A) 戦士",7)
        sc.text12(10,c_top+4,"B) 盗賊",7)
        sc.text12(10,c_top+5,"C) 魔法使い",7)
