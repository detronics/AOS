import unittest
import tkinter as tk
from main import Main

Example = Main(root=tk.Tk())


class main_0_test(unittest.TestCase):

    def test_right(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
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
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 1, False, False, '3', True])

    def test_x(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [0, 0, False, False, ''])

    def test_entr_loc0(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input = 0, 0, False, False, ''
        Example.main_0(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [0, 1, False, False, '1'])

    def test_entr_loc2(self):
        Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input, Example.import_data_stat = 2, 0, False, False, '', False
        Example.main_0(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.passw_stat, Example.main_menu_stat, Example.user_input,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 1, False, False, '3', True])


class check_main_pass_test(unittest.TestCase):

    def test_number(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, ''
        Example.check_password(but_num='1')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [False, False, '1'])

    def test_number_valid(self):
        Example.passw_stat, Example.main_menu_stat, Example.user_input = False, False, '123'
        Example.check_password(but_num='4')
        result = [Example.passw_stat, Example.main_menu_stat, Example.user_input]
        self.assertListEqual(result, [True, True, ''])

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
        Example.times = False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])

    def test_right(self):
        Example.times = False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])

    def test_left(self):
        Example.times = False
        Example.check_password(but_num='x')
        result = [Example.times]
        self.assertListEqual(result, [True])


class check_prog_passs_test(unittest.TestCase):

    def test_x_unfill(self):
        Example.entering_password, Example.times, Example.user_input, Example.change_pass, Example.passw_prog_stat, Example.home_menu_stat = True, False, '', 0, False, False
        Example.check_password_prog(but_num='x')
        result = [Example.entering_password, Example.times, Example.user_input, Example.change_pass,
                  Example.passw_prog_stat, Example.home_menu_stat]
        self.assertListEqual(result, [True, False, '', 0, False, True])

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
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test = 0, 1, '1', True, True, False
        Example.main_1(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, ]
        self.assertListEqual(result, [0, 0, '', ])

    def test_right(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '1', True, True, False, False
        Example.main_1(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.user_input, ]
        self.assertListEqual(result, [1, 1, '1', ])

    def test_left(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '1', True, True, False, False
        Example.main_1(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.user_input, ]
        self.assertListEqual(result, [2, 1, '1', ])

    def test_entr_simple(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '1', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '11', True, True, False, True])

    def test_entr_42(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 1, 1, '4', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '42', True, True, False, False])

    def test_entr_61(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '61', False, False, False, False])

    def test_entr_62(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 1, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '62', False, False, False, False])

    def test_entr_63(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 2, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '63', False, False, True, False])

    def test_entr_65(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 4, 1, '6', True, True, False, False
        Example.main_1(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 0, '', False, False, False, False])

    def test_number_simple(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat, Example.test, Example.import_data_stat = 0, 1, '2', True, True, False, False
        Example.main_1(but_num='2')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.main_menu_stat, Example.passw_stat,
                  Example.test, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '22', True, True, False, True])


class main_2_test(unittest.TestCase):

    def test_x(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat = 0, 2, '42', 0, False
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat]
        self.assertListEqual(result, [0, 1, '4', 0, False])

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
        Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level, Example.import_data_stat = 0, 2, '421', '', 0, True
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '42', '', 0, False])

    def test_x_import_clear(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level, Example.import_data_stat = 0, 2, '421', '11', 0, True
        Example.main_2(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.user_number, Example.level,
                  Example.import_data_stat]
        self.assertListEqual(result, [0, 2, '421', '', 0, True])

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
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 0, 2, '421', 1, False, 0, ''
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [0, 2, '421', 0, True, 0, ''])

    def test_entr_not_impport(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 0, 2, '421', 1, False, 0, ''
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [2, 2, '421', 1, True, 0, ''])

    def test_right_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 2, 2, '421', 1, True, 0, ''
        Example.main_3(but_num='right')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [3, 2, '421', 1, True, 0, ''])

    def test_left_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number = 3, 2, '421', 1, True, 0, ''
        Example.main_3(but_num='left')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number]
        self.assertListEqual(result, [2, 2, '421', 1, True, 0, ''])

    def test_x_import(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 3, 2, '421', 1, True, 0, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '421', 1, False, 0, '5', {'5': [0, 0]}])

    def test_entr_import421(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 3, 2, '421', 1, True, 0, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [3, 2, '421', 1, False, 0, '5', {'5': [0, 0]}])

    def test_entr_import422v1(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 2, 2, '422', 1, True, 0, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '422', 1, False, 0, '5', {'5': [0, 0]}])

    def test_entr_import422v2(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 3, 2, '422', 1, True, 0, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [3, 2, '422', 1, False, 2, '5', {'5': [0, 0]}])

    def test_entr_aspt(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 3, 2, '422', 1, True, 2, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='entr')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [2, 2, '422', 1, False, 0, '5', {'5': [1, 0]}])

    def test_x_aspt(self):
        Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat, Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt = 3, 2, '422', 1, True, 2, '5', {
            '5': [0, 0]}
        Example.main_3(but_num='x')
        result = [Example.local_pos, Example.global_pos, Example.user_input, Example.level, Example.import_data_stat,
                  Example.aspt_or_corrett_time, Example.user_number, Example.data_base_aspt]
        self.assertListEqual(result, [0, 2, '422', 1, False, 0, '5', {'5': [0, 0]}])


