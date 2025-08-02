import pyxel
import var_and_const as vc
import screen        as sc

import party as pt
import player as pl

import guild as gd

####====================================
#### CONSTANT

GUILD_TOP_MENU_TOP = 12

GUILD_TOP_KEYS = [pyxel.KEY_C, pyxel.KEY_D,      # CREATE, DELETE
                  pyxel.KEY_A, pyxel.KEY_R,      # ADD, REMOVE to party
                  pyxel.KEY_S, pyxel.KEY_L,      # SAVE, LOAD
                  pyxel.KEY_Q]                   # EXIT GUILD

####====================================
#### FUNCTIONS

def draw_guild_top_menu():
    sc.line_horizontal(GUILD_TOP_MENU_TOP-1,"- ")
    sc.text12( 2,GUILD_TOP_MENU_TOP+1,"I)nspect,   A)dd to party,   R)emove from party",7)
    sc.text12( 2,GUILD_TOP_MENU_TOP+3,"C)reate Newbi,   D)elete Member  (Q) to Castle",7)

####====================================
#### CLASS

class Guild_Top_exe():

####====================================

    def __init__(self,game):
        self.game = game
    
####====================================

    def update(self):
        if pyxel.btn(pyxel.KEY_C):
            self.game.state = "guild_newbi"
        elif pyxel.btn(pyxel.KEY_Q):
            print("quit_guild_top")
            print("game.sceneは変更なし。guild_topのまま")
            #self.game.scene = "castle_top"

####====================================

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"ぼうけんしゃギルド",0)
        
        vc.guild.list_guild_members()
        vc.party.list_party_members()
        
        draw_guild_top_menu()
        pyxel.flip()
