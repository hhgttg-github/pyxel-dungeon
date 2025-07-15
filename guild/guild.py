import os, pickle,uuid, pyxel
#import player.player
from screen import screen as sc
import var_and_const as vc
import player, monster, item, maze

GUILD_FILE = "/home/kawabe/MEGA/python/pyxel/dungeon/guild/game_guild.pickle"

####====================================
####
#### SCREEN SECTION

LIST_GUILD_MEMBER_TOP = 1
LIST_GUILD_MENU_TOP = 12
LIST_PARTY_MEMBER_TOP = 23

GUILD_MAIN_MENU_TOP = sc.TEXT_HEIGHT-4

def list_guild_members(g):
    sc.title_center("ぼうけんしゃギルド")
    l = []
    for i in g.members:
        l.append(i.name)
    sc.draw_list(l,1,alphabet = True)
    sc.lin

def draw_guild_main_menu():
    sc.line_horizontal(GUILD_MAIN_MENU_TOP-1,"- ")
    sc.text12( 2,GUILD_MAIN_MENU_TOP,"I)nspect,   A)dd to party,   R)emove from party",7)
    sc.text12( 2,GUILD_MAIN_MENU_TOP+1,"C)reate Newbi,   D)elete Member",7)
    sc.text12(18,GUILD_MAIN_MENU_TOP+2,"[ESC] = L)eave Guild",7)
    
####====================================

GUILD_MAX = 20

MAIN_GUILD_KEYS = [pyxel.KEY_I,                   # INSPECT
                   pyxel.KEY_C, pyxel.KEY_D,      # CREATE, DELETE
                   pyxel.KEY_A, pyxel.KEY_R,      # ADD, REMOVE to party
                   pyxel.KEY_S, pyxel.KEY_L,      # SAVE, LOAD
                   pyxel.KEY_L, pyxel.KEY_ESCAPE] # EXIT GUILD

####====================================

def new_player():
    
    sc.text12(8,13,"あらたに参加するかたの仕事は？　（[ESC]でキャンセル）",7)
    sc.text12(15,14,"A) 戦士",7)
    sc.text12(15,15,"B) 盗賊",7)
    sc.text12(15,16,"C) 魔法使い",7)

    keys = [pyxel.KEY_A, pyxel.KEY_B,pyxel.KEY_C, pyxel.KEY_ESCAPE]
    result = sc.key_input(keys)
    p = player.Player()
    match result:
        case pyxel.KEY_A:
            return(p.create("fighter"))
        case pyxel.KEY_B:
            return(p.create("thief"))
        case pyxel.KEY_C:
            return(p.create("mage"))
        case _:
            return(False)


####====================================

class Guild:
    def __init__(self):
        if os.path.exists(GUILD_FILE):
            self.load_guild()
        else:
            self.member       = []
            self.save_guild()
    def form_party(self,p):
        if self.member:
            for i in self.member:
                if i.in_party:
                    p.member.append(i)
    def update(self):
        self.draw_guild_main_menu()
        k = sc.key_input(MAIN_GUILD_KEYS)
        match k:
            case pyxel.KEY_I:
                self.inspect()
            case pyxel.KEY_A:
                self.add()
            case pyxel.KEY_R:
                self.remove()
            case pyxel.KEY_C:
                self.create()
            case pyxel.KEY_D:
                self.delete()
            case pyxel.KEY_S():
                self.save()
            case pyxel.KEY_L():
                self.load()
            case pyxel.KEY_ESCAPE | pyxel.KEY_L:
                vc.game.change_state("castle")
            
    def inspect(self):
        pass
    def create(self):
        p = new_player()
        if p:
            self.member.append(p)
    def delete(self):
        pass    
    def add_party(self):
        pass
    def remove_party(self):
        pass
    def save_guild(self):
        with open(GUILD_FILE, 'wb') as f:
            pickle.dump(self, f)
    def load_guild(self):
        try:
            with open(GUILD_FILE, 'rb') as f:
                self = pickle.load(f)
        except FileNotFoundError:
            print(f"エラー: {GUILD_FILE}が見つかりません。")
        except Exception as e:
            print(f"データの復元中にエラーが発生しました: {e}")
    
    def draw(self):
        pyxel.cls(0)
        list_guild_members(self)
        self.draw_guild_main_menu()
        vc.party.draw()
        
if __name__=="__main__":
    sc.screen_init()
    g = Guild()
    draw_guild_main_menu()

    pyxel.show()

