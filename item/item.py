#sys.path.append("/home/kawabe/MEGA/python/pyxel/dungeon")

import sys
import os
import csv
from dice import dice
from var_and_const import var_and_const as vc

####====================================

ITEM_CSV_FILE = "/home/kawabe/python/pyxel/pyxel-dungeon/item/game_item.csv"

####====================================

def convert_csv(row):
    ID      = int(row[0])
    NAME    = row[1]
    ATTACK  = dice.Dice(row[2])
    DEFENCE = dice.Dice(row[3])
    DAMAGE  = dice.Dice(row[4])
    PRICE   = int(row[5])
    return(Item(ID,NAME,ATTACK, DEFENCE, DAMAGE, PRICE))

class Item:
    def __init__(self, id, name, attack, defence, damage, price):
        self.id      = id
        self.name    = name
        self.attack  = attack
        self.defence = defence
        self.damage  = damage
        self.price   = price

####====================================

def init_item():
    db = {}
    with open(ITEM_CSV_FILE, 'r', newline='') as f:
        r = csv.reader(f)
        h=next(r)                    # headerをスキップ
        for i in r:
            item = convert_csv(i)
            db[item.id] = item
    vc.item_db = db

####====================================

if __name__=='__main__':
    db=init_item()