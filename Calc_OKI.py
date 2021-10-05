from tkinter import *
from tkinter.ttk import Combobox
import Cost_materials as cost


# Функция калькулятор
def OKI_window():
    # все расчеты
    def calc_unit():
        def print_oki_SRA3():
            toner_price_cmy = cost.Cost_oki()['Банка CMY']
            toner_price_k = cost.Cost_oki()['Банка K']
            drum_price = cost.Cost_oki()['Драм']
            fuser_price = cost.Cost_oki()['Печка']
            belt_price = cost.Cost_oki()['Ремень']

            # Коэффициент плотности носителя 80-130 - 1, 150-250 - 0.75, 300-400 - 0.5
            if cost.Cost_paper()[choise_media.get()][0] < 150:
                coefficient_media = 1
            elif cost.Cost_paper()[choise_media.get()][0] < 300:
                coefficient_media = 0.75
            else:
                coefficient_media = 0.5

            # Покрытие красок!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            coverage_cmy = 120
            coverage_k = 40

            # Общая фрмула расчета цены печати
            # цена отпечатка 2*А4 (цена тонера/ресурс * на покрытие / 5% + 4 драма + печка + ремень
            # / коэффициент плотности)

            if opt_r1.get() == 2 or opt_r1.get() == 3:
                coverage_cmy = 0
                drum_price = 0.25

            calc_result = 2 * (
                    (toner_price_k / 22000) * (coverage_k / 5) +
                    (toner_price_cmy / 22000) * (coverage_cmy / 5) +
                    (4 * drum_price / 30000 + fuser_price / 100000 +
                     belt_price / 100000) / coefficient_media)

            # обработка Радиокнопки 4+4
            if opt_r1.get() == 1 or opt_r1.get() == 3:
                calc_result *= 2
            return calc_result


        # if opt_r2.get() == 'A4':
        #     size_1_str.set('210')
        #     size_2_str.set('297')
        # elif opt_r2.get() == 'A5':
        #     size_1.insert(END, 148)
        #     size_2.insert(END, 210)
        # elif opt_r2.get() == 'A6':
        #     size_1.insert(0, 105)
        #     size_2.insert(0, 148)
        # elif opt_r2.get() == '210х98':
        #     size_1.insert(0, 210)
        #     size_2.insert(0, 98)
        # else:
        #     size1 = int(size_1_str.get())
        #     size2 = int(size_2_str.get())

        size1 = int(size_1.get())
        size2 = int(size_2.get())

        # количество изделий на листе СРА3
        def sum_on_list() -> object:

            x = size1 + 4
            y = size2 + 4
            free_space = 5  # поля
            w_list = 320 - 2 * free_space  # размеры для SRA3
            h_list = 450 - 2 * free_space
            sum_list = max((w_list // x) * (h_list // y), (w_list // y) * (h_list // x))
            return sum_list

        count_paper = int(pressrun.get()) // sum_on_list()  # количество листов в тираже

        # Словарь с параметрами
        items = {'Размеры': [size1, size2],  # Размеры
                 'Тираж:': pressrun.get(),
                 'Бумага': choise_media.get(),  # Комбобокс материалы
                 '4+4': opt_r1.get(),  # Радиокнопки опций
                 'Постобрабоотка': [post_chk1.get(), post_chk2.get()],  # Чекбоксы постобработки
                 'Количество листов': count_paper,
                 'Цена носителя': cost.Cost_paper()[choise_media.get()][1] * count_paper,  # стоимость бумаги
                 'Цена печати': count_paper * (
                             print_oki_SRA3() + cost.Cost_paper()[choise_media.get()][1])}  # себестоимость
        return items

    # Вывод словарем
    # 'Размеры': [size_1.get(), size_2.get()],  # Размеры
    # 'Тираж:': pressrun.get(),
    # 'Бумага': choise_media.get(),  # Комбобокс материалы
    # '4+4': opt_r1.get(),  # Радиокнопки опций
    # 'Постобрабоотка': [post_chk1.get(), post_chk2.get()],  # Чекбоксы постобработки
    # 'Количество листов': count_paper,
    # 'Цена носителя': cost.Cost_paper()[choise_media.get()][1] * count_paper,  # стоимость бумаги
    # 'Цена печати': count_paper * (print_oki_SRA3 + cost.Cost_paper()[choise_media.get()][1])}  # себестоимость
    def result_text():
        l_r['text'] = ''  # обнуление вывода

        res = calc_unit()['Цена печати']

        l_r['text'] = f'Себестоимость: {int(res)} руб.'

    # UI Под-окна для ввода параметров изделия и обращение к функции калькулятор
    sub_window = Tk()
    sub_window.geometry('400x350')

    # Частые форматы
    opt_r2 = StringVar(sub_window)
    rad_5 = Radiobutton(sub_window, text='A4', variable=opt_r2, value='A4')
    rad_5.grid(row=0, column=0)
    rad_6 = Radiobutton(sub_window, text='A5', variable=opt_r2, value='A5')
    rad_6.grid(row=0, column=1)
    rad_7 = Radiobutton(sub_window, text='A6', variable=opt_r2, value='A6')
    rad_7.grid(row=0, column=2)
    rad_8 = Radiobutton(sub_window, text='210х98', variable=opt_r2, value='210х98')
    rad_8.grid(row=0, column=3, pady=10)

    # Размеры изделия
    l1 = Label(sub_window, text='Ширина, мм:').grid(row=1, column=0, sticky=E, pady=10)
    size_1_str = StringVar()
    size_1 = Entry(sub_window, width=10, textvariable=size_1_str)
    size_1.grid(row=1, column=1)
    # size_1.insert(0, '0')
    l2 = Label(sub_window, text='Высота, мм:').grid(row=1, column=2, sticky=E)
    size_2_str = StringVar()
    size_2 = Entry(sub_window, width=10, textvariable=size_2_str)
    size_2.grid(row=1, column=3)
    # size_2.insert(0, '0')

    # Выбор радиокнопка цветности

    opt_r1 = IntVar(sub_window)
    rad_1 = Radiobutton(sub_window, text='4+0', variable=opt_r1, value=0)
    rad_1.grid(row=2, column=0)
    rad_2 = Radiobutton(sub_window, text='4+4', variable=opt_r1, value=1)
    rad_2.grid(row=2, column=1)
    rad_3 = Radiobutton(sub_window, text='1+0', variable=opt_r1, value=2)
    rad_3.grid(row=2, column=2)
    rad_3 = Radiobutton(sub_window, text='1+1', variable=opt_r1, value=3)
    rad_3.grid(row=2, column=3, pady=10)

    # Тираж
    l3 = Label(sub_window, text='Тираж:').grid(row=3, column=0, sticky=E)
    pressrun = Entry(sub_window, width=10)
    pressrun.grid(row=3, column=1)

    # Выбор носителя
    l3 = Label(sub_window, text='Выбери носитель:').grid(row=3, column=2, sticky=E)
    choise_media = Combobox(sub_window, text='Бумага', width=10)
    choise_media['values'] = list(cost.Cost_paper().keys())  # Значения материалов !список!
    choise_media.current(0)
    choise_media.grid(row=3, column=3, pady=10)

    # Чекбатон для выбора постобработки
    post_chk1 = IntVar(sub_window)
    chk1 = Checkbutton(sub_window, text='Постобр 1', variable=post_chk1, onvalue=1, offvalue=0)
    chk1.grid(row=4, column=0)
    post_chk2 = IntVar(sub_window)
    chk2 = Checkbutton(sub_window, text='Постобр 2', variable=post_chk2, onvalue=1, offvalue=0)
    chk2.grid(row=4, column=1, pady=10)

    # Результат
    l_r = Label(sub_window)
    l_r.grid(row=5, column=0, pady=10)

    # Кнопка вывода результата
    b1 = Button(sub_window, text='Расчет', command=result_text, width=50).grid(row=6, column=0, columnspan=4)
