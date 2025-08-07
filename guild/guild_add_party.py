import time, pyxel
import var_and_const as vc
import screen as sc

import guild as gd
import party as pt
import player as pl

####====================================
#### VARIABLES & CONSTANT
pass

####====================================
#### FUNCTIONS
pass

####====================================
#### CLASS

class Guild_Add_Party_exe:

####====================================

    def __init__(self):
        self.exit = False

####====================================

    def update(self):
        i = vc.guild.select_guild_members()
        if (i==False) or (i==None):
            return()
        if i>=0:
            pc = vc.guild.members[i]
            print(pc)
            if pc.in_party:
                sc.ERASE_CENTER_FRAME()
                sc.text12(6,sc.CENTER_MENU_TOP+2,"すでに パーティに います",7)
                pyxel.flip()
                time.sleep(1)
                vc.guild.state = "guild_top"
            else:
                pc.in_party = True
                vc.party.members.append(pc)
                vc.guild.state = "guild_top"
        else:
            vc.guild.state = "guild_top"

####====================================

    def draw(self):
        sc.ERASE_CENTER_FRAME()
        if vc.guild.check_empty():
            sc.text12(6,sc.CENTER_MENU_TOP+2,"ギルドメンバーは だれも いません",7)
            pyxel.flip()
            time.sleep(1)
            vc.guild.state = "guild_top"
        elif vc.party.check_full():
            sc.text12(6,sc.CENTER_MENU_TOP+2,"パーティが まんいん です",7)
            pyxel.flip()
            time.sleep(1)
            vc.guild.state = "guild_top"
        else:
            sc.text12(6,sc.CENTER_MENU_TOP+2,"だれ を パーティに よぶ？   (X) to Exit",7)
