import unittest
import tkinter as tk
from main import Main

Example = Main(root=tk.Tk())



class main_0_test(unittest.TestCase):

    def test_right(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0,0,False,False,''
        Example.main_0(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [1, 0, False, False, ''])

    def test_left(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [5, 0, False, False, ''])

    def test_number(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='1')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [0, 1, False, False, '1'])

    def test_3(self):
        Example.main_0(but_num='3')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, False, False, '3',True])

    def test_x(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='x')
        result = [Example.local_pos,Example.global_pos,Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result,[0,0,False,False,''])

    def test_entr_loc0(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [0, 1, False, False, '1'])

    def test_entr_loc2(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input , Example.import_data_stat = 2, 0, False, False, '', False
        Example.main_0(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, False, False, '3',True])

class check_main_pass_test(unittest.TestCase):

    def test_number(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, ''
        Example.check_password(but_num='1')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result,[False, False, '1'])

    def test_number_valid(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, '123'
        Example.check_password(but_num='4')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result,[True, True, ''])

    def test_x_fill(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, '123'
        Example.check_password(but_num='x')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [False, False, ''])

    def test_entr_(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, '123'
        Example.check_password(but_num='entr')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [False, False, ''])

    def test_x_unfill(self):
        Example.times =  False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])

    def test_right(self):
        Example.times =  False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])

    def test_left(self):
        Example.times =  False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])

class check_prog_passs_test(unittest.TestCase):

    def test_x_unfill(self):
        Example.entering_password, Example.times, Example.user_input,Example.change_pass, Example.passw_prog_stat,Example.home_menu_stat  = True, False,'', 0, False, False
        Example.check_password_prog(but_num='x')
        result = [Example.entering_password, Example.times, Example.user_input,Example.change_pass, Example.passw_prog_stat,Example.home_menu_stat]
        self.assertListEqual(result, [True, False, '',0,False,True])

    def test_x_fill(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '1', 0, False, False
        Example.check_password_prog(but_num='x')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [True, False, '', 0, False, False])

    def test_number(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '', 0, False, False
        Example.check_password_prog(but_num='1')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [True, False, '1', 0, False, False])

    def test_number_overflow(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '1111111111111', 0, False, False
        Example.check_password_prog(but_num='1')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [False, True, '', 0, False, False])

    def test_entr_validv1(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '123456', 0, False, False
        Example.check_password_prog(but_num='entr')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [False, False, '', 0, True, False])

    def test_entr_validv2(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '123456', 1, False, False
        Example.check_password_prog(but_num='entr')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [False, False, '', 2, False, False])

    def test_entr_invalid(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '11', 0, False, False
        Example.check_password_prog(but_num='entr')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [False, True, '', 0, False, False])

class main_1_test(unittest.TestCase):

    def test_x(self):
        Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat,Example.test=0,1,'1',True,True,False
        Example.main_1(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input,]
        self.assertListEqual(result, [0, 0, '', ])

    def test_right(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '1', True, True, False, False
        Example.main_1(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.user_input, ]
        self.assertListEqual(result, [1, 1, '1', ])

    def test_left(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat= 0, 1, '1', True, True, False, False
        Example.main_1(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.user_input, ]
        self.assertListEqual(result, [2, 1, '1', ])

    def test_entr_simple(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '1', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '11',True, True, False, True ])

    def test_entr_42(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 1, 1, '4', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 2, '42',True, True, False, False ])

    def test_entr_61(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '61',False, False, False, False ])

    def test_entr_62(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 1, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '62',False, False, False, False ])

    def test_entr_63(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 2, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '63',False, False, True, False ])

    def test_entr_65(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 4, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat]
        self.assertListEqual(result, [0, 0, '',False, False, False, False ])

    def test_number_simple(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '2', True, True, False, False
        Example.main_1(but_num='2')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.main_menu_stat, Example.passw_stat, Example.test,Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '22',True, True, False, True ])

