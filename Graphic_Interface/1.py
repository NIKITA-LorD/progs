# обращаемся к "tkinter" теперь как к "tk", что-то вроде ссылки
import tkinter as tk 

# создаём главное окно под названием "win"
win = tk.Tk()
# .title - чтобы задать название окну
win.title('Моё первое графическое приложение')
# 500 на 600 - длина на ширину (между ними англ x [икс]), +100 от левого края, + 200 от правого края (в пикселях)
h = 500
w = 600
''' должно работать, но нет
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
'''
win.geometry(f"{h}x{w}+100+200") # или win.geometry(f"{h}x{w}+100+200") win.geometry("500x600+100+200")
# .resizable - для возможности изменения параметров открытгго окна ((True, True) - по умолчанию)
win.resizable(True, True)
# минимальное и максимальное значение окна
win.minsize(300, 400)
win.maxsize(700, 800)





win.mainloop()













