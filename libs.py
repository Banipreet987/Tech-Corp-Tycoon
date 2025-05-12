import os
import subprocess
import sys
if os.name == "nt":
    import msvcrt
else:
    import tty
    import termios

def getch():
    if os.name == "nt":
        return msvcrt.getch().decode('uft-8')
    else:
        fd = sys.stdin.fileno()
        old_setting = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd , termios.TCSADRAIN , old_settings)
            return char

while(True):
    a = getch()
    print(a)