class main_2_test(unittest.TestCase):

    def test_x(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat = 0,2,'42',0,False
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat ]
        self.assertListEqual(result, [0, 1, '4',0,False ])

    def test_right(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat = 0, 2, '42', 0, False
        Example.main_2(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat]
        self.assertListEqual(result, [1, 2, '42', 0, False])

    def test_left(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat = 1, 2, '42', 0, False
        Example.main_2(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '42', 0, False])

    def test_entr_lv1(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat = 0, 2, '42', 0, False
        Example.main_2(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '421', 0, True])

    def test_x_import(self):
        Example.local_pos, Example.global_pos, Example.user_input,Example.user_number, Example.level, Example.import_data_stat = 0,2,'421','',0,True
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.user_number, Example.level, Example.import_data_stat ]
        self.assertListEqual(result, [0, 2, '42','',0,False ])

    def test_x_import_clear(self):
        Example.local_pos, Example.global_pos, Example.user_input,Example.user_number, Example.level, Example.import_data_stat = 0,2,'421','11',0,True
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input,Example.user_number, Example.level, Example.import_data_stat ]
        self.assertListEqual(result, [0, 2, '421','',0,True ])

    def test_number(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level, Example.import_data_stat = 0, 2, '421', '11', 0, True
        Example.main_2(but_num='1')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '421', '111', 0, True])

    def test_entr_lv2_len0(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level, Example.import_data_stat = 0, 2, '421', '', 0, True
        Example.main_2(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '421', '', 0, True])

    def test_entr_lv2_len(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level, Example.import_data_stat = 0, 2, '421', '1', 0, True
        Example.main_2(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '421', '1', 1, False])

