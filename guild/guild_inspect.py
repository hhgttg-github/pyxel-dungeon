import time,pyxel

import var_and_const as vc
import screen as sc
import guild as gd
import player as pl

####====================================
#### VARIABLES & CONSTANT
pass

####====================================
#### FUNCTIONS
pass

####====================================
#### CLASS

class Guild_Inspect_exe:

####------------------------------------

    def __init__(self):
        self.on_screen_member = False
    
####====================================

    def update(self):
        k = vc.detect_key(vc.KEY_AZ)
        if k:
            if k == pyxel.KEY_X:
                if self.on_screen_member:
                    self.on_screen_member = False
                    vc.guild.state = "guild_inspect"
                    return()
                vc.guild.state = "guild_top"              
            else:
                i = k - ord('a')
                count_members = len(vc.guild.members) - 1
                if i <= count_members:
                    self.on_screen_member = vc.guild.members[i]


####====================================

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"ぼうけんしゃギルド",0)
        if self.on_screen_member:
            pl.inspect_pc(self.on_screen_member)
            sc.text12(12,sc.TEXT_BOTTOM-1,"(X) to Exit",7)
            pyxel.flip()
        else:
            vc.guild.list_guild_members()
            vc.party.list_party_members()
            c_top = sc.CENTER_MENU_TOP
            sc.clear_area(sc.AREA_CENTER_MENU)
            if vc.guild.check_empty():
                sc.text12(6,c_top+2,"ギルドメンバーは だれも いません",7)
                pyxel.flip()
                time.sleep(1)
                vc.guild.state = 'guild_top'
            else:
                sc.text12(6,c_top+2,"誰を確認しますか？    (X) to Exit",7)
        