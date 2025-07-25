
import os, pickle,time, pyxel

import var_and_const as vc
import screen        as sc
import player

GUILD_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/guild/game_guild.pickle"

####====================================
####
#### SCREEN SECTION

LIST_GUILD_MEMBER_TOP = 1
GUILD_MAIN_MENU_TOP = 12

PARTY_MEMBER_TOP = sc.TEXT_HEIGHT - 4
    
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
    p = None
    c_top = sc.CENTER_MENU_TOP
    sc.clear_area(sc.AREA_CENTER_MENU)
    sc.text12(6,c_top,"職業は？    (Q) to Cancel",7)
    sc.text12(10,c_top+2,"A) 戦士",7)
    sc.text12(10,c_top+3,"B) 盗賊",7)
    sc.text12(10,c_top+4,"C) 魔法使い",7)
    pyxel.flip()
    vc.game.key_list = [pyxel.KEY_A, pyxel.KEY_B,pyxel.KEY_C, pyxel.KEY_Q]
    match vc.game.key:
        case pyxel.KEY_A:
            print("job=fighter")
            p = player.Player()
            p.get_job("fighter")
            vc.game.key.reset()
        case pyxel.KEY_B:
            print("job=thief")
            p=player.Player()
            p.get_job("thief")
            vc.game.key.reset()
        case pyxel.KEY_C:
            print("job=mage")
            p=player.Player()
            p.get_job("mage")
            vc.game.key.reset()
        case pyxel.KEY_Q:
            p=None
            vc.game.key.reset()
    if p:
        p.name = player.random_name()
        return(p)
    else:
        return(None)

####====================================

def add_fellow_to_party(g):
    print("add_fellow_to_party")
    sc.ERASE_CENTER_FRAME()
    print(vc.party.members)
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
        pyxel.flip()
        last_char = pyxel.KEY_A + len(g.members) -1
        k = sc.key_AZ(last_char)
        if k:
            k=k-pyxel.KEY_A
            vc.party.members.append(g.members[k])
            g.members.pop(k)

def remove_fellow_from_party(p):
    n = len(p.members)
    sc.ERASE_CENTER_FRAME()
    if n == 0:
        sc.text12(4,16,"パーティには だれも いない",7)
        time.sleep(2)
        sc.key_any()
        sc.ERASE_CENTER_FRAME()
        
####====================================

class Guild_Top:

    def __init__(self,g):
        self.guild = g
        self.exit = False

    def update(self):
        #Guild_Topを抜けるときは、以下
        if self.exit == True:
            self.exit = False
            self.guild.state = "guild_top"
            self.game.change_scene("castle")
    
    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"ぼうけんしゃギルド",0)
        self.guild.list_guild_members()
        self.draw_guild_top_menu()
        self.party.list_party_members()

    def draw_guild_top_menu(self):
        sc.line_horizontal(GUILD_MAIN_MENU_TOP-1,"- ")
        sc.text12( 2,GUILD_MAIN_MENU_TOP+1,"I)nspect,   A)dd to party,   R)emove from party",7)
        sc.text12( 2,GUILD_MAIN_MENU_TOP+3,"C)reate Newbi,   D)elete Member  (Q) to Castle",7)

####====================================

class Guild_Newbi:

    def __init__(self,g):
        self.guild = g

    def update(self):
        pass
    
    def draw(self):
        pass

####====================================

class Guild:

    def __init__(self,g):
        self.members = []
        self.game = g
        self.party = player.Party() 

        self.state = "guild_top"
        self.scene = {}
        self.scene["guild_top"] = Guild_Top(self)
        self.scene["guild_newbi"] = Guild_Newbi(self)

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
        remove_fellow_from_party(self)

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
        l = []
        for i in self.members:
            l.append(i.name)
        sc.draw_list2(l,1,alphabet = True)
        player.list_party_members(vc.party)


####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def update(self):
        self.scene[self.state].update()
        # vc.game.detect_key.key_list = MAIN_GUILD_KEYS
        # k = vc.game.detect_key.key
        # match k:
        #     case pyxel.KEY_I:
        #         self.inspect()
        #     case pyxel.KEY_A:
        #         self.add_fellow()
        #     case pyxel.KEY_R:
        #         self.remove_fellow()
        #     case pyxel.KEY_C:
        #         self.create_newbie()
        #     case pyxel.KEY_D:
        #         self.delete_member()
        #     case pyxel.KEY_S:
        #         self.save()
        #     case pyxel.KEY_L:
        #         self.load()
        #     case pyxel.KEY_Q:
        #         print("Exit Guild")
        #         self.game.state = "castle"

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def draw(self):
        self.scene[self.state].draw()

####////////////////////////////////////

if __name__=="__main__":
    p=player.Player()
    print(p)
    p.get_job("fighter")
    print(p)



