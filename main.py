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

        # self.world = mz.World(self)

        self.scene = {}
        self.state = "guild"

        self.scene["guild"] = vc.guild
        # self.scene["guild_top"] = gd.guild_top.Guild_Top_exe(self)

#         #self.scene["castle_top"] = castle.Castle_Top(self)
#         # self.scene["maze"] = maze.Maze()
#         # self.scene["camp"] = player.Camp()


        vc.game  = self
        self.flip_counter = 0
        self.flip_limit = 30
        pyxel.run(self.update, self.draw)

    def change_scene(self,state):
        self.state = state
        
#####////////////////////////////////////

    def update(self):
        self.scene[self.state].update()

    def draw(self):
        self.scene[self.state].draw()
        self.flip_counter += 1
        if self.flip_counter == self.flip_limit:
            pyxel.flip()
            self.flip_counter = 0

#####////////////////////////////////////

if __name__=='__main__':
    Game()
    print('out of Game')