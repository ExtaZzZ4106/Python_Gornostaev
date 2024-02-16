from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
window.mainloop()
