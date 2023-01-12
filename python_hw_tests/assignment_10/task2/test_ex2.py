import unittest
import numpy as np
import ex2


class TestMatrixSum(unittest.TestCase):

    def test_sum_matrix(self):
        statistics=ex2.matrix_stats(np.arange(3 * 4).reshape(3, 4))
        self.assertEqual(statistics['total_sum'],66)

        statistics=ex2.matrix_stats(np.array([[5,1,4,6],[7,2,5,8]]))
        self.assertEqual(statistics['total_sum'],38)

    def test_sum_rows(self):
        statistics = ex2.matrix_stats(np.arange(3 * 4).reshape(3, 4))
        self.assertEqual(np.array_equal(statistics['row_sums'],np.array([6,22,38])),True)

        statistics = ex2.matrix_stats(np.array([[5, 1, 4, 6], [7, 2, 5, 8]]))
        self.assertEqual(np.array_equal(statistics['row_sums'], np.array([16,22])), True)

    def test_sum_columns(self):
        statistics = ex2.matrix_stats(np.arange(3 * 4).reshape(3, 4))
        self.assertEqual(np.array_equal(statistics['column_sums'],np.array([12,15,18,21])),True)

        statistics = ex2.matrix_stats(np.array([[5, 1, 4, 6], [7, 2, 5, 8]]))
        self.assertEqual(np.array_equal(statistics['column_sums'], np.array([12,3,9,14])), True)

    def test_exception_handling(self):
        with self.assertRaises(ValueError):
            statistics = ex2.matrix_stats(np.array([2, 3, 6, 12, 45]))
    

if __name__=='__main__':
    unittest.main()