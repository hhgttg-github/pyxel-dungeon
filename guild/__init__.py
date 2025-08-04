from guild.guild import Guild
from guild.guild_top import Guild_Top_exe
from guild.guild_newbi import Guild_Newbi_exe
from guild.guild_inspect import Guild_Inspect_exe

####====================================
#### CONSTANT

GUILD_TOP_MENU_TOP = 12

# GUILD_TOP_KEYS = [pyxel.KEY_C, pyxel.KEY_D,      # CREATE, DELETE
#                   pyxel.KEY_A, pyxel.KEY_R,      # ADD, REMOVE to party
#                   pyxel.KEY_S, pyxel.KEY_L,      # SAVE, LOAD
#                   pyxel.KEY_Q]                   # EXIT GUILD

####====================================
#### FUNCTIONS

def draw_guild_top_menu():
    sc.line_horizontal(GUILD_TOP_MENU_TOP-1,"- ")
    sc.text12( 2,GUILD_TOP_MENU_TOP+1,"I)nspect,   A)dd to party,   R)emove from party",7)
    sc.text12( 2,GUILD_TOP_MENU_TOP+3,"C)reate Newbi,   D)elete Member  (Q) to Castle",7)

# from.import guild_top
# from.import guild_newbi
# from.import guild_add_party
# from.import guild_inspect