from Tkinter import *

def texty(root):
    text = Text(root,height=1,width=22,relief =FLAT)
    text.pack()
    text.insert(END, "Choose your difficulty")
    text.config(state = DISABLED)
    return text

def but1(root):
    button = Button(root, text = "Easy",width=22, commmand = easy
    return button

def but2(root):
    button = Button(root, text = "Medium",width=22,command = medium
    return button

def but3(root):
    button = Button(root, text = "Hard",width=22,command = hard
    return button

def buttoner(root):
    butt1 = but1(root)
    butt2 = but2(root)
    butt3 = but3(root)
    butt1.pack(padx=30)
    butt2.pack(padx=30)
    butt3.pack(padx=30)