class menu_menu_1_test(unittest.TestCase):

    def test_x(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 0
        Example.menu_menu_1(but_num='x')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [False, 0, 0])

    def test_right(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 0
        Example.menu_menu_1(but_num='right')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 1, 0])

    def test_left(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 0
        Example.menu_menu_1(but_num='left')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 1, 0])

    def test_entr_l0(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 0, 0
        Example.menu_menu_1(but_num='entr')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [False, 0, 0])

    def test_entr_l1(self):
        Example.menu_menu_stat, Example.local_pos, Example.global_pos = True, 1, 0
        Example.menu_menu_1(but_num='entr')
        result = [Example.menu_menu_stat, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [True, 0, 1])


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
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0, ''
        Example.menu_home_func(but_num='x')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input]
        self.assertListEqual(result, [False, 0, 0, ''])

    def test_right(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0, ''
        Example.menu_home_func(but_num='right')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input]
        self.assertListEqual(result, [True, 1, 0, ''])

    def test_left(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input = True, 0, 0, ''
        Example.menu_home_func(but_num='left')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input]
        self.assertListEqual(result, [True, 4, 0, ''])

    def test_entr_v0(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.buff_event_stat = True, 0, 0, '', False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input,
                  Example.buff_event_stat]
        self.assertListEqual(result, [False, 1, 0, '', True])

    def test_entr_v1(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.buff_event_stat = True, 1, 0, '', False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input,
                  Example.buff_event_stat]
        self.assertListEqual(result, [False, 0, 0, '', False])

    def test_entr_v2(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.testing_ind = True, 2, 0, '', False
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input,
                  Example.testing_ind]
        self.assertListEqual(result, [False, 0, 0, '', True])

    def test_entr_v3(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.entering_password, Example.change_pass = True, 3, 0, '', False, 0
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input,
                  Example.entering_password, Example.change_pass]
        self.assertListEqual(result, [False, 0, 0, '', True, 1])

    def test_entr_v4(self):
        Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input, Example.entering_password, Example.change_pass = True, 4, 0, '', False, 0
        Example.menu_home_func(but_num='entr')
        result = [Example.home_menu_stat, Example.local_pos, Example.global_pos, Example.user_input,
                  Example.entering_password, Example.change_pass]
        self.assertListEqual(result, [False, 0, 0, '', True, 0])


class date_and_time_test(unittest.TestCase):

    def test_x(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 1, 2
        Example.date_and_time(but_num='x')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [0, 0, 2])

    def test_right(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 1, 2
        Example.date_and_time(but_num='right')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [1, 2, 2])

    def test_left(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 1, 2
        Example.date_and_time(but_num='left')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [1, 0, 2])

    def test_entr_l0(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 0, 2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [2, 0, 1])

    def test_entr_l1(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 1, 2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [3, 1, 1])

    def test_entr_l2(self):
        Example.global_pos, Example.level, Example.time_date_stat = 1, 2, 2
        Example.date_and_time(but_num='entr')
        result = [Example.global_pos, Example.level, Example.time_date_stat]
        self.assertListEqual(result, [4, 2, 2])


