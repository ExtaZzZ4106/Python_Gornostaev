from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)
combo.grid(column=0,row=0)
window.mainloop()
