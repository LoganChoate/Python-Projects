##this code imports the relevant libraries
import tkinter
from tkinter import *

##this code is the start of several examples of using TKinter
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry("{}x{}".format(700, 400))
        self.master.title("Learning TKinter!")





## This code is the initialization call of the main method
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
