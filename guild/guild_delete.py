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

class Guild_Delete_exe:

####====================================

    def __init__(self):
        self.on_screen_member = None

####====================================

    def update(self):
        if self.on_screen_member:
            k=vc.detect_key_yn()
            if k==pyxel.KEY_Y:
                sc.ERASE_CENTER_FRAME()
                nm=self.on_screen_member.name
                sc.text12(6,sc.CENTER_MENU_TOP+2,f"{nm}さん を じょめいしました",7)
                if self.on_screen_member.in_party:
                    vc.party.remove_member(self.on_screen_member)
                vc.guild.delete_member(self.on_screen_member)
                pyxel.flip()
                time.sleep(1)
                self.on_screen_member = None
                vc.guild.state = "guild_top"
            elif (k==pyxel.KEY_N) or (k==pyxel.KEY_X):
                self.on_screen_member = None
                vc.guild.state = "guild_top"
        else:
            k = vc.detect_key(vc.KEY_AZ)
            if k:
                if k == pyxel.KEY_X:
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
            sc.text12(3,sc.TEXT_BOTTOM-1,"(Y)じょめいする  (N)じょめいしない  (X)もどる",7)
            pyxel.flip()
        else:
            vc.guild.list_guild_members()
            vc.party.list_party_members()
            sc.ERASE_CENTER_FRAME()
            if vc.guild.check_empty():
                sc.text12(6,sc.CENTER_MENU_TOP+2,"ギルドメンバーは だれも いません",7)
                pyxel.flip()
                time.sleep(1)
                vc.guild.state = "guild_top"
            else:
                sc.text12(6,sc.CENTER_MENU_TOP+2,"だれ を じょめい しますか？  (X)もどる",7)
