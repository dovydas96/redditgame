from Tkinter import *
from PIL import ImageTk,Image
import work
import game

def main():
    root = Tk(None,None," GuessTheSub")
    text = work.texty(root)
    text.pack()
    work.buttoner(root)

    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()
