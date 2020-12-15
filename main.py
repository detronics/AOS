import tkinter as tk
import winsound as wn
import time


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.times = True
        self.passw_stat = False
        self.main_menu_stat = False
        self.prog_menu_stat = False
        self.buff_stat = False
        self.password_main = '1234'
        self.user_input = ''
        self.password_prog = '123456'

    def init_main(self):
        self.background = tk.PhotoImage(file="images/b_background.png")
        self.b_left = tk.PhotoImage(file='images/b_left.png')
        self.b_right = tk.PhotoImage(file='images/b_right.png')
        self.b_menu = tk.PhotoImage(file='images/b_menu.png')
        self.b_1 = tk.PhotoImage(file='images/b_1.png')
        self.b_2 = tk.PhotoImage(file='images/b_2.png')
        self.b_3 = tk.PhotoImage(file='images/b_3.png')
        self.b_4 = tk.PhotoImage(file='images/b_4.png')
        self.b_5 = tk.PhotoImage(file='images/b_5.png')
        self.b_6 = tk.PhotoImage(file='images/b_6.png')
        self.b_7 = tk.PhotoImage(file='images/b_7.png')
        self.b_8 = tk.PhotoImage(file='images/b_8.png')
        self.b_9 = tk.PhotoImage(file='images/b_9.png')
        self.b_0 = tk.PhotoImage(file='images/b_0.png')
        self.b_entr = tk.PhotoImage(file='images/b_entr.png')
        self.b_x = tk.PhotoImage(file='images/b_x.png')
        self.b_home = tk.PhotoImage(file='images/b_home.png')
        self.b_mute = tk.PhotoImage(file='images/b_mute.png')

        background_label = tk.Label(image=self.background)
        background_label.place(x=0, y=0)

        self.display_label = tk.Label(bg="darkgreen", font=('times', 20), justify=tk.LEFT, anchor='nw', )
        self.display_label.place(x=40, y=76)

        b_left = tk.Button(bg='#e6e7e4', bd=0, image=self.b_left, activebackground='#636362',
                           command=lambda but_num='left': self.click(but_num))
        b_right = tk.Button(bg='#e6e7e4', bd=0, image=self.b_right, activebackground='#636362',
                            command=lambda but_num='right': self.click(but_num))
        b_menu = tk.Button(bg='#e6e7e4', bd=0, image=self.b_menu, activebackground='#636362')
        b_1 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_1, activebackground='#636362',
                        command=lambda but_num='1': self.click(but_num), )
        b_2 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_2, activebackground='#636362',
                        command=lambda but_num='2': self.click(but_num), )
        b_3 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_3, activebackground='#636362',
                        command=lambda but_num='3': self.click(but_num))
        b_4 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_4, activebackground='#636362',
                        command=lambda but_num='4': self.click(but_num))
        b_5 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_5, activebackground='#636362', )
        b_6 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_6, activebackground='#636362', )
        b_7 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_7, activebackground='#636362', )
        b_8 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_8, activebackground='#636362', )
        b_9 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_9, activebackground='#636362', )
        b_0 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_0, activebackground='#636362', )
        b_x = tk.Button(bg='#e6e7e4', bd=0, image=self.b_x, activebackground='#636362', )
        b_entr = tk.Button(bg='#e6e7e4', bd=0, image=self.b_entr, activebackground='#636362', )
        b_home = tk.Button(bg='#e6e7e4', bd=0, image=self.b_home, activebackground='#636362')
        b_mute = tk.Button(bg='#e6e7e4', bd=0, image=self.b_mute, activebackground='#636362')

        b_left.place(x=249, y=293)
        b_right.place(x=354, y=293)
        b_menu.place(x=310, y=293)
        b_1.place(x=253, y=345)
        b_2.place(x=308, y=343)
        b_3.place(x=364, y=345)
        b_4.place(x=253, y=385)
        b_5.place(x=308, y=383)
        b_6.place(x=364, y=384)
        b_7.place(x=253, y=423)
        b_8.place(x=308, y=423)
        b_9.place(x=364, y=424)
        b_0.place(x=308, y=464)
        b_x.place(x=253, y=463)
        b_entr.place(x=358, y=464)
        b_home.place(x=200, y=442)
        b_mute.place(x=201, y=265)

    def timer(self):
        if self.times:
            time_string = time.strftime('\n%H:%M:%S')
            self.display_label.config(text=time_string)
            self.display_label.after(200, self.timer)

    def brakepas(self):
        self.times = False
        self.display_label.config(text='')

    def start_time(self):
        self.times = True
        self.timer()

    def click(self, but_num):
        wn.PlaySound("sounds/pick.wav", wn.SND_FILENAME)
        if self.times:
            self.brakepas()
        if not self.passw_stat:
            self.check_password(but_num)
        elif self.main_menu_stat:
            self.main_menu(but_num)
        elif self.prog_menu_stat:
            self.prog_menu()

    def check_password(self, but_num):
        self.user_input += but_num
        if len(self.user_input) <= 3:
            p = '*' * len(self.user_input)
            self.display_label.config(text=f'ПАРОЛЬ:{p}')
        elif self.user_input == self.password_main:
            self.passw_stat = True
            self.main_menu_stat = True
            self.user_input = ''
            self.main_menu(but_num='1')
        else:
            self.user_input = ''
            wn.PlaySound("sounds/deny.wav", wn.SND_FILENAME)
            self.display_label.config(text='НЕВЕРНЫЙ ПАРОЛЬ')
            self.start_time()

    def main_menu(self, but_num):
        menu = {1: '1ВЗЯТИЕ', 2: '2СНЯТИЕ', 3: '3СБРОС ТРЕВОГ', 4: '4СБРОС ТРЕВОГ', 5: '5ЗАПРОС', 6: '6УПРАВЛЕНИЕ',
                11: 'ВЗЯТИЕ ИНД',
                12: 'ВЗЯТИЕ ГРУППОВОЕ', 13: 'ВЗЯТИЕ ОБЩЕЕ', 111: 'НОМЕР ПРИБОРА', 121: 'НОМЕР ПРИБОРА',
                131: 'НОМЕР ПРИБОРА',
                1111: 'НОМЕР ШЛЕЙФА', 21: 'ВЗЯТИЕ ИНД', 22: 'ВЗЯТИЕ ГРУППОВОЕ', 23: 'ВЗЯТИЕ ОБЩЕЕ',
                211: 'НОМЕР ПРИБОРА',
                221: 'НОМЕР ПРИБОРА', 231: 'НОМЕР ПРИБОРА', 2111: 'НОМЕР ШЛЕЙФА'}
        if but_num >= '0' and but_num <= '9':
            self.user_input += but_num
            print(self.user_input)
            self.display_label.config(text=menu[int(self.user_input)])
        elif but_num == 'right':
            self.user_input = str(int(self.user_input) + 1)
            self.display_label.config(text=menu[int(self.user_input)])
        elif but_num == 'left':
            self.user_input = int(self.user_input) - 1

        # self.display_label.config(text=menu[int(self.user_input)])

    def buffer(self):
        pass

    def prog_menu(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('C2000M')
    root.geometry('443x540+300+100')
    root.resizable(False, False)
    app.timer()
    root.mainloop()
