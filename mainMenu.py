from Tkinter import *
import work,game
#RUN THIS FILE TO RUN THE ACTUCAL GAME

def main():
    root = Tk(None,None," GuessTheSub") #Create the first widget for the Main menu
    text = work.texty(root,"Choose your difficulty") #Create the text header
    text.pack() # Pack the text
    work.buttoner(root) # Add the buttons to the widget

    root.mainloop()

if __name__ == '__main__':
    main()
