from tkinter import *
from tkinter import ttk


def open():

    label['text'] = f"Поздравляю, ты дурачок"
def open1():

    label['text'] = f"Поздравляю, ты не дурачок"

root = Tk()
root.title("Приложение")
root.geometry("250x150")

label = ttk.Label(text='Ты дурачок?')
label.pack(anchor=NW,padx=6,pady=6)

btnOne = ttk.Button(text='да', command=open)
btnOne.pack()

btnTwo = ttk.Button(text='нет', command=open1)
btnTwo.pack()



root.mainloop()

