from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.pack(expand=1, fill='both')
window.mainloop()
