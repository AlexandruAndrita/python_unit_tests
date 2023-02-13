import unittest
import ex2


class TestClipping(unittest.TestCase):

    def test_clipping0(self):
        self.assertEqual(ex2.clip(),[],"Should be [] - empty list")

    def test_clipping1(self):
        self.assertEqual(ex2.clip(1, 2, 0.1, 0), [1, 1, 0.1, 0],"Should be  [1, 1, 0.1, 0]")

    def test_clipping2(self):
        self.assertEqual(ex2.clip(-1, 0.5),[0, 0.5],"Should be [0, 0.5]")

    def test_clipping3(self):
        self.assertEqual(ex2.clip(-1, 0.5, min_=-2), [-1, 0.5],"Should be  [-1, 0.5]")

    def test_clipping4(self):
        self.assertEqual(ex2.clip(-1, 0.5, max_=0.3),[0, 0.3],"Should be [0, 0.3]")

    def test_clipping5(self):
        self.assertEqual(ex2.clip(-1, 0.5, min_=2, max_=3),[2, 2],"Should be [2, 2]")


if __name__=='__main__':
    unittest.main()