import shutil
import os
path=input("ENTER THE NAME OF THE DIRECTORY TO BE SOTTED.......")
list_files=os.listdir(path)
for file in list_files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else :
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)