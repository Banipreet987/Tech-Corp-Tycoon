import os
import subprocess
import sys
import msvcrt

def clrscr():
    subprocess.run('cls' if os.name == "nt" else 'clear',shell=True)
    

version = "0.1"
game_name = "Tech Corp Tycoon ( version",version,")\n"
def start():
    menu = ["Continue","New Game","Load Game","Delete Game","Multiplayer","Guild","Quit"]
    menu_len = len(menu)-1
    des = ["Continue game where you left","Starts a new game","Load game from save file","Delete save file","Play multiplayer by hosting or joining other players ","A guide for game how to play this","Quit this game"]
    selectmenu = 0
    while (True):
        clrscr()
        print("Tech Corp Tycoon ( version",version,")\n")
        i = 0
        print("Select option : w/s - Move  f/Enter - Select")
        for x in menu:
            print(x,"<<" if i == selectmenu else "")
            i += 1
        print("\n   ",des[selectmenu])
        a = ord(msvcrt.getch())
        if a in [119,87]: #W,w
            selectmenu -= 1
        elif a in [115,83]: #s,S
            selectmenu += 1
        elif a in [102,70,13]: #F,f,enter
            stamenu(selectmenu)
        elif a in [8,27]: #esc,backspace
            quit()
        if(selectmenu < 0):
            selectmenu = menu_len
        elif(selectmenu > menu_len):
            selectmenu = 0
            
def stamenu(x):
    if x == 0:
        cont()
    elif x == 1:
        newgame()
    elif x == 2:
        loadgame()
    elif x == 3:
        deletegame()
    elif x == 4:
        multip()
    elif x == 5:
        guide()
    elif x == 6:
        quit()
    

def newgame():
    clrscr
    print("New Game")
    name = input("Enter Name : ")
    stagename = input("Enter Stage Name : ")
    comp_name = input("Enter Company Name : ")
    savegame = open("saves/pros","w")

    # if os.path.exists("saves/save_#1"):
    #     print("Yes")
    # else:
    #     print("No")
def cont():
    pass
def loadgame():
    
    pass
def deletegame():
    pass
def multip():
    inter = 0
    menu = ["Host Game","Save Game","Exit"]
    selmenu = 0
    while inter == 0 :
        clrscr()
        print(game_name,"/n")
        print("Select option : w/s - Move  f/Enter - Select")
        i = 0 
        for m in menu:
            print(m,"<<" if i == selmenu else "")
            i += 1
        a = ord(msvcrt.getch())
        if a in [119,87]: #W,w
            selmenu -= 1
        elif a in [115,83]: #s,S
            selmenu += 1
        elif a in [102,70,13]: #F,f,enter
            if selmenu == 0:
                hostgame()
            elif selmenu == 1:
                joingame()
            elif selmenu == 2:
                start()
        elif a in [8,27]: #esc,backspace
            start()
        if(selmenu < 0):
            selmenu = 2
        elif(selmenu > 2):
            selmenu = 0
    pass
def guide():
    pass
def quit():
    pass

def hostgame():
    pass
def joingame():
    pass

start()