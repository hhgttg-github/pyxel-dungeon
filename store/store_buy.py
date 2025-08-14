import pyxel
import var_and_const as vc
import screen        as sc

import party  as pt
import player as pl

import guild  as gd
import store

####====================================
#### CONSTANT

STORE_TOP_MENU_TOP = 12

####====================================
#### FUNCTIONS

def draw_store_buy_menu():
    sc.line_horizontal(STORE_TOP_MENU_TOP-1,"- ")
    sc.text12( 25,STORE_TOP_MENU_TOP+1,"///商品選択",7)
    sc.text12( 30,STORE_TOP_MENU_TOP+3,"X) to Leave",7)

####====================================
#### CLASS

class Store_Buy_exe():

####////////////////////////////////////

    def __init__(self):
        self.exit = False

####////////////////////////////////////

    def update(self):
        if pyxel.btnp(pyxel.KEY_X):
            vc.store.state = "store_top"

####////////////////////////////////////

    def draw(self):
        pyxel.cls(0)
        sc.title_center(0,"よろ渦オール取引所",0)

        vc.party.list_party_members()
        
        draw_store_buy_menu()
