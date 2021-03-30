import unittest
import tkinter as tk
from main import Main

Example = Main(root=tk.Tk())



class main_0_test(unittest.TestCase):

    def test_x(self):
        result = Example.corrector_time
        self.assertEqual(result, '0.00')


    def test_right(self):
        Example.main_0(but_num='right')
        result = Example.local_pos
        self.assertEqual(result, 1)