class main_3_test(unittest.TestCase):

    def test_x_not_impport(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 0, 2, '421', 1, False,0,''
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [0, 2, '421', 0, True,0,''])

    def test_entr_not_impport(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 0, 2, '421', 1, False,0,''
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [2, 2, '421', 1, True,0,''])

    def test_right_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 2, 2, '421', 1, True,0,''
        Example.main_3(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [3, 2, '421', 1, True,0,''])

    def test_left_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 3, 2, '421', 1, True,0,''
        Example.main_3(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [2, 2, '421', 1, True,0,''])

    def test_x_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 3, 2, '421', 1, True,0,'5', {'5': [0, 0]}
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '421', 1, False,0,'5',{'5': [0, 0]}])

    def test_entr_import421(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 3, 2, '421', 1, True,0,'5', {'5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [3, 2, '421', 1, False,0,'5',{'5': [0, 0]}])

    def test_entr_import422v1(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 2, 2, '422', 1, True,0,'5', {'5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '422', 1, False,0,'5',{'5': [0, 0]}])

    def test_entr_import422v2(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 3, 2, '422', 1, True,0,'5', {'5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [3, 2, '422', 1, False,2,'5',{'5': [0, 0]}])

    def test_entr_aspt(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 3, 2, '422', 1, True,2,'5', {'5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [2, 2, '422', 1, False,0,'5',{'5': [1, 0]}])

    def test_x_aspt(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt = 3, 2, '422', 1, True,2,'5', {'5': [0, 0]}
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,Example.aspt_or_corrett_time, Example.user_number,Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '422', 1, False,0,'5',{'5': [0, 0]}])

class menu_menu_1_test(unittest.TestCase):

    def test_x(self):
        Example.menu_menu_stat, Example.local_pos,Example.global_pos = True,0,0
        Example.menu_menu_1(but_num='x')
        result = [Example.menu_menu_stat, Example.local_pos,Example.global_pos ]
        self.assertListEqual(result, [False,0,0])

    def test_right(self):
        Example.menu_menu_stat, Example.local_pos,Example.global_pos = True,0,0
        Example.menu_menu_1(but_num='right')
        result = [Example.menu_menu_stat, Example.local_pos,Example.global_pos ]
        self.assertListEqual(result, [True,1,0])

    def test_left(self):
        Example.menu_menu_stat, Example.local_pos,Example.global_pos = True,0,0
        Example.menu_menu_1(but_num='left')
        result = [Example.menu_menu_stat, Example.local_pos,Example.global_pos ]
        self.assertListEqual(result, [True,1,0])

    def test_entr_l0(self):
        Example.menu_menu_stat, Example.local_pos,Example.global_pos = True,0,0
        Example.menu_menu_1(but_num='entr')
        result = [Example.menu_menu_stat, Example.local_pos,Example.global_pos]
        self.assertListEqual(result, [False,0,0])

    def test_entr_l1(self):
        Example.menu_menu_stat, Example.local_pos,Example.global_pos = True,1,0
        Example.menu_menu_1(but_num='entr')
        result = [Example.menu_menu_stat, Example.local_pos,Example.global_pos]
        self.assertListEqual(result, [True,0,1])

class menu_menu_2_test(unittest.TestCase):

    def test_x(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 1
        Example.menu_menu_2(but_num='x')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 0, 0])

    def test_right(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 1
        Example.menu_menu_2(but_num='right')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 1, 1])

    def test_left(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 1
        Example.menu_menu_2(but_num='left')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 5, 1])

class menu_home_func_test(unittest.TestCase):

    def test_x(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0,''
        Example.menu_home_func(but_num='x')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input]
        self.assertListEqual(result, [False, 0, 0, ''])

    def test_right(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0,''
        Example.menu_home_func(but_num='right')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input]
        self.assertListEqual(result, [True, 1, 0, ''])

    def test_left(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0,''
        Example.menu_home_func(but_num='left')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input]
        self.assertListEqual(result, [True, 4, 0, ''])

    def test_entr_v0(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.buff_event_stat = True, 0, 0,'',False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input,Example.buff_event_stat]
        self.assertListEqual(result, [False, 1, 0, '',True])

    def test_entr_v1(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.buff_event_stat = True, 1, 0,'',False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input,Example.buff_event_stat]
        self.assertListEqual(result, [False, 0, 0, '',False])

    def test_entr_v2(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.testing_ind = True, 2, 0,'',False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input,Example.testing_ind]
        self.assertListEqual(result, [False, 0, 0, '',True])

    def test_entr_v3(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.entering_password,Example.change_pass = True, 3, 0,'',False,0
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input,Example.entering_password,Example.change_pass]
        self.assertListEqual(result, [False, 0, 0, '',True,1])

    def test_entr_v4(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.entering_password,Example.change_pass = True, 4, 0,'',False,0
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos,Example.user_input,Example.entering_password,Example.change_pass]
        self.assertListEqual(result, [False, 0, 0, '',True,0])

class date_and_time_test(unittest.TestCase):

    def test_x(self):
        Example.global_pos,Example.level,Example.time_date_stat  = 1,1,2
        Example.date_and_time(but_num='x')
        result = [  Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [0, 0, 2])

    def test_right(self):
        Example.global_pos,Example.level,Example.time_date_stat  = 1,1,2
        Example.date_and_time(but_num='right')
        result = [  Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [1, 2, 2])

    def test_left(self):
        Example.global_pos,Example.level,Example.time_date_stat  = 1,1,2
        Example.date_and_time(but_num='left')
        result = [Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [1, 0, 2])

    def test_entr_l0(self):
        Example.global_pos,Example.level,Example.time_date_stat  = 1,0,2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [2, 0, 1])

    def test_entr_l1(self):
        Example.global_pos,Example.level,Example.time_date_stat = 1,1,2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [3, 1, 1])

    def test_entr_l2(self):
        Example.global_pos,Example.level,Example.time_date_stat = 1,2,2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos,Example.level,Example.time_date_stat]
        self.assertListEqual(result, [4, 2, 2])

class config_device_test(unittest.TestCase):

    def test_x_unfill(self):
        Example.global_pos, Example.local_pos,Example.level, Example.user_number = 1, 1, 0, ''
        Example.config_device(but_num='x')
        result = [Example.global_pos,Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [0, 1, 0, ''])

    def test_x_fill(self):
        Example.global_pos, Example.local_pos,Example.level, Example.user_number = 1, 1, 0, '12'
        Example.config_device(but_num='x')
        result = [Example.global_pos,Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, ''])

    def test_entr_fill(self):
        Example.global_pos, Example.local_pos,Example.level, Example.user_number = 1, 1, 0, '12'
        Example.config_device(but_num='entr')
        result = [Example.global_pos,Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, ''])

    def test_number(self):
        Example.global_pos, Example.local_pos,Example.level, Example.user_number = 1, 1, 0, ''
        Example.config_device(but_num='1')
        result = [Example.global_pos,Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, '1'])

class settings_s2000m_test(unittest.TestCase):

    def test_x(self):
        pass