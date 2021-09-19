#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

count = 0

window = Tk()
window.attributes("-fullscreen", True)
window.title("Hello world")

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

def clicked():
	global count 
	count = count + 1
	lbl.configure(text="Button was clicked " + str(count))


btn = ttk.Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()

