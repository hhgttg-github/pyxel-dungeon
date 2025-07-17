
import random
from dice import dice as dc
from font import font as ft
from screen import screen as sc
from var_and_const import var_and_const as vc
from maze import maze as mz
import guild,castle

####====================================

NAME_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/player/name.csv"

def random_name():
    with open(NAME_FILE,'r') as f:
        names = f.readlines()
        l_of_names = len(names)
        p = random.randint(1,100) #50%->1name, 25%->2names, rest->3names
        result = ''
        if p <= 70:
            n = 1
        elif p <= 90:
            n = 2
        else:
            n = 3
        for i in range(n):
            m = names[random.randint(1,l_of_names)]
            result += m.strip()
            result += ' '
        result = result[:-1] #最後のスペースを除いて、
        return(result[:16].title()) # 名前は最大半角16文字(全角8文字)

####====================================

PARTY_MAX = 4

####====================================
####
#### SCREEN SECTION

def job_str(j):
    match j:
        case "fighter":
            return("せんし")
        case "thief":
            return("とうぞく")
        case "mage":
            return("じゅつし")
        case _:
            return("いっぱん")

####------------------------------------

def status_str(p):
    result = ""
    if p.status:
        for i in p.status:
            match i:
                case "poison":
                    result += "毒"
                case "paralyse":
                    result += "麻"
                case "stoned":
                    result += "石"
                case "dead":
                    result = "死亡"    
                case _:
                    result += "？"
    else:
        i = p.hp / p.hp_max
        match i:
            case i if i<=0.25:
                result = "じゅうしょう"
            case i if i<=0.5:
                result = "やばい"
            case i if i<=0.9:
                result = "ちょっと"
            case _:
                result = "げんき"
    return(f"{result:<8}")

####------------------------------------

def str_for_member(p):  # p -> PLAYER CLASS
    if p:
        return(f"{p.name:<16}" + 
               f"{job_str(p.job):<5}" + 
               f"{status_str(p)}")

####------------------------------------

def list_party_members(p):
    sc.line_horizontal(sc.TEXT_BOTTOM-5,'-')
    index = 1
    for i in range(PARTY_MAX):
        if p.members[i]:
            s = f"{index:2>} {str_for_member(i)}"
        else:
            s = f"{index:2}"
        sc.text12(0, sc.PARTY_MEMBER_TOP+index, s, 7)
        index += 1

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
    def join_from_guild(self,guild):
        for i in guild.members:
            if i.in_maze:
                self.members.append(i)

#####////////////////////////////////////
    
    def update(self):
        for i in self.members:
            i.update()

#####////////////////////////////////////

    def draw(self):
        list_party_members(self.members)

####====================================

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
    def __repr__(self):
        return (f"self.in_maze = {self.in_maze!r}\n"
                f"self.name = {self.name!r}\n"
                f"self.job = {self.job!r}\n"
                f"self.status = {self.status!r}\n"
                f"self.attack = {self.attack!r}\n"
                f"self.defence = {self.defence!r}\n"
                f"self.magic = {self.magic!r}\n"
                f"self.hp = {self.hp!r}\n"
                f"self.hp_max = {self.hp_max!r}\n"
                f"self.equip = {self.equip!r}")
    def get_job(self,job):
        match job:
            case "fighter":
                self.job = job
                self.attack  = dc.Dice("1d8+0")
                self.defence = dc.Dice("1d8+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 12
                # 新しいデフォルトの装備も必要
            case "thief":
                self.job = job
                self.attack  = dc.Dice("1d6+0")
                self.defence = dc.Dice("1d8+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 8
            case "mage":
                self.job = job
                self.attack  = dc.Dice("1d4+0")
                self.defence = dc.Dice("1d4+0")
                self.magic   = dc.Dice("1d8+0")
                self.hp = self.hp_max = 6
            case _:
                self.job = None
                self.attack  = dc.Dice("1d4+0")
                self.defence = dc.Dice("1d4+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 4
        print(f"get_job({self})")

#####////////////////////////////////////

    def update(self):
        pass

#####////////////////////////////////////

class Camp:
    def __init__(self):
        pass