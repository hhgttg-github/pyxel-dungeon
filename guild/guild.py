
import os, pickle,uuid, pyxel

import var_and_const as vc
from player import player
from screen import screen as sc

GUILD_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/guild/game_guild.pickle"

####====================================
####
#### SCREEN SECTION

LIST_GUILD_MEMBER_TOP = 1
LIST_GUILD_MENU_TOP = 12
LIST_PARTY_MEMBER_TOP = 23

GUILD_MAIN_MENU_TOP = sc.TEXT_HEIGHT-4

    
####====================================

GUILD_MAX = 20

MAIN_GUILD_KEYS = [pyxel.KEY_I,                   # INSPECT
                   pyxel.KEY_C, pyxel.KEY_D,      # CREATE, DELETE
                   pyxel.KEY_A, pyxel.KEY_R,      # ADD, REMOVE to party
                   pyxel.KEY_S, pyxel.KEY_L,      # SAVE, LOAD
                   pyxel.KEY_L, pyxel.KEY_ESCAPE] # EXIT GUILD

####====================================

def new_player():
    print("new_player")
    sc.text12(8,13,"職業は？ [ESC]=キャンセル",7)
    sc.text12(15,14,"A) 戦士",7)
    sc.text12(15,15,"B) 盗賊",7)
    sc.text12(15,16,"C) 魔法使い",7)
    keys = [pyxel.KEY_A, pyxel.KEY_B,pyxel.KEY_C, pyxel.KEY_ESCAPE]
    result = None
    while result == None:
        pyxel.flip()
        result = sc.key_input(keys)
    print(f"result={result}")
    p = player.Player()
    match result:
        case pyxel.KEY_A:
            print("job=fighter")
            return(p.create("fighter"))
        case pyxel.KEY_B:
            print("job=thief")
            return(p.create("thief"))
        case pyxel.KEY_C:
            print("job=mage")
            return(p.create("mage"))
        case _:
            return(False)


####====================================

class Guild:

    def __init__(self):
        self.members = []
        if os.path.exists(GUILD_FILE):
            self.load()
            
    def form_party(self,p):
        if self.members:
            for i in self.members:
                if i.in_party:
                    p.members.append(i)

            
    def inspect(self):
        pass
    def create_newbie(self):
        print("create_newbie")
        p = new_player()
        if p:
            self.member.append(p)
    def delete_member(self):
        pass    
    def add_fellow(self):
        print("ADD FELLOW")
    def remove_fellow(self):
        print("REMOVE FELLOW")
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

    def list_guild_members(self):
        sc.title_center(0,"ぼうけんしゃギルド",0)
        l = []
        for i in self.members:
            l.append(i.name)
        sc.draw_list(l,1,alphabet = True)
        sc.line_horizontal(12,'-')

    def draw_guild_main_menu(self):
        sc.line_horizontal(GUILD_MAIN_MENU_TOP-1,"- ")
        sc.text12( 2,GUILD_MAIN_MENU_TOP,"I)nspect,   A)dd to party,   R)emove from party",7)
        sc.text12( 2,GUILD_MAIN_MENU_TOP+1,"C)reate Newbi,   D)elete Member",7)
        sc.text12(18,GUILD_MAIN_MENU_TOP+2,"[ESC] = L)eave Guild",7)

####////////////////////////////////////

    def update(self):
        k = sc.key_input(MAIN_GUILD_KEYS)
        match k:
            case pyxel.KEY_I:
                self.inspect()
            case pyxel.KEY_A:
                self.add_fellow()
            case pyxel.KEY_R:
                self.remove_fellow()
            case pyxel.KEY_C:
                self.create_newbie()
            case pyxel.KEY_D:
                self.delete_member()
            case pyxel.KEY_S:
                self.save()
            case pyxel.KEY_L:
                self.load()
            case pyxel.KEY_ESCAPE | pyxel.KEY_L:
                vc.game.change_state("castle")

    def draw(self):
        pyxel.cls(0)
        self.list_guild_members()
        self.draw_guild_main_menu()
#        vc.party.draw()

####////////////////////////////////////

if __name__=="__main__":
    pass
#    sc.screen_init()
#    g = Guild()
#    g.draw_guild_main_menu()

#    pyxel.show()

