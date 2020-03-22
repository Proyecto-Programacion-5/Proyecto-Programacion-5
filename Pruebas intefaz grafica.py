from tkinter import *

root = Tk()

root.title("Buscaminas")
root.geometry("800x600")
root.config(bg = "gray")

miFrame = Frame()
miFrame.pack(side = "left", anchor = "n")
miFrame.config(bg = "light gray")
miFrame.config(width = "50", height = "50")
miFrame.config(bd = 25)
miFrame.config(relief = "groove")

root.mainloop()
