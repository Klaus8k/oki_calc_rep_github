from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
from CalcSubWindows import Calc_template as temp, Calc_OKI as OKI


# Основное окно программы
root = Tk()
root.geometry('400x500')
mainmenu = Menu(root)
root.config(menu=mainmenu)

# Верхняя строка меню
mainmenu.add_command(label='Печать OKI', command=OKI.OKI_window)
mainmenu.add_command(label='Офсет', command=temp.IIIIII) # IIIII - Шаблон обращения к новому окну
mainmenu.add_command(label='Наружка', command=temp.IIIIII)
mainmenu.add_command(label='Резка', command=temp.IIIIII)
mainmenu.add_command(label='Печать', command=temp.IIIIII)
mainmenu.add_command(label='Другое', command=temp.IIIIII)

root.mainloop()