class config_device_test(unittest.TestCase):

    def test_x_unfill(self):
        Example.global_pos, Example.local_pos, Example.level, Example.user_number = 1, 1, 0, ''
        Example.config_device(but_num='x')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [0, 1, 0, ''])

    def test_x_fill(self):
        Example.global_pos, Example.local_pos, Example.level, Example.user_number = 1, 1, 0, '12'
        Example.config_device(but_num='x')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, ''])

    def test_entr_fill(self):
        Example.global_pos, Example.local_pos, Example.level, Example.user_number = 1, 1, 0, '12'
        Example.config_device(but_num='entr')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, ''])

    def test_number(self):
        Example.global_pos, Example.local_pos, Example.level, Example.user_number = 1, 1, 0, ''
        Example.config_device(but_num='1')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.user_number]
        self.assertListEqual(result, [1, 1, 0, '1'])


class settings_s2000m_test(unittest.TestCase):

    def test_x(self):
        Example.global_pos, Example.level,Example.local_pos = 1, 0, 2
        Example.settings_s2000m(but_num='x')
        result = [Example.global_pos, Example.level,Example.local_pos]
        self.assertListEqual(result, [0, 0,2])

    def test_right(self):
        Example.global_pos, Example.level,Example.local_pos = 1, 0, 2
        Example.settings_s2000m(but_num='right')
        result = [Example.global_pos, Example.level,Example.local_pos]
        self.assertListEqual(result, [1, 1,2])

    def test_left(self):
        Example.global_pos, Example.level,Example.local_pos = 1, 0, 2
        Example.settings_s2000m(but_num='left')
        result = [Example.global_pos, Example.level,Example.local_pos]
        self.assertListEqual(result, [1, 5,2])

class rs_485_test(unittest.TestCase):

    def test_x(self):
        Example.level, Example.local_pos, Example.global_pos = 0,3,1
        Example.rs_485(but_num='x')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [0, 3, 0])

    def test_right(self):
        Example.level, Example.local_pos, Example.global_pos = 0,3,1
        Example.rs_485(but_num='right')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [1, 3, 1])

    def test_left(self):
        Example.level, Example.local_pos, Example.global_pos = 0,3,1
        Example.rs_485(but_num='left')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [4, 3, 1])

    def test_entr_lv2(self):
        Example.level, Example.local_pos, Example.global_pos = 2,3,1
        Example.rs_485(but_num='entr')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [2, 3, 2])

    def test_entr_lv1(self):
        Example.level, Example.local_pos, Example.global_pos = 1,3,1
        Example.rs_485(but_num='entr')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [1, 3, 1])

class rs_232_test(unittest.TestCase):

    def test_x_g2(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 2
        Example.rs_232(but_num='x')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [0, 4, 1])

    def test_right_g2(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 2
        Example.rs_232(but_num='right')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [1, 4, 2])

    def test_left_g2(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 2
        Example.rs_232(but_num='left')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [5, 4, 2])

    def test_entr_g2(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 2
        Example.rs_232(but_num='entr')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [0, 4, 1])

    def test_x_g1(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 1
        Example.rs_232(but_num='x')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [0, 4, 0])

    def test_right_g1(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 1
        Example.rs_232(but_num='right')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [1, 4, 1])

    def test_left_g1(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 1
        Example.rs_232(but_num='left')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [6, 4, 1])

    def test_entr_g1(self):
        Example.level, Example.local_pos, Example.global_pos = 0, 4, 1
        Example.rs_232(but_num='entr')
        result = [Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, [0, 4, 2])

class prog_mode_test(unittest.TestCase):

    def test_x(self):
        Example.level, Example.local_pos, Example.global_pos,Example.programm_mode, Example.passw_prog_stat, Example.user_input = 0, 4, 2,True, True, '2'
        Example.prog_mode(but_num='x')
        result = [Example.level, Example.local_pos, Example.global_pos,Example.programm_mode, Example.passw_prog_stat, Example.user_input]
        self.assertListEqual(result, [0, 0, 0,False, False, ''])

