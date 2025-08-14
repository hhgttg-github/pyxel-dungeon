
import os, pickle,time, pyxel

import var_and_const as vc
import screen        as sc

import party         as pt
import player        as pl

import guild         as gd

####====================================
#### VARIABLES & CONSTANT

LIST_GUILD_MEMBER_TOP = 1
LIST_GUILD_MEMBER_BOTTOM = 10

PARTY_MEMBER_TOP = sc.TEXT_HEIGHT - 4

GUILD_MAX = 20

GUILD_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/guild/game_guild.pickle"

####====================================
#### FUNCTIONS

####====================================
#### CLASS

class Guild:

    def __init__(self):

        self.members = []

        self.scene = {}
        self.state = "guild_top"
        
        self.scene["guild_top"] = gd.guild_top.Guild_Top_exe()
        self.scene["guild_newbi"] = gd.guild_newbi.Guild_Newbi_exe()
        self.scene["guild_delete"] = gd.guild_delete.Guild_Delete_exe()
        self.scene["guild_inspect"] = gd.guild_inspect.Guild_Inspect_exe()
        self.scene["guild_add_party"] = gd.guild_add_party.Guild_Add_Party_exe()
        self.scene["guild_remove_party"] = gd.guild_remove_party.Guild_Remove_Party_exe()
        if os.path.exists(GUILD_FILE):
            self.load()

####====================================

    def select_guild_members(self):
        # ! 0番目を選んだとき「１」が返り値。
        # members[i] -> i+1が返り値(0を返すとFalseと区別できない)
        # それ以外は : False
        if self.members:
            k = vc.detect_key(vc.KEY_AZ)
            if k in vc.KEY_AZ:
                i = k-ord('a')
                last_of_guild = len(self.members)
                if i <= last_of_guild:
                    return(i+1)
        return(False)

####....................................

    def add_member(self,pc):
        self.members.append(pc)
            
####....................................

    def delete_member(self,pc):
        if pc in self.members:
            self.members.remove(pc)

####....................................

    def save(self):
        with open(GUILD_FILE, 'wb') as f:
            pickle.dump(self, f)

    def load(self):
        try:
            with open(GUILD_FILE, 'rb') as f:
                self = pickle.load(f)
        except FileNotFoundError:
            print(f"エラー: {GUILD_FILE}が見つかりません。")
        except Exception as e:
            print(f"データの復元中にエラーが発生しました: {e}")

####....................................

    def list_guild_members(self):
        l = []
        c_l = []
        str = ""
        for i in self.members:
            s = f"{i.name:<14}/{i.job_str()} {i.level}"
            l.append(s)
            if i.in_party:
                c_l.append(13)
            else:
                c_l.append(7)
        sc.draw_list2(l,1,alphabet = True, color_list=c_l)
        sc.line_horizontal(LIST_GUILD_MEMBER_BOTTOM+1,"- ")

####....................................

    def check_full(self):
        if len(self.members) >= GUILD_MAX:
            return(True)
        else:
            return(False)
        
    def check_empty(self):
        if len(self.members) == 0:
            return(True)
        else:
            return(False)
        
####////////////////////////////////////

    def update(self):
        self.scene[self.state].update()

####////////////////////////////////////

    def draw(self):
        self.scene[self.state].draw()

####////////////////////////////////////

# if __name__=="__main__":
#     p=player.Player()
#     print(p)
#     p.get_job("fighter")
#     print(p)