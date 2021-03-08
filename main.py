import random
import tkinter as tk
import time
from playsound import playsound


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.times = True
        self.passw_stat = False
        self.main_menu_stat = False
        self.home_menu_stat = False
        self.menu_menu_stat = False
        self.entering_password = False
        self.passw_prog_stat = False
        self.buff_event_stat = False
        self.import_data_stat = False
        self.sound = True
        self.mistake = False
        self.test = False
        self.password_main = '1234'
        self.user_input = ''
        self.user_number = ''
        self.password_prog = '123456'
        self.aspt_stat = 0
        self.tim = ''
        self.time_date_stat = 2
        self.level = 0
        self.global_pos = 0
        self.local_pos = 0
        self.data_base = [1, ]
        self.data_base_aspt = {}
        self.buff_events = ['-НАЧАЛО БУФЕРА-',
                            {'name': 'ВКЛЮЧЕНИЕ ПУЛЬТА \nС2000М v3.02',
                             '0': f'{time.strftime("%m.%d")}   {time.strftime("%H:%M:%S")}',
                             '1': '\nПРИБОР 000', '2': 'НЕТ РАЗДЕЛА \nС2000М v3.02', '3': 'username',
                             '5': 'С2000М v3.02 \n№ ЗОНЫ: НЕ ЗАДАН',
                             '9': 'НОМЕР 1'}, '-КОНЕЦ БУФЕРА-']
        self.menu_home = ['ЖУРНАЛ СОБЫТИЙ', 'УПРАВЛЕНИЕ', 'ТЕСТ ИНДИКАЦИИ', 'ПАРОЛИ', 'НАСТРОЙКИ', ]
        self.menu_settings = ['⬍1 ВРЕМЯ И ДАТА', '⬍2 НАСТРОЙКА УСТРОЙСТВ', '⬍3 УСТАНОВКИ С2000М', '⬍4 RS-485',
                              '⬍5 RS-232', '⬍6 РЕЖИМ \nПРОГРАММИРОВАНИЯ']
        self.menu_prog_1 = {1: ['УСТАНОВКА ЧАСОВ', 'УСТАНОВКА ДАТЫ', 'КОРРЕКЦИЯ ХОДА'],
                            2: ['ПРИБОР:', ], 3: ['ЗВУКОВОЙ СИГНАЛИЗАТОР', 'ДОСТУП К ФУНКЦИЯМ', 'КОНТРОЛЬ ПИТАНИЯ',
                                                  'НАСТРОЙКА АЛГОРИТМА ПОЖАР2', 'СБРОС УСТАНОВОК НА ЗАВОДСКИЕ', ],
                            4: ['АДРЕС С2000=127', 'КОЛЬЦЕВОЙ', 'АДРЕС', 'ПЕРИОД 1', 'ПЕРИОД 2', ],
                            5: ['РЕЖИМ:', 'ЦЕНТР.УПРАВЛ.:−', 'СКОРОСТЬ: 9600 бит/с', 'ACCOUNT: 1234', 'СОБЫТИЯ LАRS', ],
                            6: ['РЕЖИМ ПРОГРАММИРОВАНИЯ']}
        self.menu_menu_list = ['УПРАВЛЕНИЕ', 'ПРОСМОТР \nПО СОСТОЯНИЯМ']
        self.menu_state = ['ТРЕВОГИ 0', 'НЕИСПРАВНОСТИ 0', 'ПОЖАРЫ 0', 'ЗАПУЩЕНО 0', 'ЕЩЕ', 'ЕЩЕ', 'ЕЩЕ']
        self.menu0 = ['⬍1 ВЗЯТИЕ', '⬍2 СНЯТИЕ', '⬍3 СБРОС ТРЕВОГ', '⬍4 УПРАВЛЕНИЕ', '⬍5 ЗАПРОС', '⬍6 СЕРВИС']
        self.menu1 = {"1": ['⬍11 ВЗЯТИЕ ИНД', '⬍12 ВЗЯТИЕ ГРУППОВОЕ', '⬍13 ВЗЯТИЕ ОБЩЕЕ'],
                      "2": ['⬍21 СНЯТИЕ ИНД', '⬍22 СНЯТИЕ ГРУППОВОЕ', '⬍23 СНЯТИЕ ОБЩЕЕ'], "3": ['НОМЕР ПРИБОРА'],
                      "4": ['⬍41 УПРАВЛЕНИЕ РЕЛЕ', '⬍42 УПРАВЛ. АСПТ', ],
                      "5": ['⬍51 ЗАПРОС ШС', '⬍52 ЗАПРОС АЦП'],
                      "6": ['⬍61 ВРЕМЯ', '⬍62 ДАТА', '⬍63 ТЕСТ ИЗВЕЩ.', '⬍64 ТЕСТ ИНДИКАЦ.', '⬍65 ПЕЧАТЬ БУФЕР',
                            '⬍66 СБРОС БУФ.ИТ']}
        self.menu2 = {'11': ['НОМЕР ПРИБОРА', 'НОМЕР ШЛЕЙФА'], '12': ['НОМЕР ПРИБОРА'], '13': ['НОМЕР ПРИБОРА'],
                      '21': ['НОМЕР ПРИБОРА', 'НОМЕР ШЛЕЙФА'], '22': ['НОМЕР ПРИБОРА'], '23': ['НОМЕР ПРИБОРА'],
                      '3': ['НОМЕР ПРИБОРА'],
                      '41': ['АДРЕС:', 'УСТРОЙСТВО:', 'ПРОГРАММА:'], '42': ['⬍УПР. АВТОМАТИКОЙ', '⬍УПРАВЛЕНИЕ ПУСКОМ'],
                      '51': ['ПРИБОР:', 'НОМЕР ШС'], '52': ['ПРИБОР:', 'НОМЕР ШС'],
                      '61': [], '62': [], '63': ['⬍ ВКЛ.ТЕСТ', '⬍ ВЫКЛ.ТЕСТ'], '64': ['НОМЕР ПРИБОРА'], '65': [],
                      '66': []}
        self.menu3 = {'421': ['АВТОМАТИКА: ВЫКЛ', 'АВТОМАТИКА: ВКЛ', '⬍ВКЛЮЧИТЬ', '⬍ВЫКЛЮЧИТЬ'],
                      '422': ['СОСТОЯНИЕ АСПТ:\n ВЗЯТ', f'СОСТОЯНИЕ АСПТ:\n {self.user_number}  З.ПУСК',
                              '⬍ОТМЕНИТЬ ПУСК', '⬍ЗАПУСТИТЬ АУП'],
                      '631': ['ПРИБОР:', '№ ИЗВЕЩАТЕЛЯ:', 'ВРЕМЯ, мин.:'], '632': ['ПРИБОР:', '№ ИЗВЕЩАТЕЛЯ:']}

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
        b_menu = tk.Button(bg='#e6e7e4', bd=0, image=self.b_menu, activebackground='#636362',
                           command=lambda but_num='menu': self.click(but_num), )
        b_1 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_1, activebackground='#636362',
                        command=lambda but_num='1': self.click(but_num), )
        b_2 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_2, activebackground='#636362',
                        command=lambda but_num='2': self.click(but_num), )
        b_3 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_3, activebackground='#636362',
                        command=lambda but_num='3': self.click(but_num))
        b_4 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_4, activebackground='#636362',
                        command=lambda but_num='4': self.click(but_num))
        b_5 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_5, activebackground='#636362',
                        command=lambda but_num='5': self.click(but_num))
        b_6 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_6, activebackground='#636362',
                        command=lambda but_num='6': self.click(but_num))
        b_7 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_7, activebackground='#636362',
                        command=lambda but_num='7': self.click(but_num))
        b_8 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_8, activebackground='#636362',
                        command=lambda but_num='8': self.click(but_num))
        b_9 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_9, activebackground='#636362',
                        command=lambda but_num='9': self.click(but_num))
        b_0 = tk.Button(bg='#e6e7e4', bd=0, image=self.b_0, activebackground='#636362',
                        command=lambda but_num='0': self.click(but_num))
        b_x = tk.Button(bg='#e6e7e4', bd=0, image=self.b_x, activebackground='#636362',
                        command=lambda but_num='x': self.click(but_num))
        b_entr = tk.Button(bg='#e6e7e4', bd=0, image=self.b_entr, activebackground='#636362',
                           command=lambda but_num='entr': self.click(but_num))
        b_home = tk.Button(bg='#e6e7e4', bd=0, image=self.b_home, activebackground='#636362',
                           command=lambda but_num='home': self.click(but_num))
        b_mute = tk.Button(bg='#e6e7e4', bd=0, image=self.b_mute, activebackground='#636362',
                           command=lambda but_num='mute': self.click(but_num))

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
        if self.times:
            self.brakepas()
        if self.menu_menu_stat:
            self.menu_menu(but_num)
        elif but_num == 'menu' and not self.menu_menu_stat:
            playsound('sounds/pick.wav')
            self.display_label.config(text='УПРАВЛЕНИЕ')
            self.menu_menu_stat = True
        elif self.home_menu_stat:
            self.menu_home_func(but_num)
        elif self.buff_event_stat:
            self.buff_event_func(but_num)
        elif but_num == 'home':
            playsound('sounds/pick.wav')
            self.home_menu_stat = True
            self.display_label.config(text='ЖУРНАЛ СОБЫТИЙ')
        elif self.user_input == '61':
            self.change_time(but_num)
        elif self.user_input == '62':
            self.change_data(but_num)
        elif self.test:
            self.test_detector(but_num)
        elif self.entering_password:
            self.check_password_prog(but_num)
        elif self.passw_prog_stat:
            self.prog_menu_func(but_num)
        elif not self.passw_stat:
            self.check_password(but_num)
        elif self.main_menu_stat:
            self.main_menu(but_num)

        elif but_num == 'mute':
            # TODO допилить звук
            self.sound = False
        else:
            self.start_time()

    def check_password(self, but_num):
        # print('check password')
        playsound('sounds/pick.wav')
        if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.user_input += but_num
            if len(self.user_input) <= 3:
                p = '*' * len(self.user_input)
                self.display_label.config(text=f'ПАРОЛЬ:{p}')
            elif self.user_input == self.password_main:
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = ''
                self.display_label.config(text='⬍1 ВЗЯТИЕ')
                self.buff_events.insert(-1, {'name': 'ИДЕНТИФИКАЦИЯ  ХО \nП000 С1 ХО                   2',
                                             '0': f'{time.strftime("%m.%d")}   {time.strftime("%H:%M:%S")}',
                                             '1': '\nПРИБОР 000', '2': 'НИДЕНТИФИКАЦИЯ  ХО \nП000 С1 ХО      2',
                                             '3': '№ПАРОЛЯ: 2',
                                             '5': 'ИДЕНТИФИКАЦИЯ  ХО \nП000 С1 ХО                   2',
                                             '9': 'НОМЕР 2'})
            else:
                self.user_input = ''
                playsound('sounds/deny.wav')
                self.display_label.config(text='НЕВЕРНЫЙ ПАРОЛЬ')
                self.times = True
                self.display_label.after(1000, self.timer)
        elif but_num == 'left' and len(self.user_input) == 0 or but_num == 'right' and len(self.user_input) == 0:
            self.start_time()
        elif len(self.user_input) >= 1 and but_num == 'x':
            self.user_input = ''
            self.display_label.config(text=f'ПАРОЛЬ:')
        elif len(self.user_input) == 0 and but_num == 'x':
            self.start_time()
        elif len(self.user_input) >= 1 and but_num == 'entr':
            self.user_input = ''
            playsound('sounds/pick.wav')
            self.display_label.config(text='НЕВЕРНЫЙ ПАРОЛЬ')
            self.times = True
            self.display_label.after(1000, self.timer)

    def check_password_prog(self, but_num):
        playsound('sounds/pick.wav')
        if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.user_input += but_num
            if len(self.user_input) <= 13:
                p = '*' * len(self.user_input)
                self.display_label.config(text=f'ПАРОЛЬ:{p}')
            else:
                self.user_input = ''
                playsound('sounds/deny.wav')
                self.display_label.config(text='НЕВЕРНЫЙ ПАРОЛЬ')
                self.entering_password = False
                self.times = True
                self.display_label.after(1000, self.timer)
        elif len(self.user_input) >= 1 and but_num == 'x':
            self.user_input = ''
            self.display_label.config(text=f'ПАРОЛЬ:')
        elif len(self.user_input) == 0 and but_num == 'x':
            self.home_menu_stat = True
            self.display_label.config(text='ЖУРНАЛ СОБЫТИЙ')
        elif but_num == 'entr':
            if self.user_input == self.password_prog:
                self.user_input = ''
                self.passw_prog_stat = True
                self.entering_password = False
                self.display_label.config(text='1 ВРЕМЯ И ДАТА')
                self.buff_events.insert(-1, {'name': 'ПРОГРАММИРОВАНИЕ   \nС2000М v3.02',
                                             '0': f'{time.strftime("%m.%d")}   {time.strftime("%H:%M:%S")}',
                                             '1': 'ПРОГРАММИРОВАНИЕ \nП000 С1 ХО', '2': 'НЕТ РАЗДЕЛА \nС2000М v3.02',
                                             '3': '№ПАРОЛЯ: НЕТ',
                                             '5': 'С2000М v3.02  \n№ЗОНЫ:  НЕ ЗАДАН',
                                             '9': 'НОМЕР 1'})
            else:
                self.user_input = ''
                playsound('sounds/deny.wav')
                self.display_label.config(text='НЕВЕРНЫЙ ПАРОЛЬ')
                self.entering_password = False
                self.times = True
                self.display_label.after(1000, self.timer)

    def main_menu(self, but_num):
        # print('main', self.user_input, self.level, self.local_pos, self.global_pos)
        playsound('sounds/pick.wav')
        if self.global_pos == 0:
            self.main_0(but_num)
        elif self.global_pos == 1:
            self.main_1(but_num)
        elif self.global_pos == 2:
            self.main_2(but_num)

    def main_0(self, but_num):
        # print('main_0', self.user_input, self.level, self.local_pos, self.global_pos)
        if but_num in ['1', '2', '4', '5', '6']:
            self.user_input += but_num
            self.local_pos = 0
            self.global_pos += 1
            self.display_label.config(text=self.menu1[but_num][self.local_pos])

        elif but_num == '3':
            self.user_input += but_num
            self.global_pos += 1
            self.local_pos = 0
            self.import_data_stat = True
            self.display_label.config(text=self.menu2[self.user_input][0])

        elif but_num == 'right':
            if self.local_pos == 5:
                self.local_pos = -1
            self.local_pos += 1
            self.display_label.config(text=self.menu0[self.local_pos])

        elif but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = 6
            self.local_pos -= 1
            self.display_label.config(text=self.menu0[self.local_pos])

        elif but_num == 'x':
            self.local_pos = 0
            self.global_pos = 0
            self.passw_stat = False
            self.main_menu_stat = False
            self.user_input = ''
            self.start_time()

        elif but_num == 'entr' and self.local_pos == 2:
            self.user_input += str(self.local_pos + 1)
            self.global_pos += 1
            self.local_pos = 0
            self.import_data_stat = True
            self.display_label.config(text=self.menu2[self.user_input][0])

        elif but_num == 'entr':
            self.global_pos += 1
            self.user_input += str(self.local_pos + 1)
            self.display_label.config(text=self.menu1[str(self.local_pos + 1)][0])
            self.local_pos = 0

    def main_1(self, but_num):
        print('main_1', self.user_input, self.level, self.local_pos, self.global_pos)
        if not self.import_data_stat:
            if '1' <= but_num <= str(len(self.menu1[self.user_input[:1]])):
                self.local_pos = 0
                self.user_input += str(but_num)
                if self.user_input == '42':
                    self.global_pos += 1
                elif self.user_input == '61':
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.time_date_stat = 0
                    self.change_time()
                elif self.user_input == '62':
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.time_date_stat = 0
                    self.change_data()
                elif self.user_input == '63':
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.test = True
                    self.display_label.config(text=self.menu2[self.user_input][0])
                else:
                    self.import_data_stat = True
                    self.display_label.config(text=self.menu2[self.user_input][0])
            elif but_num == 'right':
                if self.local_pos == len(self.menu1[self.user_input]) - 1:
                    self.local_pos = -1
                self.local_pos += 1
                self.display_label.config(text=self.menu1[self.user_input][self.local_pos])

            elif but_num == 'left':
                if self.local_pos == 0:
                    self.local_pos = len(self.menu1[self.user_input])
                self.local_pos -= 1
                self.display_label.config(text=self.menu1[self.user_input][self.local_pos])

            elif but_num == 'x':
                self.local_pos = int(self.user_input) - 1
                self.user_input = ''
                self.global_pos = 0
                self.display_label.config(text=self.menu0[self.local_pos])

            elif but_num == 'entr':
                self.user_input += str(self.local_pos + 1)
                if self.user_input in ['42']:
                    self.global_pos += 1
                    self.display_label.config(text=self.menu2[self.user_input][0])
                    self.local_pos = 0
                elif self.user_input == '61':
                    self.local_pos = 0
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.time_date_stat = 0
                    self.change_time()
                elif self.user_input == '62':
                    self.local_pos = 0
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.time_date_stat = 0
                    self.change_data()
                elif self.user_input == '63':
                    self.local_pos = 0
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.test = True
                    self.display_label.config(text=self.menu2[self.user_input][0])
                else:
                    self.import_data_stat = True
                    self.local_pos = 0
                    self.display_label.config(text=self.menu2[self.user_input][0])
        else:
            self.import_data(but_num=but_num, )

    def main_2(self, but_num=None):
        if self.level == 0:
            if not self.import_data_stat:
                if but_num == 'right':
                    if self.local_pos == len(self.menu2[self.user_input]) - 1:
                        self.local_pos = -1
                    self.local_pos += 1
                    self.display_label.config(text=self.menu2[self.user_input][self.local_pos])

                elif but_num == 'left':
                    if self.local_pos == 0:
                        self.local_pos = len(self.menu2[self.user_input])
                    self.local_pos -= 1
                    self.display_label.config(text=self.menu2[self.user_input][self.local_pos])

                elif but_num == 'x':
                    self.local_pos = 0
                    self.user_input = self.user_input[:1]
                    self.global_pos = 1
                    self.display_label.config(text=self.menu1[str(self.user_input)][0])

                elif but_num == 'entr':
                    self.user_input += str(self.local_pos + 1)
                    self.import_data_stat = True
                    self.local_pos = 0
                    self.display_label.config(text='ПРИБОР:')
            else:
                self.display_label.config(text=f'ПРИБОР: {self.user_number}')
                if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    self.user_number += but_num
                    self.display_label.config(text=f'ПРИБОР: {self.user_number}')
                elif but_num == 'x' and len(self.user_number) != 0:
                    self.user_number = ''
                    self.display_label.config(text=f'ПРИБОР: {self.user_number}')
                elif but_num == 'x' and len(self.user_number) == 0:
                    self.user_input = self.user_input[:2]
                    self.import_data_stat = False
                    self.display_label.config(text=self.menu2[self.user_input][self.local_pos])
                elif but_num == 'entr' and len(self.user_number) == 0:
                    playsound('sounds/deny.wav')
                    self.after(1, self.display_label.config(text='Неизвестная команда'))
                    self.after(500, self.main_2)
                elif but_num == 'entr' and len(self.user_number) != 0:
                    if self.user_number not in self.data_base_aspt.keys():
                        self.data_base_aspt[self.user_number] = [0, 0]
                    self.aspt_stat = 422 - int(self.user_input)
                    self.import_data_stat = False
                    self.display_label.config(
                        text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_stat]])
                    self.level = 1

        else:
            self.main_3(but_num)

    def main_3(self, but_num):
        if self.aspt_stat == 2:
            if but_num == 'entr':
                self.aspt_stat = 422 - int(self.user_input)
                self.data_base_aspt[self.user_number][self.aspt_stat] = 1
                self.import_data_stat = False
                self.display_label.config(
                    text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_stat]])
                self.local_pos = 2
            elif but_num == 'x':
                self.local_pos = 0
                self.import_data_stat = False
                self.aspt_stat = 422 - int(self.user_input)
                self.level = 1
                self.display_label.config(
                    text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_stat]])
        else:
            if not self.import_data_stat:
                if but_num == 'entr':
                    self.import_data_stat = True
                    self.display_label.config(text=self.menu3[self.user_input][2])
                    self.local_pos = 2

                elif but_num == 'x':
                    self.import_data_stat = True
                    self.local_pos = 0
                    self.level = 0
                    self.user_number = ''
                    self.display_label.config(text=f'ПРИБОР: {self.user_number}')
            else:
                if but_num == 'right':
                    if self.local_pos == 3:
                        self.local_pos = 2
                    else:
                        self.local_pos = 3
                    self.display_label.config(text=self.menu3[self.user_input][self.local_pos])

                elif but_num == 'left':
                    if self.local_pos == 2:
                        self.local_pos = 3
                    self.local_pos = 2
                    self.display_label.config(text=self.menu3[self.user_input][self.local_pos])

                elif but_num == 'x':
                    self.import_data_stat = False
                    self.local_pos = 0
                    self.display_label.config(
                        text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_stat]])

                elif but_num == 'entr':
                    self.import_data_stat = False
                    if self.user_input == '421':
                        self.data_base_aspt[self.user_number][self.aspt_stat] = -self.local_pos + 3
                        self.display_label.config(
                            text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_stat]])

                    else:
                        if self.local_pos == 2:
                            self.local_pos = 0
                            self.data_base_aspt[self.user_number][self.aspt_stat] = 0
                            self.display_label.config(text=self.menu3[self.user_input][0])
                        else:
                            self.display_label.config(text=f'ПОДТВЕРДИТЕ ПУСК\n ПРИБОР: {self.user_number} ')
                            self.aspt_stat = 2

    def menu_menu(self, but_num):
        if self.global_pos == 1:
            self.menu_menu_2(but_num)
        else:
            self.menu_menu_1(but_num)

    def menu_menu_1(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = 1
            else:
                self.local_pos -= 1
            self.display_label.config(text=self.menu_menu_list[self.local_pos])
        elif but_num == 'right':
            if self.local_pos == 1:
                self.local_pos = 0
            else:
                self.local_pos += 1
            self.display_label.config(text=self.menu_menu_list[self.local_pos])
        elif but_num == 'x':
            self.menu_menu_stat = False
            self.start_time()
        elif but_num == 'entr' and self.local_pos == 0:
            self.menu_menu_stat = False
            self.display_label.config(text=f'ПАРОЛЬ:')
        elif but_num == 'entr' and self.local_pos == 1:
            self.local_pos = 0
            self.global_pos += 1
            self.display_label.config(text=self.menu_state[self.local_pos])

    def menu_menu_2(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = len(self.menu_state) - 1
            else:
                self.local_pos -= 1
            self.display_label.config(text=self.menu_state[self.local_pos])
        elif but_num == 'right':
            if self.local_pos == len(self.menu_state) - 1:
                self.local_pos = 0
            else:
                self.local_pos += 1
            self.display_label.config(text=self.menu_state[self.local_pos])
        elif but_num == 'x':
            self.local_pos = 0
            self.global_pos = 0
            self.display_label.config(text=self.menu_menu_list[self.local_pos])

    def menu_home_func(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'right':
            if self.local_pos == 4:
                self.local_pos = -1
            self.local_pos += 1
            self.display_label.config(text=self.menu_home[self.local_pos])

        elif but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = 5
            self.local_pos -= 1
            self.display_label.config(text=self.menu_home[self.local_pos])

        elif but_num == 'x':
            self.home_menu_stat = False
            self.local_pos = 0
            self.global_pos = 0
            self.user_input = ''
            self.start_time()

        elif but_num == 'entr':
            if self.local_pos == 0:
                self.buff_event_stat = True
                self.home_menu_stat = False
                self.local_pos = len(self.buff_events) - 2
                self.display_label.config(text=self.buff_events[self.local_pos]['name'])

            elif self.local_pos == 1:
                self.local_pos = 0
                self.global_pos = 0
                self.home_menu_stat = False
                self.display_label.config(text=f'ПАРОЛЬ:')
            elif self.local_pos == 2:
                self.display_label.config(text='3')
            elif self.local_pos == 3:
                self.display_label.config(text='4')
            elif self.local_pos == 4:
                self.local_pos = 0
                self.global_pos = 0
                self.home_menu_stat = False
                self.entering_password = True
                self.display_label.config(text='ПАРОЛЬ:')

    def prog_menu_func(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'right':
            if self.local_pos == 5:
                self.local_pos = -1
            self.local_pos += 1
            self.display_label.config(text=self.menu_settings[self.local_pos])

        elif but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = 6
            self.local_pos -= 1
            self.display_label.config(text=self.menu_settings[self.local_pos])

        elif but_num == 'x':
            self.passw_prog_stat = False
            self.local_pos = 0
            self.global_pos = 0
            self.user_input = ''
            self.start_time()

        elif but_num == 'entr':
            self.global_pos += 1
            if self.local_pos == 0:
                self.display_label.config(text='1')
            elif self.local_pos == 1:
                self.local_pos = 0
            elif self.local_pos == 2:
                self.display_label.config(text='3')
            elif self.local_pos == 3:
                self.display_label.config(text='4')
            elif self.local_pos == 4:
                self.local_pos = 0
                self.global_pos = 0

    def buff_event_func(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'right':
            if self.local_pos >= len(self.buff_events) - 2:
                self.local_pos = len(self.buff_events) - 1
                self.display_label.config(text='-КОНЕЦ БУФЕРА-')
            else:
                self.local_pos += 1
                self.display_label.config(text=self.buff_events[self.local_pos]['name'])
        elif but_num == 'left':
            if self.local_pos <= 1:
                self.display_label.config(text='-НАЧАЛО БУФЕРА-')
                self.local_pos = 0
            else:
                self.local_pos -= 1
                self.display_label.config(text=self.buff_events[self.local_pos]['name'])

        elif but_num == 'x':
            self.passw_prog_stat = False
            self.buff_event_stat = False
            self.local_pos = 0
            self.global_pos = 0
            self.user_input = ''
            self.start_time()

        elif but_num in ['1', '2', '3', '5', '9', '0']:
            self.display_label.config(text=self.buff_events[self.local_pos][but_num])

    def test_indik_func(self, but_num):
        pass

    def test_detector(self, but_num=None):
        if len(self.user_input) < 3:
            playsound('sounds/pick.wav')
            if but_num == 'x':
                self.passw_stat = True
                self.main_menu_stat = True
                self.test = False
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])

            elif but_num == 'right':
                if self.local_pos == 1:
                    self.local_pos = 0
                else:
                    self.local_pos += 1
                self.display_label.config(text=self.menu2[str(self.user_input)][self.local_pos])

            elif but_num == 'left':
                if self.local_pos == 0:
                    self.local_pos = 1
                else:
                    self.local_pos -= 1
                self.display_label.config(text=self.menu2[str(self.user_input)][self.local_pos])

            elif but_num == 'entr':
                self.user_input += str(self.local_pos + 1)
                self.display_label.config(text=self.menu3[str(self.user_input)][0])

        else:
            playsound('sounds/pick.wav')
            param = self.menu3[self.user_input][self.level]
            self.display_label.config(text=f'{param} {self.user_number}')
            if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'{param} {self.user_number}')
            elif but_num == 'x' and len(self.user_number) != 0:
                self.user_number = ''
                self.display_label.config(text=f'{param} {self.user_number}')
            elif but_num == 'x' and len(self.user_number) == 0 and self.level == 0:
                self.data_base = [1]
                self.user_input = self.user_input[:2]
                self.display_label.config(text=self.menu2[str(self.user_input)][0])
            elif but_num == 'x' and self.level >= 1 and len(self.user_number) == 0:
                self.level -= 1
                param = self.menu3[self.user_input][self.level]
                self.display_label.config(text=f'{param} {self.user_number}')
            elif but_num == 'entr' and len(self.user_number) == 0:
                playsound('sounds/deny.wav')
            elif but_num == 'entr' and len(self.user_number) != 0:
                # self.data_base.insert(self.level, self.user_number)
                self.user_number = ''
                self.level += 1
                param = self.menu3[self.user_input][self.level]
                self.display_label.config(text=f'{param} {self.user_number}')

    def change_password_func(self, but_num):
        pass

    def change_time(self, but_num=None, ):
        position_list = [0, 1, 3, 4, 6, 7, -8]
        if self.sound:
            self.tim = time.strftime("%H:%M:%S")
            self.sound = False

        if but_num == 'x':
            playsound('sounds/pick.wav')
            self.passw_stat = True
            self.main_menu_stat = True
            self.user_input = self.user_input[:1]
            self.display_label.config(text=self.menu1[str(self.user_input)][0])
            self.time_date_stat = 2
            self.sound = True

        elif but_num == 'entr':
            if not self.mistake:
                playsound('sounds/pick.wav')
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.sound = True
            else:
                playsound('sounds/deny.wav')
                self.sound = True
                self.mistake = False
                self.local_pos = 0

        elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            if int(self.tim[:2]) > 23 or int(self.tim[3:5]) > 60 or int(self.tim[6:]) > 60:
                self.mistake = True
            temp = list(self.tim)
            self.tim = ''
            temp[position_list[self.local_pos]] = but_num
            self.tim = self.tim.join(temp)
            self.display_label.config(text=f'ВРЕМЯ: {self.tim}')
            self.local_pos += 1
            if self.local_pos == 6 and not self.mistake:
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.local_pos = 0
                self.sound = True
            elif self.mistake and self.local_pos == 6:
                # TODO поменять звук отказа
                playsound('sounds/deny.wav')
                self.sound = True
                self.local_pos = 0
                self.mistake = False

        elif self.time_date_stat == 0:
            self.display_label.config(text=f'ВРЕМЯ: {self.tim}')
            self.time_date_stat = 1
            self.display_label.after(400, self.change_time)

        elif self.time_date_stat == 1:
            self.time_date_stat = 0
            self.display_label.config(
                text=f'ВРЕМЯ: {self.tim[:position_list[self.local_pos]]}_{self.tim[position_list[self.local_pos] + 1:]}')
            self.display_label.after(400, self.change_time)

    def change_data(self, but_num=None):
        position_list = [0, 1, 3, 4, 6, 7, -8]
        if self.sound:
            self.tim = time.strftime("%d:%m:%y")
            self.sound = False

        if but_num == 'x':
            playsound('sounds/pick.wav')
            self.passw_stat = True
            self.main_menu_stat = True
            self.user_input = self.user_input[:1]
            self.display_label.config(text=self.menu1[str(self.user_input)][0])
            self.time_date_stat = 2
            self.sound = True

        elif but_num == 'entr':
            if not self.mistake:
                playsound('sounds/pick.wav')
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.sound = True
            else:
                playsound('sounds/deny.wav')
                self.sound = True
                self.mistake = False
                self.local_pos = 0

        elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            if int(self.tim[:2]) > 31 or int(self.tim[3:5]) > 12:
                self.mistake = True
            temp = list(self.tim)
            self.tim = ''
            temp[position_list[self.local_pos]] = but_num
            self.tim = self.tim.join(temp)
            self.display_label.config(text=f'ДАТА: {self.tim}')
            self.local_pos += 1
            if self.local_pos == 6 and not self.mistake:
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.local_pos = 0
                self.sound = True
            elif self.mistake and self.local_pos == 6:
                # TODO поменять звук отказа
                playsound('sounds/deny.wav')
                self.sound = True
                self.local_pos = 0
                self.mistake = False

        elif self.time_date_stat == 0:
            self.display_label.config(text=f'ДАТА: {self.tim}')
            self.time_date_stat = 1
            self.display_label.after(400, self.change_data)

        elif self.time_date_stat == 1:
            self.time_date_stat = 0
            self.display_label.config(
                text=f'ДАТА: {self.tim[:position_list[self.local_pos]]}_{self.tim[position_list[self.local_pos] + 1:]}')
            self.display_label.after(400, self.change_data)

    def import_data(self, but_num=None):
        # print('import data',self.user_input, self.level)
        param = self.menu2[self.user_input][self.level]
        self.display_label.config(text=f'{param} {self.user_number}')
        if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.user_number += but_num
            self.display_label.config(text=f'{param} {self.user_number}')
        elif but_num == 'x' and len(self.user_number) != 0:
            self.user_number = ''
            self.display_label.config(text=f'{param} {self.user_number}')
        elif but_num == 'x' and len(self.user_number) == 0 and self.level == 0:
            self.data_base = [1]
            self.import_data_stat = False
            self.user_input = self.user_input[:1]
            self.display_label.config(text=self.menu1[str(self.user_input)][0])
        elif but_num == 'x' and self.level >= 1 and len(self.user_number) == 0:
            self.level -= 1
            param = self.menu2[self.user_input][self.level]
            self.display_label.config(text=f'{param} {self.user_number}')
        elif but_num == 'entr' and len(self.user_number) == 0:
            playsound('sounds/deny.wav')
            self.after(10, self.display_label.config(text='Неизвестная команда'))
            self.after(500, self.import_data)
        elif but_num == 'entr' and len(self.user_number) != 0:
            self.data_base.insert(self.level, self.user_number)
            self.user_number = ''
            if len(self.menu2[self.user_input]) > 1 and self.level < 1:
                self.level += 1
                param = self.menu2[self.user_input][self.level]
                self.display_label.config(text=f'{param} {self.user_number}')
            elif len(self.menu2[self.user_input]) == 3 and self.level == 1:
                self.level += 1
                param = self.menu2[self.user_input][self.level]
                self.display_label.config(text=f'{param} {self.user_number}')
            else:
                self.show()

    def show(self):
        keyword = [
            ['ВЗЯТИЕ...', f'ВЗЯТ ШС\n   1                               00{self.data_base[0]}/00{self.data_base[1]}'],
            ['СНЯТИЕ...', f'СНЯТ ШС\n   1                               00{self.data_base[1]}/00{self.data_base[0]}'],
        ]
        mode = int(self.user_input[:1])
        print('mode', mode)
        if self.user_input == '41':
            self.after(1500, self.import_data)
        elif self.user_input == '51':
            self.display_label.config(
                text=f'⬍ 00{self.data_base[0]}/00{self.data_base[1]}:\n {random.choice(["ВЗЯТ", "СНЯТ"])}')
        #     TODO узнать куда возвращается пульт из запроса состояния
        elif self.user_input == '52':
            self.display_label.config(text=f'⬍ 00{self.data_base[0]}/00{self.data_base[1]}:                          '
            f'47\n Rшс = 4,7 кОм')
        elif mode == 3:
            self.import_data_stat = False
            self.user_input = ''
            self.local_pos = 0
            self.global_pos = 0
            self.after(250, self.display_label.config(text='⬍1 ВЗЯТИЕ'))
        else:
            if self.local_pos == 0:
                self.display_label.config(text=keyword[mode - 1][0])
                self.local_pos += 1
                self.after(500, self.show)
            elif self.local_pos == 1:
                self.display_label.config(text=keyword[mode - 1][1])
                self.buff_events.insert(-1, {'name': 'ВЗЯТ  ХО \nП000 С1 ХО                   2',
                                             '0': f'{time.strftime("%m.%d")}   {time.strftime("%H:%M:%S")}',
                                             '1': '\nПРИБОР 000', '2': 'ИДЕНТИФИКАЦИЯ  ХО \nП000 С1 ХО      2',
                                             '3': '№ПАРОЛЯ: 2',
                                             '5': 'ИДЕНТИФИКАЦИЯ  ХО \nП000 С1 ХО                   2',
                                             '9': 'НОМЕР 2'})
                self.local_pos += 1
                self.after(500, self.show)
            else:
                self.local_pos = 0
                self.after(1500, self.import_data)


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('C2000M')
    root.geometry('443x540+300+100')
    root.resizable(False, False)
    app.timer()
    root.mainloop()
