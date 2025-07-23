
import random
import dice as dc
import font as ft
import var_and_const as vc
import screen        as sc
import maze          as mz
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

def status_str(pc):
    result = ""
    if pc.status:
        for i in pc.status:
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
        i = pc.hp / pc.hp_max
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

def str_for_member(pc):  # p -> PLAYER CLASS
    if pc:
        return(f"{pc.name:<16}" + 
               f"{job_str(pc.job):<5}" + 
               f"{status_str(pc)}")

####------------------------------------

def list_party_members(p): # p -> Party
    sc.line_horizontal(sc.TEXT_BOTTOM-5,'-')
    for i in range(1,PARTY_MAX):
        sc.text12(0,sc.PARTY_MEMBER_TOP+i,f"{i:2}",7)
    y = 0
    if p.members:
        for pc in p.members:
            s = f"{str_for_member(pc)}"
            sc.text12(3, sc.PARTY_MEMBER_TOP+y, s, 7)
            y += 1

####====================================

class Party:
    def __init__(self):
        self.in_maze = False
        self.wxy = mz.INITIAL_WXY
        self.xy = mz.INITIAL_XY
        self.members = []
        self.scanned = [[False for _ in range(mz.MAZE_SIZE)] for _ in range(mz.WORLD_SIZE)]
                        # self.scanned[wxy][xy]の順番
        self.gold = 0
        self.key_item = []
        self.bag = []

    def add(self,pc):
        self.members.append(pc)
        pc.in_party = True

    def remove(self,pc):
        pc.in_party = False
        self.members.pop(pc)

    def join_from_guild(self,guild):
        for pc in guild.members:
            if pc.in_party:
                self.members.append(pc)

#####////////////////////////////////////
    
    def update(self):
        for pc in self.members:
            pc.update()

#####////////////////////////////////////

    def draw(self):
        list_party_members(self.members)

####====================================

class Player:
    def __init__(self):
        self.in_party = False
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
        return (f"self.in_party = {self.in_party!r}\n"
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