class change_rs_set_test(unittest.TestCase):

    def test_x_unfill(self):
        Example.user_number, Example.level, Example.local_pos, Example.global_pos = '', 0, 2,3
        Example.change_rs_set(but_num='x',param='lol')
        result = [Example.user_number, Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, ['', 0, 2,1])

    def test_x_fill(self):
        Example.user_number, Example.level, Example.local_pos, Example.global_pos = '22', 0, 2,3
        Example.change_rs_set(but_num='x',param='lol')
        result = [Example.user_number, Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, ['', 0, 2,3])

    def test_number(self):
        Example.user_number, Example.level, Example.local_pos, Example.global_pos = '22', 0, 2,3
        Example.change_rs_set(but_num='2',param='lol')
        result = [Example.user_number, Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, ['222', 0, 2,3])

    def test_entr_fill(self):
        Example.user_number, Example.level, Example.local_pos, Example.global_pos = '22', 0, 2,3
        Example.change_rs_set(but_num='entr',param='lol')
        result = [Example.user_number, Example.level, Example.local_pos, Example.global_pos]
        self.assertListEqual(result, ['', 0, 2,1])

class prog_menu_func_test(unittest.TestCase):

    def test_x(self):
        Example.level, Example.local_pos, Example.global_pos, Example.passw_prog_stat = 0,0,0, True
        Example.prog_menu_func(but_num='x')
        result = [ Example.level, Example.local_pos, Example.global_pos,Example.passw_prog_stat ]
        self.assertListEqual(result, [0,0,0,False])

    def test_right(self):
        Example.level, Example.local_pos, Example.global_pos, Example.passw_prog_stat = 0,0,0, True
        Example.prog_menu_func(but_num='right')
        result = [ Example.level, Example.local_pos, Example.global_pos,Example.passw_prog_stat ]
        self.assertListEqual(result, [0,1,0,True])

    def test_left(self):
        Example.level, Example.local_pos, Example.global_pos, Example.passw_prog_stat = 0,0,0, True
        Example.prog_menu_func(but_num='left')
        result = [ Example.level, Example.local_pos, Example.global_pos,Example.passw_prog_stat ]
        self.assertListEqual(result, [0,5,0,True])

class buff_event_func_test(unittest.TestCase):

    def test_xlbuf(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',False,True
        Example.buff_event_func(but_num='x')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,0,0,2,'',False,False])

    def test_rightbuf(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',False,True
        Example.buff_event_func(but_num='right')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,2,0,2,'',False,True])

    def test_leftbuf(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',False,True
        Example.buff_event_func(but_num='left')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,0,0,2,'',False,True])

    def test_menubuf(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',False,True
        Example.buff_event_func(but_num='menu')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,1,0,2,'',True,True])

    def test_x(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',True,True
        Example.buff_event_func(but_num='x')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,1,0,2,'',False,False])

    def test_right(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',True,True
        Example.buff_event_func(but_num='right')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [1,1,0,2,'',True,True])

    def test_left(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',True,True
        Example.buff_event_func(but_num='left')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [5,1,0,2,'',True,True])

    def test_entr(self):
        Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat  = 0,1,0,2,'',True,True
        Example.buff_event_func(but_num='entr')
        result = [Example.global_pos, Example.local_pos, Example.level, Example.time_date_stat, Example.user_input, Example.buffer_control, Example.buff_event_stat]
        self.assertListEqual(result, [0,1,0,2,'',False,True])

class test_indik_func_test(unittest.TestCase):

    def test_x(self):
        Example.local_pos, Example.home_menu_stat, Example.testing_ind = 0, False, True
        Example.test_indik_func(but_num='x')
        result = [Example.local_pos, Example.home_menu_stat, Example.testing_ind]
        self.assertListEqual(result, [2, True, False])

    def test_right(self):
        Example.local_pos, Example.home_menu_stat, Example.testing_ind = 0, False, True
        Example.test_indik_func(but_num='right')
        result = [Example.local_pos, Example.home_menu_stat, Example.testing_ind]
        self.assertListEqual(result, [1, False, True])

    def test_left(self):
        Example.local_pos, Example.home_menu_stat, Example.testing_ind = 1, False, True
        Example.test_indik_func(but_num='left')
        result = [Example.local_pos, Example.home_menu_stat, Example.testing_ind]
        self.assertListEqual(result, [0, False, True])

    def test_entr(self):
        Example.local_pos, Example.home_menu_stat, Example.testing_ind = 0, False, True
        Example.test_indik_func(but_num='entr')
        result = [Example.local_pos, Example.home_menu_stat, Example.testing_ind]
        self.assertListEqual(result, [2, True, False])

