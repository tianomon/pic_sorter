from asyncio import constants
from PIL import Image 
import tkinter as tk 
from tkinter import filedialog as fd
import os 
import pathlib


win=tk.Tk() 
win.title('pic-sorter!') 
win.geometry('300x200+100+200') 
win.resizable(False, False)
photo = tk.PhotoImage(file='logo.png')
win.iconphoto(False, photo)
win.config(bg='#a2a2d0')


count = 0 
where = ''


def callback(): #choose the folder with images
    askdir = fd.askdirectory() 
    global count
    for paths, subdirs, files in os.walk(askdir):  
        for filename in files:
            fullpath = os.path.join(paths, filename) 
            count+=1
            print(main(fullpath))

    print(count)

    if count > 0:
        return(filename)
    else:
        return()


def save(): #choose save folder
    global where
    where = fd.askdirectory()


def main(link): 
    new = link.split('.')
    if new[1]=='jpg' or new[1]=='png':
        filename = pathlib.Path(link) 
        with Image.open(filename) as img: 
            img.load()
        resolution = img.size         
        ratio = format(resolution[0], resolution[1])         
        return(moving(ratio, link))
    else: return(f'Please make sure there are no dots in the {new} file path and that the file extension is jpg or png!')


def format(horisontal, vertical): #image format definition
    if vertical > horisontal:
        return('vertical')
    elif vertical < horisontal:
        return('horizontal')
    else:
        return('square')

    
def moving(description, path): #moving files

    if description=='vertical': 
        #shutil.move(path, 'D:\new') 
        #a = os.path.basename(path)
        #filename = f'D:\new\{a}' 
        #os.rename(path, filename)
        #print(filename)
        return('vertical')
    if description=='horizontal':
        a = os.path.basename(path)
        filename = f'{where}\{a}' 
        os.rename(path, filename)
        return('horizontal')
    if description=='square':
        #a = os.path.basename(path)
        #filename = f'D:\new\{a}' #
        #os.rename(path, filename)
        return'squarelol'
    else:
        return'I can''t characterize the file!'




btn = tk.Button(text='Select the input folder', 
      command=callback)
btn.pack() 

btn1 = tk.Button(text='Select the output folder', 
      command=save)
btn1.pack() 


print(where)

win.mainloop() 

