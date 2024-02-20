from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
file = filedialog.askopenfile()
file.grid(column=0, row=0)
window.mainloop()
