from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
chk_state = BooleanVar()
chk_state.set(True)
chk_state = Checkbutton(window, text='Выбрать', var=chk_state)
chk_state.grid(column=0,row=0)
window.mainloop()
