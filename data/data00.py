import os
import subprocess,threading,socket,json
import sys
import msvcrt

def clrscr():
    subprocess.run('cls' if os.name == "nt" else 'clear',shell=True)
def int_connet():
    try:
        socket.create_connection(("8.8.8.8",53),timeout=3)
        return True
    except:
        return False

version = "0.1"
game_name = f'Tech Corp Tycoon (version:{version})'
def start():
    menu = ["Continue","New Game","Load Game","Multiplayer","Online","Delete Game","Account","Guild","Quit"]
    menu_len = len(menu)-1
    des = ["Continue game where you left","Starts a new game","Load game from save file","Play with friends ","Play online with other(and Friends) and with different enviroment","Delete save file","See your account","A guide for game how to play this","Quit this game"]
    selectmenu = 0
    while (True):
        clrscr()
        print(game_name,"\n")
        i = 0
        print("Select option : w/s - Move  f/Enter - Select")
        for x in menu:
            print(x,"<<" if i == selectmenu else "")
            i += 1
        print("\n    ",des[selectmenu])

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
        multiplayer()
    elif x == 4:
        online()
    elif x == 5:
        deletegame()
    elif x == 6:
        account()
    elif x == 7:
        guide()
    elif x == 8:
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
def online():
    inter = 0
    menu = ["Single player","Host Game","Join Game","Create Shared Game","Join Shared Game","Exit"]
    menu_no = len(menu) -1
    selmenu = 0
    while inter == 0 :
        clrscr()
        print(game_name,"\n")
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
                Mhostgame()
            elif selmenu == 1:
                Mjoingame()
            elif selmenu == 2:
                start()
        elif a in [8,27]: #esc,backspace
            start()
        if(selmenu < 0):
            selmenu = menu_no
        elif(selmenu > menu_no):
            selmenu = 0
    pass
def multiplayer():
    if int_connet():
        inter = 0
        menu = ["Host Game","Join Game","Exit"]
        menu_no = len(menu)
        selmenu = 0
        while inter == 0 :
            clrscr()
            print(game_name,"\n")
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
                    Mhostgame()
                elif selmenu == 1:
                    Mjoingame()
                elif selmenu == 2:
                    inter == 1
            elif a in [8,27]: #esc,backspace
                inter == 1
            if(selmenu < 0):
                selmenu = menu_no
            elif(selmenu > menu_no):
                selmenu = 0
    else:
        clrscr()
        print(game_name,"\n")
        print("You are offline \nEnter any key to go back")
        msvcrt.getch()
def account():
    clrscr()
    if int_connet():
        with open("data10.json","r") as file : acc = json.load(file)
        if acc["name"] :
            sel = 0
            inter = 0
            while inter == 0:
                i = 0
                for m in ["Login","Sign","Exit"]:
                    i += 1
                    print(m,"<<"if sel == i else "")
                    a = ord(msvcrt.getch())
                if a in [119,87]: #W,w
                    sel -= 1
                elif a in [115,83]: #s,S
                    sel += 1
                elif a in [102,70,13]: #F,f,enter
                    if sel == 0:
                        pass
                    elif sel == 1:
                        pass                        
                    elif sel == 2:
                        inter == 1
                elif a in [8,27]: #esc,backspace
                    inter == 1
                if(sel < 2):
                    sel = 1
                elif(sel > 2):
                    sel = 0


    else:
        print(game_name,"\n")
        print("You are offline \nEnter any key to go back")
        msvcrt.getch()

        
def guide():
    pass
def quit():
    pass

def Mhostgame():
    pass
def Mjoingame():
    pass

start()