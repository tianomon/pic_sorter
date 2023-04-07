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
win.config(bg='#e5e5e5')


white_theme = True
button_color = '#cddcc7'
count = 0 
where = ''



def theme_switch():
    global white_theme
    global button_color
    if white_theme == True:
        win.config(bg='#202020')
        button_color = '#292929'
        white_theme = False
    else:
        win.config(bg='#e5e5e5')
        button_color = '#cddcc7'
        white_theme = True


def choose_input_folder(): 
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


def choose_output_folder(): 
    global where
    where = fd.askdirectory()


def main(link): 
    new = link.split('.')
    if new[1]=='jpg' or new[1]=='png':
        filename = pathlib.Path(link) 
        with Image.open(filename) as img: 
            img.load()
        resolution = img.size         
        ratio = image_format_definition(resolution[0], resolution[1])         
        return(moving_files(ratio, link))
    else: return(f'Please make sure there are no dots in the {new} file path and that the file extension is jpg or png!')


def image_format_definition(horisontal, vertical):
    if vertical > horisontal:
        return('vertical')
    elif vertical < horisontal:
        return('horizontal')
    else:
        return('square')

    
def moving_files(description, path):

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
      command=choose_input_folder)
btn.pack() 

btn1 = tk.Button(text='Select the output folder', 
      command=choose_output_folder)
btn1.pack() 

btn0 = tk.Button(text='change theme', 
      bg=button_color,
      command=theme_switch)
btn0.pack() 


print(where)

win.mainloop() 

