import ex3
import ex4
import ex5
import ex6
import unittest


class TestShapes(unittest.TestCase):

    def test_to_string_shape(self):
        s = ex3.Shape(4, 9)
        self.assertEqual(s.to_string(),"Shape: x=4, y=9")

    def test_to_string_rectangle(self):
        r = ex4.Rectangle(1, 2, 3, 4)
        self.assertEqual(r.to_string(),"Rectangle: x=1, y=2, width=3, height=4")

    def test_area_rectangle(self):
        r = ex4.Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(),12.0)

    def test_to_string_circle(self):
        c = ex5.Circle(5, 2, 2)
        self.assertEqual(c.to_string(),"Circle: x=5, y=2, radius=2")

    def test_area_circle(self):
        c = ex5.Circle(5, 2, 2)
        self.assertEqual(c.area(),12.566370614359172)

    def test_to_string_square(self):
        s = ex6.Square(0, 0, 10)
        self.assertEqual(s.to_string(),"Square: x=0, y=0, width=10, height=10")

    def test_area_square(self):
        s = ex6.Square(0, 0, 10)
        self.assertEqual(s.area(),100.0)