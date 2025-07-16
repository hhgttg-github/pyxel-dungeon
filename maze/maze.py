import os, pickle, pyxel
from screen import screen as sc
from var_and_const import var_and_const as vc
import guild, player, castle

####====================================

WORLD_WH = 8
WORLD_SIZE = WORLD_WH * WORLD_WH

MAZE_WH = 16
MAZE_SIZE = MAZE_WH * MAZE_WH

TILE_PIXEL = 8
MAZE_PIXEL = TILE_PIXEL * MAZE_WH
X_OFFSET = 0
Y_OFFSET = 0

INITIAL_WXY = (0,0)
INITIAL_XY = (1,1)

#scanned = [[False for _ in range(MAZE_SIZE)] for _ in range(WORLD_SIZE)]
#scanned[MAP_index][MAZE_index] == Trueなら描画OK
#-> scanned[MAZE_INDEX]でチェックを。

####------------------------------------

PATH  = 0
WALL  = 1
DOOR_V = 10
DOOR_H = 11
DOOR_REDV = 12
DOOR_REDH = 13
#DOOR_BLUEV = 14
#DOOR_BLUEH = 15
DARK_ZONE = 50

EVENT  = 100
EVENT_A = 200
#EVENT_B = 300

TILE_TABLE = {
    (0,0):PATH,
    (1,0):WALL,
    (0,1):DOOR_H,
    (1,1):DOOR_V,
    (0,3):EVENT,
    (1,3):EVENT_A,
    (13,0):DARK_ZONE
    }

####====================================

def to_1d(x,y,s):
    return(x+y*s)

def to_2d(i,s):
    return(divmod(i, s))

####====================================

def draw_wm_tile(wx,wy,x,y):
    pyxel.bltm(x*TILE_PIXEL,y*TILE_PIXEL,0, x*MAZE_PIXEL+x*TILE_PIXEL,y*MAZE_PIXEL+y*TILE_PIXEL,8,8)
    
####====================================
    
WORLD_CSV = "/home/kawabe/MEGA/python/pyxel/dungeon/game_wordl.csv"

####====================================

class World():
    def __init__(self):
        self.mz = [Maze() for _ in range(WORLD_SIZE)]
        for wxy in range(WORLD_SIZE):
            wx, wy = to_2d(wxy, WORLD_WH)
            self.mz[wxy].wx = wx
            self.mz[wxy].wy = wy
            self.mz[wxy].read_map(wx,wy)
    def update(self):
        vc.maze = self.mz[vc.party.wxy]

####====================================

class Maze:
    def __init__(self):
        self.wx = None
        self.wy = None
        self.left_top_x = None
        self.left_top_y = None
        self.tile = [None for _ in range(MAZE_SIZE)]
        self.scanned = [False for _ in range(MAZE_SIZE)]
        self.data = [[] for _ in range(MAZE_SIZE)]
    def read_map(self,wx,wy):
        self.left_top_x = wx * (TILE_PIXEL * MAZE_WH)
        self.left_top_y = wy * (TILE_PIXEL * MAZE_WH)
        for x in range(MAZE_WH):
            for y in range(MAZE_WH):
                tile = pyxel.tilemaps[0].pget(self.left_top_x + x * TILE_PIXEL,
                                              self.left_top_y + y * TILE_PIXEL)
        self.tile[to_1d(x,y,MAZE_WH)] = TILE_TABLE.get(tile)
    def scanned_p(self,x,y):
        return(self.scanned[to_1d(x,y,MAZE_WH)])
    def draw_tile(self,x,y):
        draw_wm_tile(self.wx,self.wy,x,y)
    def draw_scanned(self):
        for y in range(MAZE_WH):
            for x in range(MAZE_WH):
                if self.scanned_p(x,y):
                    self.draw_tile(x,y)

####------------------------------------

if __name__=='__main__':
    
    pyxel.init(256,256)
    pyxel.load("dungeon.pyxres")
    pyxel.cls(0)

    w=World()
    w.mz[0].scanned[0] = True
    w.mz[0].scanned[1] = True
    w.mz[0].scanned[2] = True
    w.mz[0].scanned[8] = True
    w.mz[0].scanned[9] = True
    w.mz[0].scanned[10] = True
    w.mz[0].scanned[16] = True
    w.mz[0].scanned[17] = True
    w.mz[0].scanned[18] = True

    w.mz[0].draw_scanned()
    pyxel.show()

    data_exists = False
    print(f"ワールドファイル = {WORLD_CSV}", end = '')
    if os.path.exists(WORLD_CSV):
        print("( 作成済み )")
        file_exists = True
    else:
        print("( * 未作成 * )")
        file_exists = False
    print("マップデータ = ", end = '')
    if data_exists:
        print(" あり")
    else:
        print("なし")
    
    continue_loop = True
    while continue_loop:
        ans = input("C)sv-File M)ap-Data S)ave Q)uit")
        ans = ans[0].upper()

        match ans:
            case "C":
                print("CSV-FILE")
            case "M":
                print("MAP-DATA")
            case "Q":
                continue_loop = False
            case _:
                print("M, C, Qを入力してください")
    
    
    
    
    
"""     print(scanned)
    print(scanned[0])
    scanned[0][1] = True
    print(scanned[0])
    print(len(scanned)) #-> 64
    print(len(scanned[0])) #-> 256 """