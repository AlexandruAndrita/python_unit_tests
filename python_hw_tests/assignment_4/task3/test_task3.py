import unittest
import ex3


class TestSplitting(unittest.TestCase):

    def test_split_proportion0(self):
        self.assertEqual(ex3.create_train_test_splits([], 0.5),([],[]),"Should be ([],[])")

    def test_split_proportion1(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.5),([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]),
                         "Should be ([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]")

    def test_split_proportion2(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.67),([0, 1, 2, 3, 4, 5], [6, 7, 8, 9]),
                         "Should be ([0, 1, 2, 3, 4, 5], [6, 7, 8, 9])")

    def test_split_proportion3(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.22),([0, 1], [2, 3, 4, 5, 6, 7, 8, 9]),
                         "Should be ([0, 1], [2, 3, 4, 5, 6, 7, 8, 9])")

    def test_split_proportion4(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.1),([0], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         "Should be ([0], [1, 2, 3, 4, 5, 6, 7, 8, 9])")

    def test_split_proportion5(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.19),([0], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         "Should be ([0], [1, 2, 3, 4, 5, 6, 7, 8, 9])")

    def test_split_proportion6(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.32),([0, 1, 2], [3, 4, 5, 6, 7, 8, 9]),
                         "Should be ([0, 1, 2], [3, 4, 5, 6, 7, 8, 9])")


if __name__=='__main__':
    unittest.main()