import unittest
import numpy as np
import ex4


class TestMinesweeper(unittest.TestCase):

    def test_exception_shape(self):
        with self.assertRaises(ValueError):
            matrix=ex4.create_minefield(1,2,3,0)
        with self.assertRaises(ValueError):
            matrix=ex4.create_minefield(7,0,3,0)

    def test_exception_mines(self):
        with self.assertRaises(ValueError):
            matrix=ex4.create_minefield(7,7,50,0)
        with self.assertRaises(ValueError):
            matrix=ex4.create_minefield(7,7,49,0)
        with self.assertRaises(ValueError):
            matrix=ex4.create_minefield(7,7,0,0)

    def test_mines_number(self):
        matrix=ex4.create_minefield(7,7,3,0)
        self.assertEqual(np.count_nonzero(matrix==-1)==3,True)

        matrix=ex4.create_minefield(7,7,1,0)
        self.assertEqual(np.count_nonzero(matrix==-1)==1,True)

        matrix=ex4.create_minefield(7,7,20,0)
        self.assertEqual(np.count_nonzero(matrix==-1)==20,True)

    # def test_minefield(self):
    #     matrix=ex4.create_minefield(7,7,20,0)
    #     expected_matrix=np.array([[-1,-1,-1,2,1,1,-1],[ 3,-1,5,-1,2,2,2],[ 2,3,-1,3,4,-1,2],[-1,3,3,4,-1,-1,2],[ 2,-1,3,-1,-1,4,1],
    #     [2,3,-1,6,-1,4,1],[-1,2,2,-1,-1,-1,1]])
    #     self.assertEqual(np.array_equal(matrix,expected_matrix),True)


if __name__=='__main__':
    unittest.main()