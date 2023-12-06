import os
import shutil
from pathlib import *
import customtkinter as ctk
import time
list_of_files = []
path = input("Enter Path ") 
tried = False

cont = ["y","yes"]
contin = input("This cannot be undone. Are you sure to proceed? (y,n) ")
if contin not in cont:
    print("Bye!")
    quit()
#I have no idea how this code works

ext = [{"exe":"EXE"},
        {"zip":"ZIP"},
        {"png":"PNG"},
        {"jpg":"JPG"},
        {"jpeg":"JPG"},
        {"wav":"WAV"},
        {"iso":"ISO"},
        {"msi": "MSI"},
        {"txt":"TXT"},
        {"lnk":"LINK"}]

def check_edit(extension):
    for foo in ext:
        if extension in foo:
            return foo[extension]
    return None
def organize():
 
    items = {}
    try:
        f = os.listdir(path)
    except:
        print("Invalid Directory!")
        return
    for item in f:
        a = os.path.isfile(f"{path}\{item}")
        if a == True:
            ls = item.rsplit('.',1)
            name = ls[0]
            extension_ = ls[-1]
            items[f"{name}"] = extension_
        else:
            pass
        
    for key,value in items.items():
        
        list_of_files.append(f"{key}{value}")
        ext = check_edit(extension=value.lower())
        if ext == None:
            ext = value.upper()
        if not os.path.exists(f"{path}\{ext}"):
            os.mkdir(f"{path}\{ext}")

            
    def move():
        for name,extension in items.items():
            ext = check_edit(extension=extension.lower())
            if ext == None:
                ext = extension.upper()
            shutil.move(f"{path}\{name}.{extension.lower()}",f"{path}\{ext}\{name}.{extension.lower()}")
    move()

for i in range(2):
    organize()
    
print(f"Succesfully organized {len(list_of_files)} files.")
time.sleep(3)
print(f"\n{list_of_files}")


