
import os, pickle,time, pyxel

import var_and_const as vc
import screen        as sc

import party         as pt
import player        as pl

import guild         as gd

####====================================
#### VARIABLES & CONSTANT

LIST_GUILD_MEMBER_TOP = 1
PARTY_MEMBER_TOP = sc.TEXT_HEIGHT - 4

GUILD_MAX = 20

GUILD_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/guild/game_guild.pickle"

####====================================
#### FUNCTIONS
pass

####====================================
#### CLASS

class Guild:

    def __init__(self):

        self.members = []

        self.scene = {}
        self.state = "guild_top"
        
        self.scene["guild_top"] = gd.guild_top.Guild_Top_exe()
        self.scene["guild_newbi"] = gd.guild_newbi.Guild_Newbi_exe()
        # self.scene["guild_inspect"] = gd.guild_inspect.Guild_Inspect_exe(self.game)

        if os.path.exists(GUILD_FILE):
            self.load()

####....................................

    def add_member(self,pc):
        self.members.append(pc)
            
####....................................

    def inspect(self):
        pass

####....................................

    def delete_member(self):
        pass

####....................................

    def add_fellow(self):
        pass

####....................................

    def remove_fellow(self):
        pass

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
        str = ""
        for i in self.members:
            #print(f"i={i} / i.name = {i.name} / i.job={i.job_str()}")
            s = f"{i.name:<14}/{i.job_str()} {i.level}"
            l.append(s)
        sc.draw_list2(l,1,alphabet = True)

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