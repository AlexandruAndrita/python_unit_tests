import unittest
import ex1


class TestFib(unittest.TestCase):

    def test_fib0(self):
        self.assertEqual(ex1.fib(0),0,"Should be 0")

    def test_fib1(self):
        self.assertEqual(ex1.fib(1),1,"Should be 1")

    def test_fib2(self):
        self.assertEqual(ex1.fib(2),1,"Should be 1")

    def test_fib3(self):
        self.assertEqual(ex1.fib(3),2,"Should be 2")

    def test_fib7(self):
        self.assertEqual(ex1.fib(7),13,"Should be 13")

    def test_fib23(self):
        self.assertEqual(ex1.fib(23),28657,"Should be 28657")

    def test_fib75(self):
        self.assertEqual(ex1.fib(75),2111485077978050,"Should be 2111485077978050")

    def test_fib_negative_input1(self):
        self.assertEqual(ex1.fib(-2),-1,"Should be -1")

    def test_fib_negative_input2(self):
        self.assertEqual(ex1.fib(-100),-1,"Should be -1")


if __name__=='__main__':
    unittest.main()