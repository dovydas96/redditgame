from Tkinter import *
import work,fetcher

def easymode(root):
    root.destroy()
    root = Tk(None,None," EasyMode")
    url = fetcher.get_link(4)
    img = work.maketk(url)
    label = Label(root, image=img)
    label.pack(padx=5, pady=5)
    root.mainloop()

def mediummode(root):
    root.destroy()
    root = Tk(None,None," EasyMode")
    url = fetcher.get_link(10)
    img = work.maketk(url)
    for i in url[0]:
        print i
    label = Label(root, image=img)
    label.pack(padx=5, pady=5)
    root.mainloop()

def hardmode(root):
    root.destroy()
    root = Tk(None,None," Hard Mode")
    url = fetcher.get_link(15)
    img = work.maketk(url)
    label = Label(root, image=img)
    label.pack(padx=5, pady=5)
    root.mainloop()
