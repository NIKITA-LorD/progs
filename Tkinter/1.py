from tkinter import *
from tkinter import ttk

def message():
    label['text'] = entry.get()

root = Tk()
root.title("Приложение")
root.geometry("250x150")

entry = ttk.Entry()
entry.pack(anchor=NW,padx=6,pady=6)

btn = ttk.Button(text='Click', command=message)
btn.pack(anchor=NW,padx=6,pady=6)

label = ttk.Label()
label.pack(anchor=NW,padx=6,pady=6)

root.mainloop()
