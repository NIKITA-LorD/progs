from tkinter import *
from tkinter import ttk

def message1():
    numberOne = int(f'{entryOne.get()}')
    numberTwo = int(f'{entryTwo.get()}')
    label['text'] = f"Результат - {numberOne+numberTwo}"

def message2():
    numberOne = int(f'{entryOne.get()}')
    numberTwo = int(f'{entryTwo.get()}')
    label['text'] = f"Результат - {numberOne-numberTwo}"

def message3():
    numberOne = int(f'{entryOne.get()}')
    numberTwo = int(f'{entryTwo.get()}')
    label['text'] = f"Результат - {numberOne*numberTwo}"

def message4():
    numberOne = int(f'{entryOne.get()}')
    numberTwo = int(f'{entryTwo.get()}')
    label['text'] = f"Результат - {numberOne/numberTwo}"


root = Tk()
root.title("Приложение")
root.geometry("250x400")

entryOne = ttk.Entry()
entryOne.pack(anchor=NW,padx=6,pady=6)


entryTwo = ttk.Entry()
entryTwo.pack(anchor=NW,padx=6,pady=6)


label = ttk.Label(text='Результат')
label.pack(anchor=NW,padx=6,pady=6)

btn = ttk.Button(text='+', command=message1)
btn.pack(anchor=NW,padx=6,pady=6)

btn = ttk.Button(text='-', command=message2)
btn.pack(anchor=NW,padx=6,pady=6)

btn = ttk.Button(text='*', command=message3)
btn.pack(anchor=NW,padx=6,pady=6)

btn = ttk.Button(text='/', command=message4)
btn.pack(anchor=NW,padx=6,pady=6)

root.mainloop()