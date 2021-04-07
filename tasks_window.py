import tkinter as tk


class Tasks(tk.Frame):

    def __init__(self,root):
        super().__init__(root)
        self.init_tasks()

    def init_tasks(self):
        self.background = tk.PhotoImage(file="images/white_background.png")
        self.checkbox = tk.PhotoImage(file="images/checkbox_clear.png")
        background_label = tk.Label(image=self.background)
        background_label.place(x=0, y=0)
        checkbox_label = tk.Label(image=self.checkbox)
        # checkbox_label2 = tk.Label(image=self.checkbox)
        checkbox_label.place(x=10, y=40)
        # checkbox_label2.place(x=10, y=100)
        description_1 = tk.Label(text = 'Возьмите под охрану шлейф номер 1, прибора с \nадресом 12', font=('times', 14),bg='#ffffff',justify=tk.LEFT )
        description_1.place(x=5, y=80)
        task_1 = tk.Button(bg='#ffffff', bd=0, font=('times', 16), activebackground='#636362', text='Задание №1')
        # task_2 = tk.Button(bg='#ffffff', bd=0, font=('times', 14), activebackground='#636362', text='Задание №2')
        task_1.place(x=50, y = 35)
        # task_2.place(x=50, y=95)



if __name__ == '__main__':
    root = tk.Tk()
    app = Tasks(root)
    app.pack()
    root.title('Окно заданий')
    root.geometry('443x540+300+100')
    root.resizable(False, False)
    root.mainloop()