import pyxel
import var_and_const as vc
import sprite        as sp
import font          as ft
import screen        as sc
import maze
import guild         as gd
import player        as pl
import guild_top
import castle

####====================================

class Game:
    def __init__(self):
        sc.screen_init()
#        item.init_item()
#        monster.init_monster()

        self.world = maze.World(self)
        self.scene = {}
        self.scene["guild_top"]   = guild_top.Guild_Top_exe(self)
        self.scene["guild_newbi"] = guild_bewbi.Guild_Newbi.exe(self)
        #self.scene["castle_top"] = castle.Castle_Top(self)
        # self.scene["maze"] = maze.Maze()
        # self.scene["camp"] = player.Camp()

        self.state = "guild_top"

        self.guild = gd.Guild(self)
        self.party = pl.Party(self)
        
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