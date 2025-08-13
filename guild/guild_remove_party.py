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

class Guild_Remove_Party_exe:

####====================================

    def __init__(self):
        pass

####====================================

    def update(self):
        k = vc.detect_key_party_member()
        if k:
            if k == pyxel.KEY_X:
                vc.guild.state = "guild_top"              
            else:
                pc = vc.party.members[k-1]
                vc.party.remove_member(pc)

####====================================

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"ぼうけんしゃギルド",0)
        vc.guild.list_guild_members()
        vc.party.list_party_members()
        sc.ERASE_CENTER_FRAME()
        if vc.guild.check_empty():
            sc.text12(6,sc.CENTER_MENU_TOP+2,"ギルドメンバーは だれも いません",7)
            pyxel.flip()
            time.sleep(1)
            vc.guild.state = "guild_top"
        elif vc.party.check_empty():
            sc.text12(6,sc.CENTER_MENU_TOP+2,"パーティには だれも いません",7)
            pyxel.flip()
            time.sleep(1)
            vc.guild.state = "guild_top"
        else:
            sc.text12(6,sc.CENTER_MENU_TOP+2,"だれ を パーティから はずしますか？  (X)もどる",7)