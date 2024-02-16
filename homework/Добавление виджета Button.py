from tkinter import *

window = Tk()
window.geometry('400x250')
window.title("Добро пожаловать")
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!")
btn.grid(column=1, row=0)
window.mainloop()