class test_detector_test(unittest.TestCase):

    def test_x_len2(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test  = 0,'63',False,False,True
        Example.test_detector(but_num='x')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test]
        self.assertListEqual(result, [0,'6',True,True,False])

    def test_right_len2(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test  = 0,'63',False,False,True
        Example.test_detector(but_num='right')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test]
        self.assertListEqual(result, [1,'63',False,False,True])

    def test_left_len2(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test  = 0,'63',False,False,True
        Example.test_detector(but_num='left')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test]
        self.assertListEqual(result, [1,'63',False,False,True])

    def test_entr_len2(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test  = 0,'63',False,False,True
        Example.test_detector(but_num='entr')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test]
        self.assertListEqual(result, [0,'631',False,False,True])

    def test_x_unfill_len3(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number = 0,'631',False,False,True,''
        Example.test_detector(but_num='x')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number]
        self.assertListEqual(result, [0,'63',False,False,True,''])

    def test_x_fill_len3(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number = 0,'631',False,False,True,'5'
        Example.test_detector(but_num='x')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number]
        self.assertListEqual(result, [0,'631',False,False,True,''])

    def test_x_fill_len3_lv1(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level = 0,'631',False,False,True,'',1
        Example.test_detector(but_num='x')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level]
        self.assertListEqual(result, [0,'631',False,False,True,'',0])

    def test_number_len3(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number = 0,'631',False,False,True,'5'
        Example.test_detector(but_num='1')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number]
        self.assertListEqual(result, [0,'631',False,False,True,'51'])

    def test_entr_len3_lv0(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level = 0,'631',False,False,True,'5',0
        Example.test_detector(but_num='entr')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level]
        self.assertListEqual(result, [0,'631',False,False,True,'',1])

    def test_entr_len3_lv1(self):
        Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level = 0,'631',False,False,True,'5',1
        Example.test_detector(but_num='entr')
        result = [Example.local_pos,Example.user_input,Example.passw_stat, Example.main_menu_stat, Example.test, Example.user_number, Example.level]
        self.assertListEqual(result, [0,'631',False,False,True,'',2])

