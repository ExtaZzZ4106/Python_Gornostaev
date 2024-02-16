from tkinter import *

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)
window.mainloop()
