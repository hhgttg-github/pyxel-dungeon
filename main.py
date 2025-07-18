import pyxel
from var_and_const import var_and_const as vc
from sprite  import sprite as sp
from font    import font as ft
from screen  import screen as sc
from maze    import maze
from guild   import guild
from castle  import castle
from player  import player

####====================================

class Game:
    def __init__(self):
        sc.screen_init()

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
        # self.guild.form_party(vc.party)
        
        pyxel.run(self.update, self.draw)

#####////////////////////////////////////

    def update(self):
        self.scene[self.state].update()

    def draw(self):
#        pyxel.cls(0)
        self.scene[self.state].draw()
        pyxel.flip()

#####////////////////////////////////////

if __name__=='__main__':
    vc.game = Game()
    print('out of Game')