class change_password_func_test(unittest.TestCase):

    def test_x_lv1(self):
        Example.level, Example.local_pos, Example.user_number  = 1,0,'',
        Example.change_password_func(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [0,0,''])

    def test_entr_lv1(self):
        Example.level, Example.local_pos, Example.user_number  = 1,0,'',
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [1,0,''])

    def test_x_lv2(self):
        Example.level, Example.local_pos, Example.user_number  = 2,0,'',
        Example.change_password_func(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [0,0,''])

    def test_right_lv2(self):
        Example.level, Example.local_pos, Example.user_number  = 2,0,'',
        Example.change_password_func(but_num='right')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [2,1,''])

    def test_left_lv2(self):
        Example.level, Example.local_pos, Example.user_number,Example.crossout  = 2,0,'',False
        Example.change_password_func(but_num='left')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [2,1,''])

    def test_entr_lv2_l0(self):
        Example.level, Example.local_pos, Example.user_number,Example.crossout  = 2,0,'',False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number,Example.crossout ]
        self.assertListEqual(result, [2,0,'',True])

    def test_entr_lv2_l1(self):
        Example.level, Example.local_pos, Example.user_number ,Example.crossout = 2,1,'',False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number ]
        self.assertListEqual(result, [0,1,''])

    def test_entr_lv3(self):
        Example.level, Example.local_pos, Example.user_number,Example.crossout  = 3,0,'',False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number,Example.crossout ]
        self.assertListEqual(result, [3,0,'',True])

    def test_x_lv3(self):
        Example.level, Example.local_pos, Example.user_number,Example.crossout  = 3,0,'',False
        Example.change_password_func(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number,Example.crossout ]
        self.assertListEqual(result, [0,0,'',False])

    def test_number(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout = 0, 0, '', False
        Example.change_password_func(but_num='1')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout]
        self.assertListEqual(result, [0, 0, '1', False])

    def test_x_unfill(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.change_pass, Example.home_menu_stat = 0, 0, '', False,2, False
        Example.change_password_func(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.change_pass,Example.home_menu_stat]
        self.assertListEqual(result, [0, 3, '', False,0,True])

    def test_x_fill(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.change_pass, Example.home_menu_stat = 0, 0, '12', False,2, False
        Example.change_password_func(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.change_pass,Example.home_menu_stat]
        self.assertListEqual(result, [0, 0, '', False,2,False])

    def test_entr_1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.change_pass, Example.home_menu_stat = 0, 0, '1', False,2, False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.change_pass,Example.home_menu_stat]
        self.assertListEqual(result, [1, 0, '', False,2,False])

    def test_entr_2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.change_pass, Example.home_menu_stat = 0, 0, '2', False,2, False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.change_pass,Example.home_menu_stat]
        self.assertListEqual(result, [2, 0, '', False,2,False])

    def test_entr_3(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.change_pass, Example.home_menu_stat = 0, 0, '3', False,2, False
        Example.change_password_func(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.change_pass,Example.home_menu_stat]
        self.assertListEqual(result, [3, 0, '', False,2,False])

class new_password_entering_test(unittest.TestCase):

    def test_x_ab0(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities = 1, 0, '',True,0
        Example.new_password_entering(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout]
        self.assertListEqual(result, [0, 0, '',False])

    def test_number_ab0(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities = 1, 0, '',True,0
        Example.new_password_entering(but_num='1')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities]
        self.assertListEqual(result, [1, 0, '1',True,0])

    def test_entr_ab0_l0(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 0, '3',True,0,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 1, '',True,0,''])

    def test_entr_ab0_l1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '1',True,0,'1'
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 0, '',True,1,''])

    def test_entr_ab0_l1v2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,0,'1'
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 1, '',True,0,'1'])

    def test_x_ab1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,1,''
        Example.new_password_entering(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [0, 1, '',True,0,''])

    def test_right_ab1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,1,''
        Example.new_password_entering(but_num='right')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 0, '',True,1,''])

    def test_left_ab1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,1,''
        Example.new_password_entering(but_num='left')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 0, '',True,1,''])

    def test_entr_ab1_l1(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 0, '',True,1,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 0, '',True,2,''])

    def test_entr_ab1_l2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,1,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 1, '',True,3,''])

    def test_x_ab2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,2,''
        Example.new_password_entering(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [0, 1, '',True,0,''])

    def test_right_ab2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,2,''
        Example.new_password_entering(but_num='right')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 2, '',True,2,''])

    def test_left_ab2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,2,''
        Example.new_password_entering(but_num='left')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 0, '',True,2,''])

    def test_entr_ab2(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,2,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [0, 1, '',True,0,''])

    def test_x_ab3(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,3,''
        Example.new_password_entering(but_num='x')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [0, 1, '',True,0,''])

    def test_number_ab3(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,3,''
        Example.new_password_entering(but_num='1')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 1, '1',True,3,''])

    def test_entr_ab3_fill(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '11',True,3,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [0, 1, '',True,0,''])

    def test_entr_ab3_unfill(self):
        Example.level, Example.local_pos, Example.user_number, Example.crossout, Example.choose_pass_abilities,Example.user_input = 1, 1, '',True,3,''
        Example.new_password_entering(but_num='entr')
        result = [Example.level, Example.local_pos, Example.user_number, Example.crossout,Example.choose_pass_abilities,Example.user_input]
        self.assertListEqual(result, [1, 1, '',True,3,''])

