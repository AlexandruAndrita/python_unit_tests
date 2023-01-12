import unittest
import numpy as np
import ex1


class TestExtendMethod(unittest.TestCase):

    def test_no_fill_size(self):
        new_array=ex1.extend(np.arange(4),7)
        self.assertEqual(new_array.size,7)

    def test_1D_exception(self):
        tmp=np.array([[1,2,3],[4,5,6]])
        with self.assertRaises(ValueError):
            ex1.extend(tmp,7)

    def test_size_exception(self):
        tmp=np.array([1,2,3,4])
        with self.assertRaises(ValueError):
            ex1.extend(tmp,3)

    def test_fill_value(self):
        new_array=ex1.extend(np.arange(4), 7, fill=0)
        tmp=np.array([0,1,2,3,0,0,0])
        self.assertEqual(np.array_equal(new_array,tmp),True)

    def test_fill_mean_int(self):
        new_array=ex1.extend(np.arange(4),7,fill="mean")
        tmp=np.array([0,1,2,3,1,1,1])
        self.assertEqual(np.array_equal(new_array,tmp),True)

    def test_fill_mean_float(self):
        new_array=ex1.extend(np.arange(4,dtype=float),7,fill="mean")
        tmp=np.array([0.,1.,2.,3.,1.5,1.5,1.5])
        self.assertEqual(np.array_equal(new_array,tmp),True)

    def test_fill_mean_string(self):
        new_array=ex1.extend(np.array(["hello","world"]),5,fill="mean")
        tmp=np.array(['hello','world','mean','mean','mean'])
        self.assertEqual(np.array_equal(new_array,tmp),True)


if __name__=='__main__':
    unittest.main()