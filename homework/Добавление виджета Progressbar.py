from tkinter import *
from tkinter.ttk import Progressbar

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
bar = Progressbar(window, length=200)
bar['value'] = 70
bar.grid(column=0, row=0)
window.mainloop()
