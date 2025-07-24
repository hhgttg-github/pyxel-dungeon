import pyxel
import var_and_const as vc
import sprite        as sp
import font          as ft
import screen        as sc
import maze
import guild
import castle
import player

####====================================

class Game:
    def __init__(self):
        sc.screen_init()
        self.detect_key = vc.Detect_key()
#        item.init_item()
#        monster.init_monster()

        self.world = maze.World()
        self.scene = {}
        self.scene["guild"] = guild.Guild()
        self.scene["guild"].game = self
        self.scene["castle"] = castle.Castle()
        self.scene["castle"].game = self
        # self.scene["maze"] = maze.Maze()
        # self.scene["camp"] = player.Camp()

        self.state = "guild"

        vc.party = player.Party()
        vc.game  = self
        # self.guild.form_party(vc.party)
        
        pyxel.run(self.update, self.draw)

#####////////////////////////////////////

    def update(self):
        self.detect_key.update()
        self.scene[self.state].update()

    def draw(self):
#        pyxel.cls(0)a
        self.scene[self.state].draw()
        pyxel.flip()

#####////////////////////////////////////

if __name__=='__main__':
    Game()
    print('out of Game')