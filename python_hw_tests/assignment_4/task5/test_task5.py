import unittest
import ex5


class BubbleSortTest(unittest.TestCase):

    def test_sorted_0(self):
        some_list = [1, 3, 0, 4, 5]
        self.assertEqual(ex5.sort(some_list),None)
        self.assertEqual(some_list,[0, 1, 3, 4, 5],"Should be [0, 1, 3, 4, 5]")

    def test_sorted_1(self):
        some_list = [1, 3, 0, 4, 5]
        self.assertEqual(ex5.sort(some_list,ascending=False),None)
        self.assertEqual(some_list,[5, 4, 3, 1, 0],"Should be [5, 4, 3, 1, 0]")

    def test_sorted_2(self):
        some_list = [5, 6, 3, 2, 1, 4, 9, 8, 10, 44, 23, 100, 69]
        self.assertEqual(ex5.sort(some_list,ascending=True),None)
        self.assertEqual(some_list,[1, 2, 3, 4, 5, 6, 8, 9, 10, 23, 44, 69, 100],
                         "Should be [1, 2, 3, 4, 5, 6, 8, 9, 10, 23, 44, 69, 100]")

    def test_sorted_3(self):
        some_list = [5, 6, 3, 2, 1, 4, 9, 8, 10, 44, 23, 100, 69]
        self.assertEqual(ex5.sort(some_list,ascending=False),None)
        self.assertEqual(some_list,[100, 69, 44, 23, 10, 9, 8, 6, 5, 4, 3, 2, 1],
                         "Should be [100, 69, 44, 23, 10, 9, 8, 6, 5, 4, 3, 2, 1]")


if __name__=='__main__':
    unittest.main()