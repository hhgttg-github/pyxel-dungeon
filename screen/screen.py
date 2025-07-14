import pyxel,sys

#sys.path.append('/home/kawabe/MEGA/python/pyxel/dungeon/')
from font import font as ft

####====================================
####
#### KEY_INPUT

def key_input(l):
    while True:
        for k in l:
            if pyxel.btnp(k):
                return(k)

####====================================

SCREEN_OFFSET = 2
SCREEN_WIDTH  = 360 + SCREEN_OFFSET*2
SCREEN_HEIGHT = 360 + SCREEN_OFFSET*2

TEXT_WIDTH = SCREEN_WIDTH // ft.FONT12_WIDTH
TEXT_LEFT = 0
TEXT_RIGHT = TEXT_WIDTH -1
TEXT_HEIGHT = SCREEN_HEIGHT // ft.FONT12_HEIGHT #0-25, 全部で26行
TEXT_TOP = 0
TEXT_BOTTOM = TEXT_HEIGHT -1 #25

TITLE_LEFT = 0
TITLE_RIGHT = TEXT_WIDTH -1

####------------------------------------

PARTY_MEMBER_TOP = TEXT_BOTTOM - 5

####====================================

def text12(x,y,str,c):
    pyxel.text(x*ft.FONT12_WIDTH+SCREEN_OFFSET, y*ft.FONT12_HEIGHT+SCREEN_OFFSET, str ,c, ft.um12)

def text10(x,y,str,c):
    pyxel.text(x*ft.FONT10_WIDTH+SCREEN_OFFSET, y*ft.FONT10_HEIGHT+SCREEN_OFFSET, str ,c, ft.um10)

####====================================

def line_horizontal(y,ch):
    for x in range(1,TEXT_RIGHT):
        text12(x,y,ch,7)

####====================================

def top_box():
    text12(TEXT_LEFT,TEXT_TOP,"+",7)
    text12(TEXT_RIGHT,TEXT_TOP,"+",7)
    text12(TEXT_LEFT,2,"+",7)
    text12(TEXT_RIGHT,2,"+",7)

    for x in range(1,TEXT_RIGHT):
        text12(x,TEXT_TOP,"-",7)
        text12(x,2,"-",7)
    text12(0,1,"!",7)
    text12(TEXT_RIGHT,1,"!",7)

def titlebox_left(str):
    text12(2,1,str,7)

def titlebox_center(str):
    l = len(str)
    x = (TITLE_RIGHT - l) // 2
    text12(x,1,str,7)

def titlebox_right(str):
    l = len(str)
    x = TITLE_RIGHT - l
    text12(x,1,str,7)

####------------------------------------

def title_color(y,c):
    pyxel.rect(0,y*ft.FONT12_HEIGHT,SCREEN_WIDTH,ft.FONT12_HEIGHT,c)
    
def title_left(y,str,c):
    text12(0,y,str,c)

def title_center(y,str,c):
    l = len(str)
    x = (TITLE_RIGHT - l) // 2
    text12(x,y,str,c)

def title_right(y,str,c):
    l = len(str)
    x = TITLE_RIGHT - l
    text12(x,y,str,c)

####====================================

def max_of_list(l):
    result = 0
    if l:
        for i in l:
            if len(i) > result:
                result = len(i)
    return(result)

#---------------------------------------

def draw_list1(l,top,left,number=False,alphabet=False):
    y = top
    if alphabet:
        x = left
        id = 'A'
    elif number:
        x = left
        id = 1
    else:
        x = left
    for i in l:
        if alphabet:
            text12(x,y,id+" "+i,7)
            id = chr(ord(id) + 1)
        elif number:
            text12(x,y,f"{id:>{2}d} "+i,7)
            id += 1
        else:
            text12(x,y,i,7)
        y += 1

#---------------------------------------

def draw_list2(l,top,number,alphabet):
    """項目はひとつ12文字以内におさめること"""
    COL_WIDTH = TEXT_WIDTH // 2
    if alphabet:
        id = 'A'
    elif number:        
        id = 1
    x  = 1    # 左列
    left_l  = l[0:10]
    right_l = l[10:]
    y = top
    for i in left_l:
        if alphabet:
            text12(x,y,id+" "+i,7)
            id = chr(ord(id) + 1)
        elif number:
            text12(x,y,f"{id:>{2}d} "+i,7)
            id += 1
        else:
            text12(x,y,i,7)
        y += 1
    x = 16 # COL_WIDTH+1 右列
    y = top
    for i in right_l:
        if alphabet:
            text12(x,y,id+" "+i,7)
            id = chr(ord(id) + 1)
        elif number:
            text12(x,y,f"{id:>{2}d} "+i,7)
            id += 1
        else:
            text12(x,y,i,7)
        y += 1

#---------------------------------------

def draw_list(l,top=0, number=False, alphabet=False):
    """lは文字列のリスト。len(l)が10以下なら1列、20以下なら2列
    それ以上のときはエラーとなる。(半角文字問題は先送り)"""
    n = len(l)
    max_of_l = max_of_list(l)
    match n:
        case n if 1 < n <= 10:
            left_margin = (TEXT_WIDTH - max_of_l) // 2
            draw_list1(l,top,left_margin,number,alphabet)
        case n if n <= 20:
            draw_list2(l,top,number,alphabet)
        case captured:
            text12(5,15,"リストが0以下、または20を超えています",7)
    
####====================================

def draw_guild_main_menu():
    pass

####====================================

if __name__=="__main__":
    pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT)
    pyxel.cls(0)
    
    title_color(0,2)
    title_center(0,"ボルタック交易所",7)

    l = ['あああ','いいい','かきくけこ','あめんぼ','あああ','いいい','かきくけこ','あかなょん','あああ','いいい','かきくけこ','あめんぼなさかなょん']
    draw_list(l,1,alphabet=True)
    line_horizontal(11,"- ")
#    line_horizontal(20,"- ")
    title_color(20,7)
    title_left(20," #  N A M E                 J O B     S T A T U S",0)
    l = ['あかさたなはまやらわ','いきしちにひみいりい','うくすつぬふむゆるう','えけせてねへめえれえ']
    draw_list(l,21,number=True)
    # line_horizontal(23,"- ")
    # line_horizontal(24,"# ")
    # line_horizontal(25,"あ")

    pyxel.show()        
