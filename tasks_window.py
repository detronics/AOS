import tkinter as tk


class Tasks(tk.Frame):

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.init_tasks()

    def init_tasks(self):
        self.tasks_stat = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                           False, False, ]
        self.task_list = ['   Задание №1', '   Задание №2', '   Задание №3', '   Задание №4', '   Задание №5',
                          '   Задание №6',
                          '   Задание №7', '   Задание №8', '   Задание №9', '   Задание №10', '   Задание №11',
                          '   Задание №12',
                          '   Задание №13', '   Задание №14', '   Задание №15']
        self.description_list = ['Возьмите под охрану шлейф номер 1, прибора с адресом 12',
                                 'Снимите с охраны все шлейфы прибора с адресом 10',
                                 'Выполните сброс тревог с прибора номер 1', 'Выполнить запуст АСПТ с  номером 4',
                                 'Отмените запуск АСПТ с номером 4', 'Включите реле номер 1 прибора с адресом 44',
                                 'Выполните запрос состояния шлейфа номер 4 прибора с адресом 4',
                                 'Выполните запрос АЦП извещателя с адресом 4 прибора номер 1',
                                 'Установите время на приборе 12:00',
                                 'Установите дату  на приборе 11.08.99',
                                 'Включите тест извещателя с адресом 4 прибора номер 5',
                                 'Измените адрес пульта на 1', 'Измените пароль номер 2 на "4321"',
                                 'Установите режим работу пульта "ПИ/Резерв"',
                                 'Переведите пульт в режим программирования', ]
        self.label_list = []
        self.label_list_2 = []
        self.check_but_list = []
        self.task_numer = 0
        self.background = tk.PhotoImage(file="images/white_background.png")
        self.checkbox_clear = tk.PhotoImage(file="images/checkbox_clear.png")
        self.checkbox_checked = tk.PhotoImage(file="images/checkbox_checked.png")
        # background_label = tk.Label(self.main, image=self.background)
        # background_label.place(x=0, y=0)
        # command=lambda x=self.task_1_stat: self.hide_description() if x == True else self.bad_aswer())
        for i in self.task_list:
            self.label_list.append(tk.Label(self.main, text=i, font=('times', 14), bg='#f9966f', compound=tk.LEFT,
                                            image=self.checkbox_clear, width=443, height=33, bd=0, anchor='w'))
            self.check_but_list.append(tk.Button(self.main, text='Проверить', width=9, height=1, state=tk.DISABLED))
        for i in self.description_list:
            self.label_list_2.append(tk.Label(self.main, bg='#f9982f', font=('times', 12), compound=tk.LEFT, width=443,
                                              height=1, bd=0, anchor='w', text=i))
        for i in range(len(self.label_list)):
            self.label_list[i].pack()
            self.check_but_list[i].place(x=345, y=35 * i+2)
            # self.label_list_2[i].pack()

        self.start = tk.Button(self.main, text='Старт', command=self.start)
        self.start.place(x=0, y=540)

    def start(self):
        self.start.config(state=tk.DISABLED)
        # self.description_1.place(x=0, y=65)

    def hide_description(self):
        self.task_1.config(image=self.checkbox_checked)
        self.task_2.place(x=0, y=65)
        self.description_1.place()

    def bad_answer(self):
        message_window = tk.Toplevel()
        message_window.attributes("-topmost", True)
        message_window.geometry('150x150+800+150')
        message_window.resizable(False, False)
        message = tk.Label(message_window, text="ОШИБКА", font=('times', 18))
        ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
        message.pack()
        ok_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    root.title('Окно заданий')
    root.geometry('443x580+300+100')
    # root.resizable(False, False)
    root.mainloop()