class change_time_test(unittest.TestCase):

    def test_x_v1(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat = False,1,'12',1,1,-1,1,False,False
        Example.change_time(but_num='x')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat]
        self.assertListEqual(result, [True,0,'12',1,1,-1,1,False,False])

    def test_x_v2(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat = False,0,'12',1,1,1,1,False,False
        Example.change_time(but_num='x')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat]
        self.assertListEqual(result, [False,0,'12',0,1,1,2,False,False])

    def test_x_v3(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat = False,0,'12',1,1,-1,1,False,False
        Example.change_time(but_num='x')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat]
        self.assertListEqual(result, [True,0,'1',1,1,-1,2,True,True])

    def test_entr_v1(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake = False,1,'12',1,1,0,1,False,False,False
        Example.change_time(but_num='entr')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [False,0,'12',0,1,0,2,False,False,False])

    def test_entr_v2(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake = False,1,'12',1,1,-1,1,False,False,False
        Example.change_time(but_num='entr')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [True,1,'1',1,1,-1,2,True,True,False])

    def test_entr_v3(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake = False,1,'12',1,1,-1,1,False,False,True
        Example.change_time(but_num='entr')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [True,0,'12',1,1,-1,1,False,False,False])

    def test_number_v1(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake,Example.tim = False,5,'61',1,1,0,1,False,False,False,'12:12:10'
        Example.change_time(but_num='0')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [False,0,'61',0,1,0,2,False,False,False])

    def test_number_v2(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake,Example.tim = False,5,'61',1,1,-1,1,False,False,False,'12:12:10'
        Example.change_time(but_num='0')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [True,0,'6',1,1,-1,2,True,True,False])

    def test_number_v3(self):
        Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,\
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat, Example.mistake,Example.tim = False,5,'61',1,1,-1,1,False,False,True,'12:12:10'
        Example.change_time(but_num='0')
        result = [Example.time_capture, Example.local_pos, Example.user_input, Example.level, Example.global_pos,
        Example.temp_val, Example.time_date_stat, Example.passw_stat, Example.main_menu_stat,Example.mistake]
        self.assertListEqual(result, [True,0,'61',1,1,-1,1,False,False,False])

class correct_time_test(unittest.TestCase):

    def test_x(self):
        Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time = 2,0,1,'0.00',0
        Example.correct_time(but_num='x')
        result = [ Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time]
        self.assertListEqual(result, [2,0,1,'0.00',0])

    def test_entr(self):
        Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time = 2,0,1,'0.00',1
        Example.correct_time(but_num='entr')
        result = [ Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time]
        self.assertListEqual(result, [2,0,1,'0.00',1])

    def test_right(self):
        Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time = 2,0,1,'0.00',1
        Example.correct_time(but_num='right')
        result = [ Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time]
        self.assertListEqual(result, [2,0,1,0.18,0])

    def test_left(self):
        Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time = 2,0,1,0.00,1
        Example.correct_time(but_num='left')
        result = [ Example.level, Example.local_pos, Example.global_pos ,Example.corrector_time,Example.aspt_or_corrett_time]
        self.assertListEqual(result, [2,0,1,-0.17,0])

class import_data_test(unittest.TestCase):

    def test_x_unfill_l0(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 0,0,1,'','22',True
        Example.import_data(but_num='x')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [0,0,1,'','2',False])

    def test_x_unfill_l1(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 1,0,1,'','21',True
        Example.import_data(but_num='x')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [0,0,1,'','21',True])

    def test_x_fill(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 1,0,1,'22','21',True
        Example.import_data(but_num='x')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [1,0,1,'','21',True])

    def test_number(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 1,0,1,'22','21',True
        Example.import_data(but_num='1')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [1,0,1,'221','21',True])

    def test_entr_unfill(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 1,0,1,'','21',True
        Example.import_data(but_num='entr')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [1,0,1,'','21',True])

    def test_entr_fill_l0(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 0,0,1,'22','21',True
        Example.import_data(but_num='entr')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [1,0,1,'','21',True])

    def test_entr_fill_l1(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 1,0,1,'21','41',True
        Example.import_data(but_num='entr')
        result = [  Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat ]
        self.assertListEqual(result, [2,0,1,'','41',True])

class choose_type_events_test(unittest.TestCase):

    def test_x(self):
        Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat = 0,0,1,'','31',True
        Example.choose_type_events(but_num='x')
        result = [Example.level, Example.local_pos, Example.global_pos, Example.user_number,Example.user_input, Example.import_data_stat]
        self.assertListEqual(result, [0,0,0,'','',False])