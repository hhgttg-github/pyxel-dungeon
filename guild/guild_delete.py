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
    def check_delete(self):
        k=vc.detect_key_yn()
        if k=="Yes":
            sc.ERASE_CENTER_FRAME()
            name=self.on_screen_member.name
            sc.text12(6,sc.CENTER_MENU_TOP+2,f"{name}さん を じょめいしました",7)
            pyxel.flip()
            time.sleep(1)
            return(k)
        elif (k=="No") or (k=="Cancel"):
            self.on_screen_member = None
            return(k)
        else:
            pass #未入力でなおも入力待機
                
####====================================

    def update(self):
        if self.on_screen_member:
            result = self.check_delete()
            match result:
                case "Yes":
                    vc.guild.delete(self.on_screen_member) #実際のdelete処理を
                    vc.guld.state = "guild_top"
                case "No":
                    vc.guild.state = "guild_top"
                case _:
                    pass
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
