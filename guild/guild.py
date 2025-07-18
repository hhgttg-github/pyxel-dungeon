
import os, pickle,time, pyxel

from var_and_const import var_and_const as vc
from player import player
from screen import screen as sc

GUILD_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/guild/game_guild.pickle"

####====================================
####
#### SCREEN SECTION

LIST_GUILD_MEMBER_TOP = 1
GUILD_MAIN_MENU_TOP = 12

PARTY_MEMBER_TOP = sc.TEXT_HEIGHT-4
    
####====================================

GUILD_MAX = 20
PARTY_MAX = 4

MAIN_GUILD_KEYS = [pyxel.KEY_I,                   # INSPECT
                   pyxel.KEY_C, pyxel.KEY_D,      # CREATE, DELETE
                   pyxel.KEY_A, pyxel.KEY_R,      # ADD, REMOVE to party
                   pyxel.KEY_S, pyxel.KEY_L,      # SAVE, LOAD
                   pyxel.KEY_Q]                   # EXIT GUILD

####====================================

def new_player():
    c_top = sc.CENTER_MENU_TOP
    sc.clear_area(sc.AREA_CENTER_MENU)
    sc.text12(6,c_top,"職業は？    (Q) to Cancel",7)
    sc.text12(10,c_top+2,"A) 戦士",7)
    sc.text12(10,c_top+3,"B) 盗賊",7)
    sc.text12(10,c_top+4,"C) 魔法使い",7)
    keys = [pyxel.KEY_A, pyxel.KEY_B,pyxel.KEY_C, pyxel.KEY_Q]
    result = None
    while result == None:
        pyxel.flip()
        result = sc.key_input(keys)
    p = player.Player()
    match result:
        case pyxel.KEY_A:
            print("job=fighter")
            p.get_job("fighter")
        case pyxel.KEY_B:
            print("job=thief")
            p.get_job("thief")
        case pyxel.KEY_C:
            print("job=mage")
            p.get_job("mage")
        case pyxel.KEY_Q:
            p=None
    if p:
        p.name = player.random_name()
        return(p)
    else:
        print("RETURN WITH NONE")
        return(None)

####====================================

def add_fellow_to_party(g):
    print("add_fellow_to_party")
    sc.ERASE_CENTER_FRAME()
    print(f"player.members={vc.player.members}")
    if not(g.members):
        print("ギルドむじん")
        sc.text12(9,13,"ギルドには だれも いない．．．",7)
        pyxel.flip()
        time.sleep(2)
        sc.key_any()
        return()
    if len(vc.party.members) == PARTY_MAX:
        print("パーティまんいん")
        sc.text12(4,16,"いま、パーティは まんいん だ",7)
        time.sleep(2)
        sc.key_any()
        sc.ERASE_CENTER_FRAME()
        return()
    else:
        sc.text12(11,16,"だれ を よぶ？",7)
        last_char = pyxel.KEY_A + len(g.members) -1
        k = sc.key_AZ(last_char)
        if k:
            k=k-pyxel.KEY_A
            vc.party.members.append(g.members[k])
            g.members.pop(k)

####====================================
class Guild:

    def __init__(self):
        self.members = []
        self.game = None
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
        p = new_player()
        if p:
            self.members.append(p)

    def delete_member(self):
        pass    

    def add_fellow(self):
        print("ADD FELLOW TO PARTY in Guild()")
        add_fellow_to_party(self)

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
        sc.draw_list2(l,1,alphabet = True)
        player.list_party_members(vc.party)

    def draw_guild_main_menu(self):
        sc.line_horizontal(GUILD_MAIN_MENU_TOP-1,"- ")
        sc.text12( 2,GUILD_MAIN_MENU_TOP+1,"I)nspect,   A)dd to party,   R)emove from party",7)
        sc.text12( 2,GUILD_MAIN_MENU_TOP+3,"C)reate Newbi,   D)elete Member  (Q) to Castle",7)

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

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
            case pyxel.KEY_Q:
                print("Exit Guild")
                self.game.state = "castle"

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def draw(self):
        pyxel.cls(0)
        self.list_guild_members()
        self.draw_guild_main_menu()
#        vc.party.draw()

####////////////////////////////////////

if __name__=="__main__":
    p=player.Player()
    print(p)
    p.get_job("fighter")
    print(p)



