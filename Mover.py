import os
import shutil

def File_Mover():
    usrInpt1 = input()
    usrInpt2 = input()

    shutil.move(usrInpt1, usrInpt2)

File_Mover()