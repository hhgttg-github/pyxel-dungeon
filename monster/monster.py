#sys.path.append("/home/kawabe/MEGA/python/pyxel/dungeon")
import sys
import os
import csv
from dice import dice
from var_and_const import var_and_const as vc

####====================================

MONSTER_CSV_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/monster/game_monster.csv"

####====================================

def convert_csv(row):
    ID      = int(row[0])
    NAME    = row[1]
    ATTACK  = dice.Dice(row[2])
    DEFENCE = dice.Dice(row[3])
    HP_MAX  = dice.Dice(row[4])
    PRICE   = int(row[5])
    EXP     = int(row[6])
    return(Monster(ID,NAME,ATTACK, DEFENCE, HP_MAX, PRICE, EXP))

class Monster:
    def __init__(self, id, name, attack, defence, hp_max, price, exp):
        self.id      = id
        self.name    = name
        self.attack  = attack
        self.defence = defence
        self.hp_max  = hp_max
        self.hp      = None
        self.price   = price
        self.exp     = exp

####====================================

def init_monster():
    db = {}
    with open(MONSTER_CSV_FILE, 'r', newline='') as f:
        r = csv.reader(f)
        h=next(r)                    # headerをスキップ
        for i in r:
            monster = convert_csv(i)
            db[monster.id] = monster
    vc.monster_db = db

####====================================

if __name__=='__main__':
    db=init_monster()