# -*- coding: utf-8 -*-

import unittest, Homework

class Homework_TestCase(unittest.TestCase):
    def test_homework(self):
        self.assertEqual(
            Homework.FizzBizz(23), "23")
        self.assertEqual(
            Homework.Tex_free(30, 50000, False), 25000)
        self.assertEqual(
            Homework.Leap_year(1988), "윤년")
        

if __name__ == "__main__":
    unittest.main(verbosity=3)
