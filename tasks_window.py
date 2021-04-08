import tkinter as tk


class Tasks(tk.Frame):

    def __init__(self,root):
        super().__init__(root)
        self.init_tasks()

    def init_tasks(self):
        self.background = tk.PhotoImage(file="images/white_background.png")
        self.checkbox_clear = tk.PhotoImage(file="images/checkbox_clear.png")
        self.checkbox_checked = tk.PhotoImage(file="images/checkbox_checked.png")
        background_label = tk.Label(image=self.background)
        background_label.place(x=0, y=0)
        self.task_1 = tk.Label(text = '   Задание №1', font=('times', 14),
                                 bg='#f99fff', compound=tk.LEFT,image = self.checkbox_clear,width=443, bd=0, anchor = 'w')
        self.task_1.place(x=0, y=35)
        self.description_1 = tk.Label(bg='#f9982f', font=('times', 12),  compound = tk.LEFT,width=443,bd=0, anchor = 'w',
                                 text='Возьмите под охрану шлейф номер 1, прибора с адресом 12')
        # self.description_1.place(x=1, y = 65)

        self.task_2 = tk.Label(text='   Задание №2', font=('times', 14),
                          bg='#f99fff', compound=tk.LEFT, image=self.checkbox_clear, width=443, bd=0, anchor='w')
        self.task_2.place(x=0, y=65)

        start = tk.Button(text = 'Start', command = self.show_description)
        start.place(x=5, y=500)
        check_success=tk.Button(text='success', command = self.hide_description)
        check_success.place(x=105, y=500)
        check_bad=tk.Button(text='bad', command = self.bad_aswer)
        check_bad.place(x=305, y=500)

    def show_description(self):
        self.task_2.place(x=0,y=85)
        self.description_1.place(x=0, y=65)

    def hide_description(self):
        self.task_1.config(image = self.checkbox_checked)
        self.task_2.place(x=0,y=65)
        self.description_1.place()

    def bad_aswer(self):
        message_window = tk.Toplevel(app)
        message_window.attributes("-topmost",True)
        message_window.geometry('150x150+450+200')
        message_window.resizable(False, False)
        message = tk.Label(message_window, text="ОШИБКА", font=('times', 18))
        ok_button = tk.Button(message_window, text="OK", command = message_window.destroy)
        message.pack()
        ok_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    app.pack()
    root.title('Окно заданий')
    root.geometry('443x540+300+100')
    root.resizable(False, False)
    root.mainloop()