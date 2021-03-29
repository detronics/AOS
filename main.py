import random
import tkinter as tk
import time
from playsound import playsound


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.times = True
        self.programm_mode = False
        self.passw_stat = False
        self.main_menu_stat = False
        self.home_menu_stat = False
        self.menu_menu_stat = False
        self.entering_password = False
        self.passw_prog_stat = False
        self.buff_event_stat = False
        self.import_data_stat = False
        self.time_capture = True
        self.mistake = False
        self.test = False
        self.buffer_control = False
        self.crossout = False
        self.testing_ind = False
        self.choose_pass_abilities = 0
        self.change_pass = 0
        self.singh = '+'
        self.password_main = '1234'
        self.user_input = ''
        self.user_number = ''
        self.password_prog = '123456'
        self.data_range = ['31.12.99', '01.01.00', ]
        self.aspt_or_corrett_time = 0
        self.type_event_val = 0
        self.tim = ''
        self.dat = time.strftime("%d:%m:%y")
        self.corrector_time = '0.00'
        self.time_date_stat = 2
        self.temp_val = -1
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
        self.type_events = ['⬍ ВСЕ', '⬍ ПОЖАРЫ', '⬍ ТРЕВОГИ', '⬍ ПУСКИ', '⬍ ОСТАНОВЫ', '⬍ НЕИСПРАВНОСТИ',
                            '⬍ ОТКЛЮЧЕНИЯ',
                            '⬍ ВЫКЛ. АВТОМАТИК', '⬍ НОРМЫ', ]
        self.buff_settings = ['⬍ПОКАЗЫВАТЬ ВСЕ\n СОБЫТИЯ',
                              f'⬍ТИП СОБЫТИЯ:\n {self.type_events[self.type_event_val][1:]}',
                              f'⬍ДАТА:с {self.data_range[1]}\n           по {self.data_range[0]}',
                              '⬍РАЗДЕЛ:  ВСЕ', '⬍ЭЛЕМЕНТ:  ВСЕ', '⬍ПРИБОР:  ВСЕ', ]
        self.area_settings = ['empty', '⬍ВВЕСТИ НОМЕР..', '⬍ВЫБРАТЬ \nИЗ СПИСКА..', '⬍РАЗРЕШИТЬ ВСЕ']
        self.element_settings = ['⬍ВЫБРАТЬ \nИЗ СПИСКА..', '⬍РАЗРЕШИТЬ ВСЕ']
        self.device_settings = ['⬍ВВЕСТИ \nАДРЕС ПРИБОРА..', '⬍ВВЕСТИ \n№ ВХОДА/ВЫХОДА', '⬍РАЗРЕШИТЬ ВСЕ']
        self.menu_home = ['⬍ЖУРНАЛ СОБЫТИЙ', 'УПРАВЛЕНИЕ', 'ТЕСТ ИНДИКАЦИИ', 'ПАРОЛИ', 'НАСТРОЙКИ', ]
        self.password_menu = ['⬍ИЗМЕНИТЬ', '⬍УДАЛИТЬ', '⬍ДОБАВИТЬ']
        self.password_abilities = ['⬍ВЗЯТИЕ И СНЯТИЕ', '⬍ВЗЯТИЕ', '⬍ВСЕ ФУНКЦИИ']
        self.test_indik = ['⬍ С2000М', '⬍ ДРУГИЕ ПРИБОРЫ']
        self.menu_settings = ['⬍1 ВРЕМЯ И ДАТА', '⬍2 НАСТРОЙКА \nУСТРОЙСТВ', '⬍3 УСТАНОВКИ С2000М', '⬍4 RS-485',
                              '⬍5 RS-232', '⬍6 РЕЖИМ \nПРОГРАММИРОВАНИЯ']
        self.rs_485_set = [127, '-', 126, 240, 2]
        self.rs_232_mode = ['⬍ПРИНТЕР', '⬍КОМПЬЮТЕР', '⬍ПИ/РЕЗЕРВ', '⬍RS-202TD', '⬍ATS100 (LARS)', '⬍TRX-150 (CID)']
        self.rs_485_mod = ['АДРЕС С2000=', 'КОЛЬЦЕВОЙ                        : ', 'АДРЕС                     =',
                           'ПЕРИОД 1                     =', 'ПЕРИОД 2                     =']
        self.menu_prog_1 = {1: ['УСТАНОВКА ЧАСОВ', 'УСТАНОВКА ДАТЫ', 'КОРРЕКЦИЯ ХОДА'],
                            2: ['ПРИБОР:', ],
                            3: ['⬍ЗВУКОВОЙ \nСИГНАЛИЗАТОР', '⬍ДОСТУП \nК ФУНКЦИЯМ', '⬍КОНТРОЛЬ \nПИТАНИЯ',
                                '⬍КОНТРОЛЬ СВЯЗИ \nПО RS-232',
                                '⬍НАСТРОЙКА \nАЛГОРИТМА ПОЖАР2', '⬍СБРОС УСТАНОВОК \nНА ЗАВОДСКИЕ', ],
                            4: [f'{self.rs_485_mod[0]}{self.rs_485_set[0]}',
                                f'{self.rs_485_mod[1]}{self.rs_485_set[1]}',
                                f'{self.rs_485_mod[2]}{self.rs_485_set[2]}',
                                f'{self.rs_485_mod[3]}{self.rs_485_set[3]}',
                                f'{self.rs_485_mod[4]}{self.rs_485_set[4]}', ],
                            5: [f'РЕЖИМ: \n {self.rs_232_mode[0][1:]}', f'АДРЕС С2000=127', 'ТАЙМ.СВЯЗИ =20',
                                'ЦЕНТР.УПРАВЛ.                  :−', 'СКОРОСТЬ: \n9600 бит/с', 'ACCOUNT: \n1234',
                                '⬍СОБЫТИЯ LАRS', ],
                            6: ['РЕЖИМ \nПРОГРАММИРОВАНИЯ']}
        self.menu_menu_list = ['УПРАВЛЕНИЕ', 'ПРОСМОТР \nПО СОСТОЯНИЯМ']
        self.menu_state = ['ПОЖАРЫ\n (0)', 'ТРЕВОГИ\n (0)', 'ЗАПУЩЕНЫ\n (0)', 'ОСТАНОВЛЕНЫ\n (0)',
                           'НЕИСПРАВНОСТИ\n (0)', 'ОТКЛЮЧЕНИЯ\n (0)']
        self.menu0 = ['⬍1 ВЗЯТИЕ', '⬍2 СНЯТИЕ', '⬍3 СБРОС ТРЕВОГ', '⬍4 УПРАВЛЕНИЕ', '⬍5 ЗАПРОС', '⬍6 СЕРВИС']
        self.menu1 = {"1": ['⬍11 ШС ПРИБОРА', '⬍12 ГРУППА ШС', '⬍13 ВСЕ ШС'],
                      "2": ['⬍21 СНЯТИЕ ИНД', '⬍22 СНЯТИЕ ГРУППОВОЕ', '⬍23 СНЯТИЕ ОБЩЕЕ'], "3": ['ПРИБОР:'],
                      "4": ['⬍41 УПРАВЛ. РЕЛЕ', '⬍42 УПРАВЛ. АСПТ', ],
                      "5": ['⬍51 ЗАПРОС ШС', '⬍52 ЗАПРОС АЦП'],
                      "6": ['⬍61 ВРЕМЯ', '⬍62 ДАТА', '⬍63  ТЕСТ ИЗВЕЩ.', '⬍64  ТЕСТ  ИНДИКАЦ', '⬍65 ПЕЧАТЬ БУФЕР',
                            '⬍66 СБРОС БУФ.ИТ']}
        self.menu2 = {'11': ['ПРИБОР:', 'НОМЕР ШС'], '12': ['ПРИБОР:'], '13': ['ПРИБОР:'],
                      '21': ['ПРИБОР:', 'НОМЕР ШС'], '22': ['ПРИБОР:'], '23': ['ПРИБОР:'],
                      '3': ['ПРИБОР:'],
                      '41': ['ПРИБОР:', 'УСТРОЙСТВО:', 'ПРОГРАММА:'], '42': ['⬍УПР. АВТОМАТИКОЙ', '⬍УПРАВЛЕНИЕ ПУСКОМ'],
                      '51': ['ПРИБОР:', 'НОМЕР ШС'], '52': ['ПРИБОР:', 'НОМЕР ШС'],
                      '61': [], '62': [], '63': ['⬍ ВКЛ.ТЕСТ', '⬍ ВЫКЛ.ТЕСТ'], '64': ['ПРИБОР:'], '65': [],
                      '66': ['ПРИБОР:']}
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
        elif but_num == 'menu' and not self.menu_menu_stat and self.buff_event_stat != True and self.programm_mode == False:
            playsound('sounds/pick.wav')
            self.display_label.config(text='⬍УПРАВЛЕНИЕ')
            self.menu_menu_stat = True
        elif self.home_menu_stat:
            self.menu_home_func(but_num)
        elif self.buff_event_stat:
            self.buff_event_func(but_num)
        elif but_num == 'home' and self.programm_mode == False:
            playsound('sounds/pick.wav')
            self.home_menu_stat = True
            self.display_label.config(text='⬍ЖУРНАЛ СОБЫТИЙ')
        elif self.user_input == '61':
            self.change_time(but_num)
        elif self.user_input == '62':
            self.change_data(but_num)
        elif self.change_pass == 2:
            self.change_password_func(but_num)
        elif self.test:
            self.test_detector(but_num)
        elif self.testing_ind:
            self.test_indik_func(but_num)
        elif self.entering_password:
            self.check_password_prog(but_num)
        elif self.passw_prog_stat:
            self.prog_menu_func(but_num)
        elif not self.passw_stat:
            self.check_password(but_num)
        elif self.main_menu_stat:
            self.main_menu(but_num)
        else:
            self.start_time()

    def choose_type_events(self, but_num=None):
        self.display_label.config(text=f'⬍ТИП СОБЫТИЯ:\n{self.type_events[self.type_event_val]}')
        if but_num == 'x':
            playsound('sounds/pick.wav')
            self.level = 0
            self.display_label.config(text=self.buff_settings[self.global_pos])
        elif but_num == 'entr':
            playsound('sounds/pick.wav')
            playsound('sounds/pick.wav')
            self.level = 0
            self.buff_settings[self.global_pos] = f'⬍ТИП СОБЫТИЯ:\n {self.type_events[self.type_event_val][1:]}'
            self.display_label.config(text=f'⬍ТИП СОБЫТИЯ:\n {self.type_events[self.type_event_val][1:]}')
        elif but_num == 'right':
            playsound('sounds/pick.wav')
            if self.type_event_val == 8:
                self.type_event_val = 0
            else:
                self.type_event_val += 1
            self.display_label.config(text=f'⬍ТИП СОБЫТИЯ:\n{self.type_events[self.type_event_val]}')
        elif but_num == 'left':
            playsound('sounds/pick.wav')
            if self.type_event_val == 0:
                self.type_event_val = 8
            else:
                self.type_event_val -= 1
            self.display_label.config(text=f'⬍ТИП СОБЫТИЯ:\n{self.type_events[self.type_event_val]}')

    def set_data_range(self, but_num=None):
        position_list = ['empty', 0, 1, 3, 4, 6, 7, -8]
        prefix = ['ПО ДАТУ:', 'С ДАТЫ :', ]
        control_datarange = ['31.12.99', '01.01.00']
        if but_num == 'x':
            playsound('sounds/pick.wav')
            if self.local_pos > 1:
                self.data_range[-self.level] = control_datarange[-self.level]
                self.local_pos = 1
            elif self.level == 2 and self.local_pos == 1:
                self.level -= 1
            else:
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.global_pos])

        elif but_num == 'entr':
            if not self.mistake:
                playsound('sounds/pick.wav')
                self.local_pos = 1
                self.level += 1
                self.buff_settings[
                    self.global_pos] = f'⬍ДАТА:с {self.data_range[1]}\n           по {self.data_range[0]}'
            else:
                playsound('sounds/deny.wav')
                self.mistake = False
                self.local_pos = 1

        elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            if int(self.data_range[-self.level][:2]) > 31 or int(self.data_range[-self.level][3:5]) > 12:
                self.mistake = True
            temp = list(self.data_range[-self.level])
            self.data_range[-self.level] = ''
            temp[position_list[self.local_pos]] = but_num
            self.data_range[-self.level] = self.data_range[-self.level].join(temp)
            self.display_label.config(text=f'{prefix[-self.level]} {self.data_range[-self.level]}')
            self.local_pos += 1
            if self.local_pos == 7 and not self.mistake:
                self.buff_settings[
                    self.global_pos] = f'⬍ДАТА:с {self.data_range[1]}\n           по {self.data_range[0]}'
                self.level += 1
                self.local_pos = 1
            elif self.mistake and self.local_pos == 7:
                # TODO поменять звук отказа
                playsound('sounds/deny.wav')
                self.local_pos = 1
                self.mistake = False

        elif self.level == 3:
            # TODO sound
            self.level = 0
            self.local_pos = 1
            self.display_label.config(text=self.buff_settings[self.global_pos])

        elif self.time_date_stat == 2:
            self.display_label.config(text=f'{prefix[-self.level]}{self.data_range[-self.level]}')
            self.time_date_stat = 1
            self.display_label.after(400, self.buff_event_func)

        elif self.time_date_stat == 1:
            self.time_date_stat = 2
            self.display_label.config(
                text=f'{prefix[-self.level]}{self.data_range[-self.level][:position_list[self.local_pos]]}_{self.data_range[-self.level][position_list[self.local_pos] + 1:]}')
            self.display_label.after(400, self.buff_event_func)

    def choose_area(self, but_num=None):
        self.display_label.config(text=self.area_settings[self.local_pos])
        if self.level == 3:
            playsound('sounds/pick.wav')
            if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'РАЗДЕЛ: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) != 0:
                self.user_number = ''
                self.display_label.config(text=f'РАЗДЕЛ: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'entr' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[3])
            elif but_num == 'entr' and len(self.user_number) != 0:
                self.level = 0
                self.buff_settings[3] = f'⬍РАЗДЕЛ: {self.user_number} \n НЕТ РАЗДЕЛА'
                self.user_number = ''
                self.display_label.config(text=self.buff_settings[3])

        elif self.level == 2:
            playsound('sounds/pick.wav')
            if but_num == 'x':
                self.level = 0
                self.display_label.config(text=self.buff_settings[3])
            if but_num == 'entr':
                if self.user_input == 'change':
                    self.buff_settings[3] = '⬍РАЗДЕЛ:  ВСЕ'
                self.level = 0
                self.display_label.config(text=self.buff_settings[3])

            elif but_num == 'right' or but_num == 'left':
                self.user_input += 'change'
                self.display_label.config(text=f'Выбор:  ВСЕ')

        else:
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.local_pos == 3:
                    self.local_pos = 1
                else:
                    self.local_pos += 1
                self.display_label.config(text=self.area_settings[self.local_pos])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.local_pos == 1:
                    self.local_pos = 3
                else:
                    self.local_pos -= 1
                self.display_label.config(text=self.area_settings[self.local_pos])
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                if self.local_pos == 3:
                    self.buff_settings[self.global_pos] = '⬍РАЗДЕЛ:  ВСЕ'
                    self.local_pos = 1
                    self.level = 0
                    self.display_label.config(text=self.buff_settings[self.global_pos])
                elif self.local_pos == 2:
                    self.level = 2
                    self.display_label.config(text=f'Выбор:{self.buff_settings[self.global_pos][8:]}')
                elif self.local_pos == 1:
                    self.level = 3
                    self.display_label.config(text='РАЗДЕЛ:')

    def choose_element(self, but_num=None):
        if self.level == 2:
            playsound('sounds/pick.wav')
            if but_num == 'x':
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'entr':
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.local_pos])
        else:
            self.display_label.config(text=self.element_settings[self.local_pos - 1])
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.local_pos == 1:
                    self.local_pos = 0
                else:
                    self.local_pos += 1
                self.display_label.config(text=self.element_settings[self.local_pos - 1])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.local_pos = 1
                else:
                    self.local_pos -= 1
                self.display_label.config(text=self.element_settings[self.local_pos - 1])
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.level = 0
                    self.display_label.config(text=self.buff_settings[self.global_pos])
                if self.local_pos == 1:
                    self.level += 1
                    print(self.level)
                    self.display_label.config(text=f'Выбор: ⬍ВСЕ')

    def choose_device(self, but_num=None):
        if self.level == 2:
            playsound('sounds/pick.wav')
            if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'ПРИБОР: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) != 0:
                self.user_number = ''
                self.display_label.config(text=f'ПРИБОР: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'entr' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[3])
            elif but_num == 'entr' and len(self.user_number) != 0:
                self.level = 0
                self.buff_settings[5] = f'⬍ПРИБОР:  \n Адр.{self.user_number}'
                self.user_number = ''
                self.display_label.config(text=self.buff_settings[5])

        elif self.level == 3:
            playsound('sounds/pick.wav')
            if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'№ ВХОДА/ВЫХОДА:\n {self.user_number}')
            elif but_num == 'x' and len(self.user_number) != 0:
                self.user_number = ''
                self.display_label.config(text=f'№ ВХОДА/ВЫХОДА:\n  {self.user_number}')
            elif but_num == 'x' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'entr' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=self.buff_settings[3])
            elif but_num == 'entr' and len(self.user_number) != 0:
                self.level = 0
                self.local_pos = 1
                if 'Адр.' in self.buff_settings[5]:
                    self.buff_settings[5] += f'/{self.user_number}'
                self.user_number = ''
                self.display_label.config(text=self.buff_settings[5])
        else:
            self.display_label.config(text=self.device_settings[self.local_pos - 1])
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.level = 0
                self.local_pos = 1
                self.display_label.config(text=self.buff_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.local_pos == 2:
                    self.local_pos = 0
                else:
                    self.local_pos += 1
                self.display_label.config(text=self.device_settings[self.local_pos - 1])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.local_pos = 2
                else:
                    self.local_pos -= 1
                self.display_label.config(text=self.device_settings[self.local_pos - 1])
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.buff_settings[5] = '⬍ПРИБОР:  ВСЕ'
                    self.level = 0
                    self.display_label.config(text=self.buff_settings[self.global_pos])
                if self.local_pos == 1:
                    self.level = 2
                    self.display_label.config(text=f'ПРИБОР:')
                if self.local_pos == 2:
                    self.level = 3
                    self.display_label.config(text='№ ВХОДА/ВЫХОДА:')

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
                if self.change_pass == 1:
                    self.entering_password = False
                    self.user_input = ''
                    self.change_pass = 2
                    self.display_label.config(text='№ ПАРОЛЯ:')
                else:
                    self.user_input = ''
                    self.passw_prog_stat = True
                    self.entering_password = False
                    self.display_label.config(text='⬍1 ВРЕМЯ И ДАТА')
                    self.buff_events.insert(-1, {'name': 'ПРОГРАММИРОВАНИЕ   \nС2000М v3.02',
                                                 '0': f'{time.strftime("%m.%d")}   {time.strftime("%H:%M:%S")}',
                                                 '1': 'ПРОГРАММИРОВАНИЕ \nП000 С1 ХО',
                                                 '2': 'НЕТ РАЗДЕЛА \nС2000М v3.02',
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
        print('main_0', self.user_input, self.level, self.local_pos, self.global_pos)
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
                #     TODO выяснить работу режимов 65 66
                elif self.user_input == '65':
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.global_pos = 0
                    self.local_pos = 0
                    self.user_input = ''
                    self.start_time()
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
                if self.user_input == '42':
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
                elif self.user_input == '65':
                    self.main_menu_stat = False
                    self.passw_stat = False
                    self.global_pos = 0
                    self.local_pos = 0
                    self.user_input = ''
                    self.start_time()
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
                    self.aspt_or_corrett_time = 422 - int(self.user_input)
                    self.import_data_stat = False
                    self.display_label.config(
                        text=self.menu3[self.user_input][
                            self.data_base_aspt[self.user_number][self.aspt_or_corrett_time]])
                    self.level = 1

        else:
            self.main_3(but_num)

    def main_3(self, but_num):
        if self.aspt_or_corrett_time == 2:
            if but_num == 'entr':
                self.aspt_or_corrett_time = 422 - int(self.user_input)
                self.data_base_aspt[self.user_number][self.aspt_or_corrett_time] = 1
                self.import_data_stat = False
                self.display_label.config(
                    text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_or_corrett_time]])
                self.local_pos = 2
            elif but_num == 'x':
                self.local_pos = 0
                self.import_data_stat = False
                self.aspt_or_corrett_time = 422 - int(self.user_input)
                self.level = 1
                self.display_label.config(
                    text=self.menu3[self.user_input][self.data_base_aspt[self.user_number][self.aspt_or_corrett_time]])
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
                        text=self.menu3[self.user_input][
                            self.data_base_aspt[self.user_number][self.aspt_or_corrett_time]])

                elif but_num == 'entr':
                    self.import_data_stat = False
                    if self.user_input == '421':
                        self.data_base_aspt[self.user_number][self.aspt_or_corrett_time] = -self.local_pos + 3
                        self.display_label.config(
                            text=self.menu3[self.user_input][
                                self.data_base_aspt[self.user_number][self.aspt_or_corrett_time]])

                    else:
                        if self.local_pos == 2:
                            self.local_pos = 0
                            self.data_base_aspt[self.user_number][self.aspt_or_corrett_time] = 0
                            self.display_label.config(text=self.menu3[self.user_input][0])
                        else:
                            self.display_label.config(text=f'ПОДТВЕРДИТЕ ПУСК\n ПРИБОР: {self.user_number} ')
                            self.aspt_or_corrett_time = 2

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
                self.home_menu_stat = False
                self.testing_ind = True
                self.local_pos = 0
                self.display_label.config(text='⬍ С2000М')
            elif self.local_pos == 3:
                self.local_pos = 0
                self.global_pos = 0
                self.change_pass = 1
                self.home_menu_stat = False
                self.entering_password = True
                self.display_label.config(text='ПАРОЛЬ:')
            elif self.local_pos == 4:
                self.local_pos = 0
                self.global_pos = 0
                self.home_menu_stat = False
                self.entering_password = True
                self.display_label.config(text='ПАРОЛЬ:')

    def date_and_time(self, but_num=None):
        if self.global_pos == 2:
            self.change_time(but_num)
        elif self.global_pos == 3:
            self.change_data(but_num)
        elif self.global_pos == 4:
            self.correct_time(but_num)
        else:
            self.display_label.config(text=self.menu_prog_1[1][self.level])
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.global_pos = 0
                self.level = 0
                self.display_label.config(text=self.menu_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.level == 2:
                    self.level = -1
                self.level += 1
                self.display_label.config(text=self.menu_prog_1[1][self.level])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.level == 0:
                    self.level = 3
                self.level -= 1
                self.display_label.config(text=self.menu_prog_1[1][self.level])
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                if self.level == 0:
                    self.global_pos = 2
                    self.time_date_stat = 0
                    self.change_time()
                elif self.level == 1:
                    self.global_pos = 3
                    self.time_date_stat = 0
                    self.change_data()
                else:
                    self.global_pos = 4
                    self.correct_time()

    def config_device(self, but_num=None):
        self.display_label.config(text=f'ПРИБОР: {self.user_number}')
        if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            self.user_number += but_num
            self.display_label.config(text=f'ПРИБОР: {self.user_number}')
        elif but_num == 'x' and len(self.user_number) != 0:
            playsound('sounds/pick.wav')
            self.user_number = ''
            self.display_label.config(text=f'ПРИБОР: {self.user_number}')
        elif but_num == 'x' and len(self.user_number) == 0:
            playsound('sounds/pick.wav')
            self.global_pos = 0
            self.level = 0
            self.display_label.config(text=self.menu_settings[self.local_pos])
        elif but_num == 'entr' and len(self.user_number) == 0:
            # TODO utochnity
            playsound('sounds/deny.wav')
            self.after(10, self.display_label.config(text='Неизвестная команда'))
            self.after(500, self.config_device)
        elif but_num == 'entr' and len(self.user_number) != 0:
            playsound('sounds/deny.wav')
            self.user_number = ''
            self.after(10, self.display_label.config(text='НЕТ ПРИБОРА'))
            self.after(1000, self.config_device)

    def settings_s2000m(self, but_num=None):
        print(self.local_pos, self.level)
        self.display_label.config(text=self.menu_prog_1[3][self.level])
        if but_num == 'x':
            playsound('sounds/pick.wav')
            self.global_pos = 0
            self.level = 0
            self.display_label.config(text=self.menu_settings[self.local_pos])
        elif but_num == 'right':
            playsound('sounds/pick.wav')
            if self.level == 5:
                self.level = -1
            self.level += 1
            self.display_label.config(text=self.menu_prog_1[3][self.level])
        elif but_num == 'left':
            playsound('sounds/pick.wav')
            if self.level == 0:
                self.level = 6
            self.level -= 1
            self.display_label.config(text=self.menu_prog_1[3][self.level])
        elif but_num == 'entr':
            playsound('sounds/pick.wav')

    def rs_485(self, but_num=None):
        if self.global_pos == 2:
            self.change_rs_set(but_num=but_num, param=self.rs_485_mod[self.level])
        else:
            self.display_label.config(text=self.menu_prog_1[4][self.level])
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.global_pos = 0
                self.level = 0
                self.display_label.config(text=self.menu_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.level == len(self.menu_prog_1[4]) - 1:
                    self.level = -1
                self.level += 1
                self.display_label.config(text=self.menu_prog_1[4][self.level])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.level == 0:
                    self.level = len(self.menu_prog_1[4])
                self.level -= 1
                self.display_label.config(text=self.menu_prog_1[4][self.level])
            elif but_num == 'entr':
                if self.level == 1:
                    playsound('sounds/pick.wav')
                    playsound('sounds/pick.wav')
                    if self.rs_485_set[self.level] == '-':
                        self.rs_485_set[self.level] = '+'
                    else:
                        self.rs_485_set[self.level] = '-'
                    self.menu_prog_1[4][self.level] = f'КОЛЬЦЕВОЙ                        : {self.rs_485_set[1]}'
                    self.display_label.config(text=self.menu_prog_1[4][self.level])
                else:
                    playsound('sounds/pick.wav')
                    self.global_pos = 2
                    self.change_rs_set(param=self.rs_485_mod[self.level] )

    def rs_232(self, but_num=None):
        if self.global_pos == 2:
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.global_pos = 1
                self.display_label.config(text=self.menu_prog_1[5][self.level])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.level == len(self.rs_232_mode) - 1:
                    self.level = -1
                self.level += 1
                self.display_label.config(text=f'РЕЖИМ: \n {self.rs_232_mode[self.level]}')
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.level == 0:
                    self.level = len(self.rs_232_mode)
                self.level -= 1
                self.display_label.config(text=f'РЕЖИМ: \n {self.rs_232_mode[self.level]}')
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                playsound('sounds/pick.wav')
                self.global_pos = 1
                self.menu_prog_1[5][0] = f'РЕЖИМ: \n {self.rs_232_mode[self.level][1:]}'
                self.display_label.config(text=self.menu_prog_1[5][0])
                self.level = 0
        else:
            self.display_label.config(text=self.menu_prog_1[5][self.level])
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.global_pos = 0
                self.level = 0
                self.display_label.config(text=self.menu_settings[self.local_pos])
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.level == len(self.menu_prog_1[5]) - 1:
                    self.level = -1
                self.level += 1
                self.display_label.config(text=self.menu_prog_1[5][self.level])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.level == 0:
                    self.level = len(self.menu_prog_1[5])
                self.level -= 1
                self.display_label.config(text=self.menu_prog_1[5][self.level])
            elif but_num == 'entr' and self.level == 0:
                playsound('sounds/pick.wav')
                self.global_pos = 2
                self.display_label.config(text=self.menu_prog_1[5][0][:8] + '⬍' + self.menu_prog_1[5][0][8:])

    def prog_mode(self, but_num=None):
        self.programm_mode = True
        self.display_label.config(text='РЕЖИМ   ПРОГРАММИР')
        if but_num == 'x':
            self.programm_mode = False
            self.passw_prog_stat = False
            self.local_pos = 0
            self.global_pos = 0
            self.user_input = ''
            self.start_time()

    def change_rs_set(self, param, but_num=None, ):
        self.display_label.config(text=f'{param} {self.user_number}')
        if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            self.user_number += but_num
            self.display_label.config(text=f'{param} {self.user_number}')
        elif but_num == 'x' and len(self.user_number) != 0:
            playsound('sounds/pick.wav')
            self.user_number = ''
            self.display_label.config(text=f'{param} {self.user_number}')
        elif but_num == 'x' and len(self.user_number) == 0:
            playsound('sounds/pick.wav')
            self.global_pos = 1
            self.display_label.config(text=self.menu_prog_1[4][self.level])
        elif but_num == 'entr' and len(self.user_number) == 0:
            playsound('sounds/pick.wav')
        elif but_num == 'entr' and len(self.user_number) != 0:
            playsound('sounds/pick.wav')
            playsound('sounds/pick.wav')
            self.rs_485_set[self.level] = self.user_number
            self.menu_prog_1[4][self.level] = self.rs_485_mod[self.level] + self.rs_485_set[self.level]
            self.user_number = ''
            self.global_pos = 1

    def prog_menu_func(self, but_num=None):
        if self.global_pos == 0:
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
                function_list = [self.date_and_time, self.config_device, self.settings_s2000m, self.rs_485,
                                 self.rs_232, self.prog_mode]
                self.global_pos += 1
                self.temp_val = self.local_pos
                function_list[self.local_pos]()
        else:
            function_list = [self.date_and_time, self.config_device, self.settings_s2000m, self.rs_485,
                             self.rs_232, self.prog_mode]
            function_list[self.temp_val](but_num)

    def buff_event_func(self, but_num=None):
        if self.level == 0:
            playsound('sounds/pick.wav')
            if not self.buffer_control:
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
                    self.buff_settings = ['⬍ПОКАЗЫВАТЬ ВСЕ\n СОБЫТИЯ',
                                          f'⬍ТИП СОБЫТИЯ:\n {self.type_events[self.type_event_val][1:]}',
                                          f'⬍ДАТА:с {self.data_range[1]}\n           по {self.data_range[0]}',
                                          '⬍РАЗДЕЛ:  ВСЕ', '⬍ЭЛЕМЕНТ:  ВСЕ', '⬍ПРИБОР:  ВСЕ', ]
                    self.passw_prog_stat = False
                    self.buff_event_stat = False
                    self.time_date_stat = 2
                    self.local_pos = 0
                    self.global_pos = 0
                    self.user_input = ''
                    self.start_time()

                elif but_num in ['1', '2', '3', '5', '9', '0']:
                    self.display_label.config(text=self.buff_events[self.local_pos][but_num])

                elif but_num == 'menu':
                    self.buffer_control = True
                    self.display_label.config(text=self.buff_settings[0])
            else:
                if but_num == 'x':
                    self.buffer_control = False
                    self.type_event_val = 0
                    self.global_pos = 0
                    self.display_label.config(text=self.buff_events[self.local_pos]['name'])

                elif but_num == 'right':
                    if self.global_pos >= len(self.buff_settings) - 1:
                        self.global_pos = 0
                        self.display_label.config(text=self.buff_settings[self.global_pos])
                    else:
                        self.global_pos += 1
                        self.display_label.config(text=self.buff_settings[self.global_pos])

                elif but_num == 'left':
                    if self.global_pos == 0:
                        self.global_pos = len(self.buff_settings) - 1
                        self.display_label.config(text=self.buff_settings[self.global_pos])
                    else:
                        self.global_pos -= 1
                        self.display_label.config(text=self.buff_settings[self.global_pos])

                elif but_num == 'entr':
                    if self.global_pos == 0:
                        self.buffer_control = False
                        self.display_label.config(text=self.buff_events[self.local_pos]['name'])
                    else:
                        self.level += 1
                        function_list = ['empty', self.choose_type_events, self.set_data_range, self.choose_area,
                                         self.choose_element, self.choose_device]
                        function_list[self.global_pos]()
        else:
            function_list = ['empty', self.choose_type_events, self.set_data_range, self.choose_area,
                             self.choose_element, self.choose_device]
            function_list[self.global_pos](but_num)

    def test_indik_func(self, but_num):
        playsound('sounds/pick.wav')
        if but_num == 'x':
            self.local_pos = 2
            self.home_menu_stat = True
            self.testing_ind = False
            self.display_label.config(text=self.menu_home[self.local_pos])
        elif but_num == 'right':
            if self.local_pos == 1:
                self.local_pos = 0
                self.display_label.config(text=self.test_indik[self.local_pos])
            else:
                self.local_pos = 1
                self.display_label.config(text=self.test_indik[self.local_pos])
        elif but_num == 'left':
            if self.local_pos == 0:
                self.local_pos = 1
                self.display_label.config(text=self.test_indik[self.local_pos])
            else:
                self.local_pos = 0
                self.display_label.config(text=self.test_indik[self.local_pos])
        elif but_num == 'entr':
            playsound('sounds/pick.wav')
            self.local_pos = 2
            self.home_menu_stat = True
            self.testing_ind = False
            self.display_label.config(text=self.menu_home[self.local_pos])

    def test_detector(self, but_num=None):
        # TODO уточнить работу данной функции
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
                if self.level < len(self.menu3[self.user_input]) - 1:
                    self.user_number = ''
                    self.level += 1
                    param = self.menu3[self.user_input][self.level]
                    self.display_label.config(text=f'{param} {self.user_number}')
                else:
                    # TODO поменять звук
                    self.user_number = ''
                    self.level = 1
                    param = self.menu3[self.user_input][self.level]
                    self.display_label.config(text=f'{param} {self.user_number}')

    def change_password_func(self, but_num=None):
        if self.level == 1:
            if self.crossout:
                self.new_password_entering(but_num)
            else:
                if but_num == 'x' and len(self.user_number) == 0:
                    self.level = 0
                    self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                elif but_num == 'entr':
                    self.user_number = ''
                    self.display_label.config(text=f'НОВ. ПАРОЛЬ: {self.user_number}')
                    self.crossout = True
        elif self.level == 2:
            if self.crossout:
                self.new_password_entering(but_num)
            else:
                if but_num == 'x' and len(self.user_number) == 0:
                    self.level = 0
                    self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                elif but_num == 'right':
                    if self.local_pos == 1:
                        self.local_pos = 0
                    else:
                        self.local_pos = 1
                    self.display_label.config(text=self.password_menu[self.local_pos])
                elif but_num == 'left':
                    if self.local_pos == 0:
                        self.local_pos = 1
                    else:
                        self.local_pos = 0
                    self.display_label.config(text=self.password_menu[self.local_pos])
                elif but_num == 'entr' and self.local_pos == 0:
                    self.user_number = ''
                    self.crossout = True
                    self.display_label.config(text=f'НОВ. ПАРОЛЬ: {self.user_number}')
                elif but_num == 'entr' and self.local_pos == 1:
                    self.user_number = ''
                    self.level = 0
                    self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
        elif self.level == 3:
            if self.crossout:
                self.new_password_entering(but_num)
            else:
                if but_num == 'x' and len(self.user_number) == 0:
                    self.level = 0
                    self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                elif but_num == 'entr':
                    self.user_number = ''
                    self.display_label.config(text=f'НОВ. ПАРОЛЬ: {self.user_number}')
                    self.crossout = True
        else:
            playsound('sounds/pick.wav')
            self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
            if but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) != 0:
                self.user_number = ''
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
            elif but_num == 'x' and len(self.user_number) == 0:
                self.home_menu_stat = True
                self.local_pos = 3
                self.display_label.config(text='ПАРОЛИ')
            elif but_num == 'entr':
                if self.user_number == '1':
                    self.level = 1
                    self.user_number = ''
                    self.display_label.config(text='⬍ ИЗМЕНИТЬ')
                elif self.user_number == '2':
                    self.level = 2
                    self.user_number = ''
                    self.display_label.config(text='⬍ ИЗМЕНИТЬ')
                else:
                    self.level = 3
                    self.user_number = ''
                    self.display_label.config(text='⬍ ДОБАВИТЬ')

    def new_password_entering(self, but_num=None):
        pass_param = ['⬍УПР. ШЛЕЙФАМИ', '⬍УПР. РАЗДЕЛАМИ']
        if self.choose_pass_abilities == 0:
            param = ['НОВ. ПАРОЛЬ:', 'ПОДТВЕРДИТЕ:']
            if but_num == 'x' and len(self.user_number) == 0:
                self.crossout = False
                self.local_pos = 0
                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
            elif but_num == 'entr' and len(self.user_number) == 0:
                playsound('sounds/pick.wav')
                self.display_label.config(text=f'{param[self.local_pos]}{self.user_number}')
            elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                p = '*' * len(self.user_number)
                self.display_label.config(text=f'{param[self.local_pos]}{p}')
            elif but_num == 'entr' and len(self.user_number) != 0:
                if self.local_pos == 0:
                    self.local_pos += 1
                    self.user_input = self.user_number
                    self.user_number = ''
                    self.display_label.config(text=f'{param[self.local_pos]}{self.user_number}')
                else:
                    if self.user_input == self.user_number:
                        self.user_input = ''
                        self.user_number = ''
                        self.local_pos = 0
                        self.choose_pass_abilities = 1
                        self.display_label.config(text='⬍УПР. ШЛЕЙФАМИ')
                    else:
                        playsound('sounds/deny.wav')
                        self.user_number = ''
                        self.display_label.config(text=f'{param[self.local_pos]}{self.user_number}')
        elif self.choose_pass_abilities == 1:
            if but_num == 'x' and len(self.user_number) == 0:
                playsound('sounds/pick.wav')
                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                self.choose_pass_abilities = 0
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.local_pos == 1:
                    self.local_pos = 0
                else:
                    self.local_pos = 1
                self.display_label.config(text=pass_param[self.local_pos])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.local_pos = 1
                else:
                    self.local_pos = 0
                self.display_label.config(text=pass_param[self.local_pos])
            elif but_num == 'entr' and self.local_pos == 0:
                playsound('sounds/pick.wav')
                self.choose_pass_abilities = 2
                self.display_label.config(text=self.password_abilities[self.local_pos])
            elif but_num == 'entr' and self.local_pos == 1:
                playsound('sounds/pick.wav')
                self.choose_pass_abilities = 3
                self.display_label.config(text='№ УРОВНЯ:')

        elif self.choose_pass_abilities == 2:
            if but_num == 'x':
                playsound('sounds/pick.wav')
                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                self.choose_pass_abilities = 0
            elif but_num == 'right':
                playsound('sounds/pick.wav')
                if self.local_pos == 2:
                    self.local_pos = 0
                else:
                    self.local_pos += 1
                self.display_label.config(text=self.password_abilities[self.local_pos])
            elif but_num == 'left':
                playsound('sounds/pick.wav')
                if self.local_pos == 0:
                    self.local_pos = 2
                else:
                    self.local_pos -= 1
                self.display_label.config(text=self.password_abilities[self.local_pos])
            elif but_num == 'entr':
                playsound('sounds/pick.wav')
                playsound('sounds/pick.wav')

                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                self.choose_pass_abilities = 0
        elif self.choose_pass_abilities == 3:
            if but_num == 'x' and len(self.user_number) == 0:
                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                self.choose_pass_abilities = 0
            elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.user_number += but_num
                self.display_label.config(text=f'№ УРОВНЯ: {self.user_number}')
            elif but_num == 'entr' and len(self.user_number) != 0:
                playsound('sounds/pick.wav')
                self.user_number = ''
                self.level = 0
                self.display_label.config(text=f'№ ПАРОЛЯ: {self.user_number}')
                self.choose_pass_abilities = 0
            elif but_num == 'entr' and len(self.user_number) == 0:
                playsound('sounds/deny.wav')
                self.display_label.config(text=f'№ УРОВНЯ: {self.user_number}')

    def change_time(self, but_num=None, ):
        position_list = [0, 1, 3, 4, 6, 7, -8]
        if self.time_capture:
            self.tim = time.strftime("%H:%M:%S")
            self.time_capture = False

        if but_num == 'x':
            playsound('sounds/pick.wav')
            if self.local_pos > 0:
                self.local_pos = 0
                self.time_capture = True
            elif self.temp_val >= 0:
                self.global_pos = 1
                self.level = 0
                self.local_pos = 0
                self.time_date_stat = 2
                self.display_label.config(text=self.menu_prog_1[1][self.level])
            else:
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.time_capture = True

        elif but_num == 'entr':
            if not self.mistake:
                if self.temp_val >= 0:
                    self.global_pos = 1
                    self.level = 0
                    self.local_pos = 0
                    self.time_date_stat = 2
                    self.display_label.config(text=self.menu_prog_1[1][self.level])
                else:
                    playsound('sounds/pick.wav')
                    self.passw_stat = True
                    self.main_menu_stat = True
                    self.user_input = self.user_input[:1]
                    self.display_label.config(text=self.menu1[str(self.user_input)][0])
                    self.time_date_stat = 2
                    self.time_capture = True
            else:
                playsound('sounds/deny.wav')
                self.time_capture = True
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
                if self.temp_val >= 0:
                    self.global_pos = 1
                    self.level = 0
                    self.local_pos = 0
                    self.time_date_stat = 2
                    self.display_label.config(text=self.menu_prog_1[1][self.level])
                else:
                    self.passw_stat = True
                    self.main_menu_stat = True
                    self.user_input = self.user_input[:1]
                    self.display_label.config(text=self.menu1[str(self.user_input)][0])
                    self.time_date_stat = 2
                    self.local_pos = 0
                    self.time_capture = True
            elif self.mistake and self.local_pos == 6:
                # TODO поменять звук отказа
                playsound('sounds/deny.wav')
                self.time_capture = True
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
        if self.time_capture:
            self.dat = time.strftime("%d:%m:%y")
            self.time_capture = False
        if but_num == 'x':
            playsound('sounds/pick.wav')
            if self.local_pos > 0:
                self.local_pos = 0
                self.time_capture = True
            elif self.temp_val >= 0:
                self.global_pos = 1
                self.level = 1
                self.local_pos = 0
                self.time_date_stat = 2
                self.display_label.config(text=self.menu_prog_1[1][self.level])
            else:
                self.passw_stat = True
                self.main_menu_stat = True
                self.user_input = self.user_input[:1]
                self.display_label.config(text=self.menu1[str(self.user_input)][0])
                self.time_date_stat = 2
                self.time_capture = True

        elif but_num == 'entr':
            if not self.mistake:
                if self.temp_val >= 0:
                    self.global_pos = 1
                    self.level = 1
                    self.local_pos = 0
                    self.time_date_stat = 2
                    self.display_label.config(text=self.menu_prog_1[1][self.level])
                else:
                    playsound('sounds/pick.wav')
                    self.passw_stat = True
                    self.main_menu_stat = True
                    self.user_input = self.user_input[:1]
                    self.display_label.config(text=self.menu1[str(self.user_input)][0])
                    self.time_date_stat = 2
                    self.time_capture = True
            else:
                playsound('sounds/deny.wav')
                self.time_capture = True
                self.mistake = False
                self.local_pos = 0

        elif but_num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            playsound('sounds/pick.wav')
            if int(self.dat[:2]) > 31 or int(self.dat[3:5]) > 12:
                # TODO check control
                print(self.dat[3:5])
                self.mistake = True
            temp = list(self.dat)
            self.dat = ''
            temp[position_list[self.local_pos]] = but_num
            self.dat = self.dat.join(temp)
            self.display_label.config(text=f'ДАТА: {self.dat}')
            self.local_pos += 1
            if self.local_pos == 6 and not self.mistake:
                if self.temp_val >= 0:
                    self.global_pos = 1
                    self.level = 1
                    self.local_pos = 0
                    self.time_date_stat = 2
                    self.display_label.config(text=self.menu_prog_1[1][self.level])
                else:
                    self.passw_stat = True
                    self.main_menu_stat = True
                    self.user_input = self.user_input[:1]
                    self.display_label.config(text=self.menu1[str(self.user_input)][0])
                    self.time_date_stat = 2
                    self.local_pos = 0
                    self.time_capture = True
            elif self.mistake and self.local_pos == 6:
                # TODO поменять звук отказа
                playsound('sounds/deny.wav')
                self.time_capture = True
                self.local_pos = 0
                self.mistake = False

        elif self.time_date_stat == 0:
            self.display_label.config(text=f'ДАТА: {self.dat}')
            self.time_date_stat = 1
            self.display_label.after(400, self.change_data)

        elif self.time_date_stat == 1:
            self.time_date_stat = 0
            self.display_label.config(
                text=f'ДАТА: {self.dat[:position_list[self.local_pos]]}_{self.dat[position_list[self.local_pos] + 1:]}')
            self.display_label.after(400, self.change_data)

    def correct_time(self, but_num=None):
        steps = [0.18, 0.17]
        self.display_label.config(text=f'С/СУТКИ: {self.singh}{self.corrector_time}')
        if but_num == 'x':
            playsound('sounds/pick.wav')
            self.corrector_time = '0.00'
            self.singh = '+'
            self.global_pos = 1
            self.level = 2
            self.local_pos = 0
            self.display_label.config(text=self.menu_prog_1[1][self.level])
            return
        elif but_num == 'entr':
            playsound('sounds/pick.wav')
            self.global_pos = 1
            self.level = 2
            self.local_pos = 0
            self.display_label.config(text=self.menu_prog_1[1][self.level])
        elif but_num == 'right':
            playsound('sounds/pick.wav')
            if self.corrector_time == '0.00':
                self.aspt_or_corrett_time = 0
            elif self.aspt_or_corrett_time == 1:
                self.aspt_or_corrett_time = 0
            else:
                self.aspt_or_corrett_time = 1
            self.corrector_time = round(float(self.corrector_time) + steps[self.aspt_or_corrett_time], 2)
        elif but_num == 'left':
            playsound('sounds/pick.wav')
            if self.corrector_time == 0.18:
                self.aspt_or_corrett_time = 0
                self.corrector_time = round(float(self.corrector_time) - steps[self.aspt_or_corrett_time], 2)
            elif self.aspt_or_corrett_time == 1:
                self.aspt_or_corrett_time = 0
                self.corrector_time = round(float(self.corrector_time) - steps[self.aspt_or_corrett_time - 1], 2)
            else:
                self.aspt_or_corrett_time = 1
                self.corrector_time = round(float(self.corrector_time) - steps[self.aspt_or_corrett_time - 1], 2)

        if float(self.corrector_time) >= 0.00:
            self.singh = '+'
        else:
            self.singh = ''
        self.display_label.config(text=f'С/СУТКИ: {self.singh}{self.corrector_time}')

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
        #     TODO Узнать куда возвращается пульт
        elif mode == 6:
            self.import_data_stat = False
            self.local_pos = int(self.user_input[1:]) - 1
            self.user_input = self.user_input[:1]
            self.after(250, self.display_label.config(text=self.menu1[self.user_input][self.local_pos]))
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
