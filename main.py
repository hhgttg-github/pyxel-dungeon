import pyxel
import var_and_const as vc
import sprite        as sp
import font          as ft
import screen        as sc

import guild         as gd

import maze.maze     as mz

import party         as pt
#import player        as pl
#import castle

####====================================

class Game:
    def __init__(self):
        sc.screen_init()
#        item.init_item()
#        monster.init_monster()

        self.world = mz.World(self)
        self.scene = {}
        self.scene["guild_top"]   = gd.guild_top.Guild_Top_exe(self)
        self.scene["guild_newbi"] = gd.guild_newbi.Guild_Newbi_exe(self)
        self.scene["guild_inspect"] = gd.guild_inspect.Guild_Inspect_exe(self)
        #self.scene["castle_top"] = castle.Castle_Top(self)
        # self.scene["maze"] = maze.Maze()
        # self.scene["camp"] = player.Camp()

        self.state = "guild_top"

        self.guild = gd.guild.Guild(self)
        self.party = pt.party.Party(self)
        
        vc.guild = self.guild
        vc.party = self.party
        vc.game  = self
        
        pyxel.run(self.update, self.draw)

    def change_scene(self,state):
        self.state = state
        
#####////////////////////////////////////

    def update(self):
        self.scene[self.state].update()

    def draw(self):
        self.scene[self.state].draw()
        pyxel.flip()

#####////////////////////////////////////

if __name__=='__main__':
    Game()
    print('out of Game')