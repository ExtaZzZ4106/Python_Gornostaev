from tkinter import *
from tkinter import messagebox

def cliked():
    messagebox.showerror('Заголовок', 'Текст')

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
btn = Button(window, text='Клик', command=cliked)
btn.grid(column=0, row=0)
window.mainloop()
