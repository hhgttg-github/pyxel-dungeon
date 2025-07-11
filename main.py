import pyxel
from var_and_const import var_and_const as vc
from sprite import sprite as sp
from dice import dice as dc
from font import font as ft
import castle, maze, guild, player, item, monster

# from castle import castle
# from maze import maze
# from guild import guild

class Game:
    def __init__(self):
        pyxel.init(320,320,display_scale=2,fps=20)

        item.init_item()
        monster.init_monster()
        
        self.world = maze.World()
        self.guild = guild.Guild()
        self.scene = {}
        self.scene["guild"] = guild.Guild()
        self.scene["castle"] = castle.Castle()
        self.scene["maze"] = maze.Maze()
        self.scene["camp"] = player.Camp()

        self.change_state("guild")

        vc.party = player.Party()
        self.guild.form_party(vc.party)
        
        pyxel.run(self.update, self.draw)

    def change_scene(self,state):
        self.state = state
        self.scene[state].update()
        
    def update(self):
        self.scene[self.state].update()
    def draw(self):
        pyxel.cls(0)
        self.scene[self.state].draw()

if __name__=='__main__':
    vc.game = Game()