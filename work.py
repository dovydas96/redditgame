from Tkinter import *
from PIL import ImageTk,Image
from urllib2 import urlopen
import work,fetcher,io,game

def texty(root,line):
    text = Text(root,height=1,width=22,relief = FLAT)
    text.pack()
    text.insert(END, line)
    text.config(state = DISABLED)
    return text

def maketk(url):
    imageb = urlopen(url[1]).read()
    data = io.BytesIO(imageb)
    img = Image.open(data)
    img = img.resize((400,400),Image.ANTIALIAS)
    tkimg = ImageTk.PhotoImage(img)
    return tkimg

def but1(root):
    button = Button(root, text = "Easy",width=22, command = lambda: game.easymode(root))
    return button

def but2(root):
    button = Button(root, text = "Medium",width=22, command = lambda: game.mediummode(root))
    return button

def but3(root):
    button = Button(root, text = "Hard",width=22,command = lambda: game.hardmode(root))
    return button

def buttoner(root):
    butt1 = but1(root)
    butt2 = but2(root)
    butt3 = but3(root)
    butt1.pack(padx=30)
    butt2.pack(padx=30)
    butt3.pack(padx=30)
