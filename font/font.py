
import pyxel

# um10=10x10pixel, um12=12x12pyxel
um10 = pyxel.Font("/home/kawabe/MEGA/python/pyxel/font/umplus_j10r.bdf")
um12 = pyxel.Font("/home/kawabe/MEGA/python/pyxel/font/umplus_j12r.bdf")

FONT_SPACING = 2
FONT10_WIDTH = 10
FONT10_HEIGHT = FONT10_WIDTH + FONT_SPACING
FONT12_WIDTH = 12
FONT12_HEIGHT = FONT12_WIDTH + FONT_SPACING

#k8l = pyxel.Font("k8x12L.bdf")
#k8s = pyxel.Font("k8x12S.bdf")
#mg = pyxel.Font("misaki_gothic.bdf")
#mg2 = pyxel.Font("misaki_gothic_2nd.bdf")
#mm = pyxel.Font("misaki_mincho.bdf")

#pyxel.text(x,y, "イヌが西むきゃ尾は東", color, um10)

####====================================

def letter_count(str):
    count = 0
    for c in str:
        if ((ord(c) >= 33) and (ord(c) <= 126)):
            count += 0.5
        else:
            count += 1
    return(count)                            

####====================================

def msg(str, x, y, c, f_size):
    if f_size == 10:
        f = um10
        sp = 2
    else:
        f = um12
        sp = 0
    pyxel.text(x*f_size, y*(f_size+sp), str, c,f)

if __name__=='__main__':
    pyxel.init(360,360)
# #    pyxel.text(0,0,'■▲♥★♤',7,um10)


    msg("1: abcdef 30/30 4",0,0,7,12)
#    for x in range(4):
    msg("戦士",5,1,7,10)
#    for x in range(20):
    msg("僧侶",5,2,7,10)
#    for x in range(24):
    msg("盗賊",5,3,7,10)
    pyxel.show()
