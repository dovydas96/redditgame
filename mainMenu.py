from Tkinter import *
import work,game

def main():
    root = Tk(None,None," GuessTheSub")
    text = work.texty(root,"Choose your difficulty")
    text.pack()
    work.buttoner(root)

    root.mainloop()

if __name__ == '__main__':
    main()
