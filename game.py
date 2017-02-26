from Tkinter import *
import work,fetcher

def game_window(root,line,num):
    root.destroy()
    root = Tk(None,None,line)
    url = fetcher.get_link(num)
    img = work.maketk(url)
    label = Label(root, image=img)
    label.pack(padx=5, pady=5)
    for i in range(num):
        button = work.answerbuttn(root,url[2],url[0][i])
        button.pack()

    root.mainloop()
