from Tkinter import *
import work,fetcher


def game_window(root,line,num,diff):
    root.destroy()
    root = Tk(None,None,line)
    top = Frame(root)
    bottom = Frame(root)
    top.pack(side = TOP)
    bottom.pack(side = BOTTOM,fill = BOTH,expand= True)
    url = fetcher.get_link(num,diff)
    img = work.maketk(url)
    label = Label(root, image=img)
    label.pack(in_=top, side = LEFT)
    for i in range(num):
        button = work.answerbuttn(root,url[2],url[0][i],line,num,diff)
        button.pack(in_=top,side=TOP)

    root.mainloop()
