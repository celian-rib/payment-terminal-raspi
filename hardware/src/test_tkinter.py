from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x200")
window.title("Hello world")

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = ttk.Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()

