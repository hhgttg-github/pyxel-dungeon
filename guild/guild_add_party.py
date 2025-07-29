import pyxel
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

class Guild_Add_Party.exe: #パーティに参加する

    def __init__(self,g):
        self.game = g

    def update(self):
        vc.detect_key.key_list = vc.KEY_AZ
        if vc.detect_key.key == pyxel.KEY_Q:
            self.exit = True
        else:
            n = vc.detect_key.key - pyxel.KEY_A
            pc = vc.access_nth(vc.guild.members, n)
            if pc:
                vc.guild.members.pop(n)
                pc.in_party = True
                vc.party.members.append(pc)
        if self.exit:
            self.guild.state = "guild_top"

    def draw(self):
        sc.ERASE_CENTER_FRAME()
        if vc.guild.check_empty():
            sc.text12(9,15,"ギルドには だれも いない．．．",7)
            pyxel.flip()
            time.sleep(2)
            self.exit = True
        elif vc.guild.party.check_full():
            sc.text12(9,15,"パーティが まんいん だ．．．",7)
            pyxel.flip()
            time.sleep(2)
            self.exit = True
        else:
            sc.text12(11,15,"だれ を パーティに よぶ？",7)
            pyxel.flip()            



####====================================
####------------------------------------

    def __init__(self,game):
        self.game = game
    
####====================================

    def update(self):
        pass

####====================================

    def draw(self):
        pass