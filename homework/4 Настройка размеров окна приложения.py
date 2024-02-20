from tkinter import *

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()
