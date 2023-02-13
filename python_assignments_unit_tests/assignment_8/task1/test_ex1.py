import math
import ex1
import unittest


class TestComplex(unittest.TestCase):

    def test_comparison(self):
        c1=ex1.Complex(-1,-2)
        c2=ex1.Complex(2,4)
        c3=ex1.Complex(1,2)
        self.assertEqual(c1==c3,False)
        self.assertEqual(c1+c2==c3,True)

    def test_string_format(self):
        c1=ex1.Complex(-1, -2)
        self.assertEqual(repr(c1),"Complex(real=-1, imaginary=-2)")

    def test_absolute_value(self):
        c2=ex1.Complex(2, 4)
        self.assertEqual(abs(c2),math.sqrt(20))

    def test_addition(self):
        c1=ex1.Complex(-1,-2)
        c3=ex1.Complex(1,2)
        c1+=c3
        self.assertEqual(c1.real==0 and c1.imaginary==0,True)

    def test_add_all(self):
        c2=ex1.Complex(2, 4)
        c3=ex1.Complex(1, 2)
        c4=c2+c2+c3
        result=ex1.Complex(5,10)
        self.assertEqual(c4==result,True)
        result=ex1.Complex(2,4)
        self.assertEqual(c2==result,True)
        result=ex1.Complex(1,2)
        self.assertEqual(c3==result,True)

    def test_exception_handling(self):
        c=ex1.Complex(2,3)
        with self.assertRaises(TypeError):
            c=c+1

if __name__=='__main__':
    unittest.main()