#as we are not allowed to used the built-in round() in this task
import builtins

round_func = builtins.round
def checking_round(*args, **kwargs):
    raise AssertionError("Built-in round is not allowed")
builtins.round = checking_round


import unittest
import ex4


class TestRounding(unittest.TestCase):

    def test_round_base_case0(self):
        self.assertEqual(ex4.round_(777.777),778,"Should be 778")

    def test_round_base_case1(self):
        self.assertEqual(ex4.round_(777.222),777,"Should be 777")

    def test_round_case_0(self):
        self.assertEqual(ex4.round_(777.777,0),778.0,"Should be 778.0")

    def test_round_case_1(self):
        self.assertEqual(ex4.round_(777.777,1),777.8,"Should be 777.8")

    def test_round_case_2(self):
        self.assertEqual(ex4.round_(777.777,2),777.78,"Should be 777.78")

    def test_round_case_3(self):
        self.assertEqual(ex4.round_(777.777,3),777.777,"Should be 777.777")

    def test_round_case_4(self):
        self.assertEqual(ex4.round_(777.777,4),777.777,"Should be 777.777")

    def test_round_case_minus_1(self):
        self.assertEqual(ex4.round_(777.777,-1),780.0,"Should be 780.0")

    def test_round_case_minus_2(self):
        self.assertEqual(ex4.round_(777.777,-2),800.0,"Should be 800.0")

    def test_round_case_minus_3(self):
        self.assertEqual(ex4.round_(777.777,-3),1000.0,"Should be 1000.0")

    def test_round_case_minus_4(self):
        self.assertEqual(ex4.round_(777.777,-4),0.0,"Should be 0.0")


if __name__=='__main__':
    unittest.main()