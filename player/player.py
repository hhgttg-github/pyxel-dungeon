import uuid
from dice import Dice as dc
from font import font as ft
from screen import screen as sc
from var_and_const import var_and_const as vc
from maze import maze as mz
import guild,castle
￼￼
NAME_FILE = "/home/kawabe/MEGA/python/pyxel/dungeon/name.csv"

####====================================

PARTY_MAX = 4

####====================================
####
#### SCREEN SECTION

def list_party_members(p):
    pass

####====================================

class Party:
    def __init__(self):
        self.in_maze = False
        self.wxy = mz.INITIAL_WXY
        self.xy = mz.INITIAL_XY
        self.members = [None for _ in range(PARTY_MAX)]
        self.scanned = [[False for _ in range(mz.MAZE_SIZE)] for _ in range(mz.WORLD_SIZE)]
                        # self.scanned[wxy][xy]の順番
        self.gold = 0
        self.key_item = []
        self.bag = []
    def add(self,p):
        self.members.append(p)
#        self.members.append(vc.game.guild.member[id])
    def join_from_guild(self,guil):
        for i in guild.members:
            if i.in_maze:
                self.members.append(i)
    def update(self):
        for i in self.members:
            i.update()
    def draw(self):
        list_party_members(self.members)

class Player:
    def __init__(self):
        self.in_maze = False
        self.name = None
        self.job = None
        self.status = []
        self.attack = None
        self.defence = None
        self.magic = None
        self.hp = None
        self.hp_max = None
        self.equip = {"weapon":None,"armor":None,"shield":None,"others":None}
    def create(self,job):
        match job:
            case "fighter":
                self.attack  = dc.Dice("1d8+0")
                self.defence = dc.Dice("1d8+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 12
                # 新しいデフォルトの装備も必要
            case "thief":
                self.attack  = dc.Dice("1d6+0")
                self.defence = dc.Dice("1d8+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 8
            case "mage":
                self.attack  = dc.Dice("1d4+0")
                self.defence = dc.Dice("1d4+0")
                self.magic   = dc.Dice("1d8+0")
                self.hp = self.hp_max = 6
            case _:
                self.attack  = dc.Dice("1d4+0")
                self.defence = dc.Dice("1d4+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 4


    def update(self):
        pass

class Camp:
    def __init__(self):
        pass