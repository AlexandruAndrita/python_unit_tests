import ex1
import unittest


class TestComplexNumber(unittest.TestCase):

    def test_absolute_value(self):
        c=ex1.Complex(1.2,-5.4)
        self.assertEqual(c.abs(),5.531726674375733)

    def test_addition(self):
        c1=ex1.Complex(1.0,-2.0)
        c2=ex1.Complex(9.0,100.0)
        c1.add(c2)
        c_sum=ex1.Complex.add_all(c1, c1, c2, ex1.Complex(33.75, -14.25))
        self.assertEqual(c_sum.real==62.75 and c_sum.imaginary==281.75,True)
        self.assertEqual(c1.real==10.0 and c1.imaginary==98.0,True)

    def test_exception_add(self):
        c=ex1.Complex(1.7,-2.9)
        with self.assertRaises(TypeError):
            c.add(100)

    def test_exception_add_all(self):
        c=ex1.Complex(1.7,-2.9)
        with self.assertRaises(TypeError):
            c_sum=ex1.Complex.add_all(100)