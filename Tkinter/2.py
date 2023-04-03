from tkinter import *
from tkinter import ttk

i = 0

def message():
    global i
    i += 1
    label['text'] = f"{i}"


def message2():
    global i
    i -= 1
    label['text'] = f"{i}"

root = Tk()
root.title("Приложение")
root.geometry("250x150")



btnOne = ttk.Button(text='+1', command=message)
btnOne.pack(anchor=NW,padx=6,pady=6)


label = ttk.Label()
label.pack(anchor=NW,padx=6,pady=6)

btnTwo = ttk.Button(text='-1', command=message2)
btnTwo.pack(anchor=NW,padx=6,pady=6)

root.mainloop()