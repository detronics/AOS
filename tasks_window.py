import tkinter as tk


class Tasks(tk.Frame):

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.init_tasks()

    def init_tasks(self):
        self.tasks_stat = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                           False, False]
        self.tasks_names = ['   Задание №1', '   Задание №2', '   Задание №3', '   Задание №4', '   Задание №5',
                          '   Задание №6',
                          '   Задание №7', '   Задание №8', '   Задание №9', '   Задание №10', '   Задание №11',
                          '   Задание №12',
                          '   Задание №13', '   Задание №14', '   Задание №15']
        self.description_list = ['Возьмите под охрану ШС№ 1, прибора№ 12',
                                 'Снимите с охраны все ШС прибора № 10',
                                 'Выполните сброс тревог с прибора № 1', 'Выполнить запуст АСПТ № 4',
                                 'Отмените запуск АСПТ № 4', 'Включите реле №1 прибора № 44',
                                 'Выполните запрос состояния ШС №4 прибора № 4',
                                 'Выполните запрос АЦП извещателя с адресом 4 прибора № 1',
                                 'Установите время на приборе 12:00',
                                 'Установите дату  на приборе 11.08.99',
                                 'Включите тест извещателя с адресом 4 прибора №5',
                                 'Измените адрес пульта на 1', 'Измените пароль № 2 на "4321"',
                                 'Установите режим работы пульта "ПИ/Резерв"',
                                 'Переведите пульт в режим программирования', ]
        self.task_number = 0
        self.background = tk.PhotoImage(file="images/white_background.png")
        self.checkbox_clear = tk.PhotoImage(file="images/checkbox_clear.png")
        self.checkbox_checked = tk.PhotoImage(file="images/checkbox_checked.png")
        self.label_tasks = [tk.Label(self.main, text=i, font=('times', 14),  compound=tk.LEFT,
                                             image=self.checkbox_clear, width=443, height=33, bd=0, anchor='w') for i in self.tasks_names]
        self.check_but_list = [tk.Button(self.main, text='Проверить', width=9, height=1, state=tk.DISABLED,
                                                 command=self.check) for i in self.tasks_names ]
        self.label_descriptions = [tk.Label(self.main, bg='#f9982f', font=('times', 12), compound=tk.LEFT, width=443,
                                                    height=2, bd=0, anchor='w', text=i) for i in self.description_list]
        for i in range(len(self.label_tasks)):
            self.label_tasks[i].place(x=0, y=35 * i)
            self.check_but_list[i].place(x=345, y=35 * i + 5)

        self.start = tk.Button(self.main, text='Старт', command=self.start)
        self.start.place(x=0, y=565)

    def start(self):
        self.start.config(state=tk.DISABLED)
        self.task_number = 0
        for i in range(self.task_number+1, 15):
            self.label_tasks[i].place(x=0, y=(i + 1) * 35)
            self.check_but_list[i].place(x=345, y=35 * (i + 1) + 2)
        self.check_but_list[self.task_number].config(state=tk.ACTIVE)
        self.label_descriptions[self.task_number].place(x=0, y=35 * (self.task_number + 1))

    def check(self):
        if self.tasks_stat[self.task_number]:
            self.good_answer()
        else:
            self.bad_answer()

    def good_answer(self):
        if self.task_number == 14:
            self.label_tasks[self.task_number].config(image=self.checkbox_checked)
            self.check_but_list[self.task_number].config(state=tk.DISABLED)
            self.label_descriptions[self.task_number].place_forget()
            self.all_right()
        else:
            self.label_tasks[self.task_number].config(image=self.checkbox_checked)
            self.check_but_list[self.task_number].config(state=tk.DISABLED)
            self.label_descriptions[self.task_number].place_forget()
            self.task_number += 1
            self.label_tasks[self.task_number].place(x=0, y=35 * self.task_number)
            self.check_but_list[self.task_number].place(x=345, y=35 * self.task_number + 2)
            self.check_but_list[self.task_number].config(state=tk.ACTIVE)
            self.label_descriptions[self.task_number].place(x=0, y=35 * (self.task_number + 1))
            for i in range(self.task_number, len(self.tasks_stat)):
                self.tasks_stat[i] = False

    def bad_answer(self):
        message_window = tk.Toplevel()
        message_window.attributes("-topmost", True)
        message_window.geometry('+800+150')
        message_window.resizable(False, False)
        message = tk.Label(message_window, text="Задание не выполено", font=('times', 16))
        ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
        message.pack()
        ok_button.pack()

    def all_right(self):
        message_window = tk.Toplevel()
        message_window.attributes("-topmost", True)
        message_window.geometry('+800+150')
        message_window.resizable(False, False)
        message = tk.Label(message_window, text="Все задания выполнены", font=('times', 18))
        ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
        self.start.config(state=tk.ACTIVE)
        for i in self.label_tasks:
            i.config(image=self.checkbox_clear)
        message.pack()
        ok_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    root.title('Окно заданий')
    root.geometry('443x590+750+100')
    root.resizable(False, False)
    root.mainloop()
