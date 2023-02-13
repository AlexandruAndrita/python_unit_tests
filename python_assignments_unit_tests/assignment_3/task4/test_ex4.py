import unittest
import ex4


class TestMatrixOperations(unittest.TestCase):

    def test_case0(self):
        matrix=[[1, 2, 3, 4],[5, 0, 0, 0],[0, 0, 0, 0]]
        row_sum,column_sum,total_sum=[],[],0
        self.assertEqual(ex4.matrix_operations(matrix,row_sum,column_sum),15,"Should be 15")
        self.assertEqual(row_sum,[10,5,0],"Should be [10,5,0]")
        self.assertEqual(column_sum,[6,2,3,4],"Should be [6,2,3,4]")

    def test_case1(self):
        matrix = [[1, 2, 3, 4], [5, 0, 0, 1], [1, 0, 1, 0]]
        row_sum, column_sum, total_sum = [], [], 0
        self.assertEqual(ex4.matrix_operations(matrix, row_sum, column_sum), 18, "Should be 18")
        self.assertEqual(row_sum, [10, 6, 2], "Should be [10,6,2]")
        self.assertEqual(column_sum, [7, 2, 4, 5], "Should be [7,2,4,5]")
