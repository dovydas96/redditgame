from Tkinter import *
from PIL import ImageTk,Image
from urllib2 import urlopen
import work,fetcher,io,game,mainMenu
count = 0

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
    img = img.resize((550,450),Image.ANTIALIAS)
    tkimg = ImageTk.PhotoImage(img)
    return tkimg

#Sloppy code to be fixed once the main program is functional
def but1(root):
    button = Button(root, text = "Easy",width=22, command = lambda: game.game_window(root," Easy Mode",5,"hot"))
    return button

def but2(root):
    button = Button(root, text = "Medium",width=22, command = lambda: game.game_window(root," Medium Mode",10,"hot"))
    return button

def but3(root):
    button = Button(root, text = "Hard",width=22, command = lambda: game.game_window(root," Hard Mode",10,"new"))
    return button

def buttoner(root):
    butt1 = but1(root)
    butt2 = but2(root)
    butt3 = but3(root)
    butt1.pack(padx=30)
    butt2.pack(padx=30)
    butt3.pack(padx=30)

def answerbuttn(root,correct,texty,line,num,diff):
    button = Button(root,text = texty,width = 22, command = lambda: checker(root,correct,texty,line,num,diff))
    return button

def checker(root,correctSub,subName,line,num,diff):
    global count
    if correctSub == subName:
        count = counter()
        game.game_window(root,line,num,diff)
    else:
        print correctSub
        print  count
        count = 0
        root.destroy()
        mainMenu.main()

def counter():
    global count
    count += 1
    return count
