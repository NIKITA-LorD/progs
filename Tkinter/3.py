from tkinter import *
from tkinter import ttk

i = 0

def message():
    global i
    i += 1
    label['text'] = f"{i}"


def message2():
    global i
    i += 10
    label['text'] = f"{i}"

def message3():
    global i
    i += 100
    label['text'] = f"{i}"


def message4():
    global i
    i -= 1
    label['text'] = f"{i}"

def message5():
    global i
    i -= 10
    label['text'] = f"{i}"

def message6():
    global i
    i -= 100
    label['text'] = f"{i}"

root = Tk()
root.title("Приложение")
root.geometry("250x250")



btnOne = ttk.Button(text='+1', command=message)
btnOne.pack(anchor=NW,padx=6,pady=6)

btnOne10 = ttk.Button(text='+10', command=message2)
btnOne10.pack(anchor=NW,padx=6,pady=6)

btnOne100 = ttk.Button(text='+100', command=message3)
btnOne100.pack(anchor=NW,padx=6,pady=6)

label = ttk.Label()
label.pack(anchor=NW,padx=6,pady=6)

btnTwo = ttk.Button(text='-1', command=message4)
btnTwo.pack(anchor=NW,padx=6,pady=6)

btnTwo10 = ttk.Button(text='-10', command=message5)
btnTwo10.pack(anchor=NW,padx=6,pady=6)

btnTwo100 = ttk.Button(text='-100', command=message6)
btnTwo100.pack(anchor=NW,padx=6,pady=6)
root.mainloop()