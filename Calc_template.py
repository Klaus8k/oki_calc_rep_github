from tkinter import *
from tkinter.ttk import Combobox
import Cost_materials as price



def IIIIII():
    # Функция калькулятор
    def calc_unit():


        size_unit = [size_1.get(), size_2.get()]  # размеры
        # Словарь с параметрами
        items = {'Размеры': size_unit,  # Размеры
                 'Материал': choise_media.get(),  # Комбобокс материалы
                 'Опция': opt_r1.get(),  # Радиокнопки опций
                 'Постобрабоотка': [post_chk1.get(), post_chk2.get()]}  # Чекбоксы постобработки

        return items

    def result_text():  # Вывод
        l_r['text'] = ''  # обнуление вывода
        l_r['text'] = f'Себестоимость: {calc_unit()}'

    # UI Под-окна для ввода параметров изделия и обращение к модулю просчета
    sub_window = Tk()
    sub_window.geometry('500x300')

    # Размеры изделия
    l1 = Label(sub_window, text='Ширина, мм:').pack()
    size_1 = Entry(sub_window)
    size_1.pack()

    l2 = Label(sub_window, text='Высота, мм:').pack()
    size_2 = Entry(sub_window)
    size_2.pack()

    # Выбор носителя
    l3 = Label(sub_window, text='Выбери носитель:').pack()
    choise_media = Combobox(sub_window)
    choise_media['values'] = (80, 130, 200, 350)  # Значения материалов !список!
    choise_media.current(0)
    choise_media.pack()

    # Выбор радиокнопка одно из
    opt_r1 = IntVar(sub_window)  # указать к какому экземпляру окна относится переменная!!!
    rad_1 = Radiobutton(sub_window, text='пост обр 1', variable=opt_r1, value=0)
    rad_1.pack()
    rad_2 = Radiobutton(sub_window, text='пост обр 2', variable=opt_r1, value=1)
    rad_2.pack()

    # Чекбатон для выбора постобработки
    post_chk1 = IntVar(sub_window)
    chk1 = Checkbutton(sub_window, text='Постобр 1', variable=post_chk1, onvalue=1, offvalue=0)
    chk1.pack()
    post_chk2 = IntVar(sub_window)
    chk2 = Checkbutton(sub_window, text='Постобр 2', variable=post_chk2, onvalue=1, offvalue=0)
    chk2.pack()

    # Результат
    l_r = Label(sub_window)
    l_r.pack()

    # Кнопка вывода результата
    b1 = Button(sub_window, text='Расчет', command=result_text).pack()