
import pyxel

import random
import dice as dc
import font as ft
import var_and_const as vc
import screen        as sc
import maze          as mz
import guild,castle

####====================================
#### VARIABLES & CONSTANT

NAME_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/player/name.csv"

####====================================
#### FUNCTIONS

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
        return(result[:14].title()) # 名前は最大半角14文字(全角7文字)

####------------------------------------

def inspect_pc(pc):
    pyxel.cls(0)
    sc.title_center(0,f"{pc.name} {pc.job_str()}/ Level {pc.level}",0)
    sc.text12(3,2,f"HP {pc.hp}/{pc.hp_max}",7)

####====================================
#### CLASS

class Player:
    def __init__(self,job=None):
        self.in_party = False
        self.name = random_name()
        self.job = job
        self.level = 1
        self.status = []
        self.attack = None
        self.defence = None
        self.magic = None
        self.hp = None
        self.hp_max = None
        self.equip = {"weapon":None,"armor":None,"shield":None,"others":None}
        self.get_job()
    def __repr__(self):
        return (f"self.in_party = {self.in_party!r}\n"
                f"self.name = {self.name!r}\n"
                f"self.job = {self.job!r}\n"
                f"self.level  = {self.level!r}\n"
                f"self.status = {self.status!r}\n"
                f"self.attack = {self.attack!r}\n"
                f"self.defence = {self.defence!r}\n"
                f"self.magic = {self.magic!r}\n"
                f"self.hp = {self.hp!r}\n"
                f"self.hp_max = {self.hp_max!r}\n"
                f"self.equip = {self.equip!r}")
    def one_string(self):
        return(f"{self.name:<16}" + 
               f"{self.job_str():<5}" + 
               f"{self.status_str()}")
    
    def get_job(self):
        match self.job:
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
                self.job = None
                self.attack  = dc.Dice("1d4+0")
                self.defence = dc.Dice("1d4+0")
                self.magic   = dc.Dice("1d4+0")
                self.hp = self.hp_max = 4

####------------------------------------

    def job_str(self):
        j = self.job
        match j:
            case j if j == "fighter":
                return("せんし")
            case j if j == "thief":
                return("とうぞく")
            case j if j == "mage":
                return("じゅつし")
            case _:
                return("いっぱん")

####------------------------------------

    def status_str(self):
        result = ""
        if self.status:
            for i in self.status:
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
            i = self.hp / self.hp_max
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


#####////////////////////////////////////

    def update(self):
        pass

#####////////////////////////////////////

    def draw(self):
        pass