import ex2
import unittest


class TestReader(unittest.TestCase):

    # Return true if string passed as path does not exist - raises a ValueError
    def test_file_exists(self):
        with self.assertRaises(ValueError):
            r=ex2.Reader("ex2_data.tx")

    def test_file_closed(self):
        with self.assertRaises(Exception):
            r=ex2.Reader("ex2_data.txt")
            r.close()
            r[23]

    def test_task2_index0(self):
        r=ex2.Reader("ex2_data.txt")
        self.assertEqual(r[0],b't')
        r.close()

    def test_task2_index1(self):
        r=ex2.Reader("ex2_data.txt")
        self.assertEqual(r[1],b'h')
        r.close()

    def test_task2_index_negative(self):
        r=ex2.Reader("ex2_data.txt")
        self.assertEqual(r[-1],b'\xb5')
        r.close()

    # Returns true if r["string"] raises a TypeError
    def test_task2_index_exception(self):
        r=ex2.Reader("ex2_data.txt")
        with self.assertRaises(TypeError):
            r["string"]

    # Returns true if r[100] raises an IndexError
    def test_task2_index_exception(self):
        r=ex2.Reader("ex2_data.txt")
        with self.assertRaises(IndexError):
            r[100]

    def test_task2_length(self):
        r=ex2.Reader("ex2_data.txt")
        self.assertEqual(len(r),56)
        r.close()


if __name__=='__main__':
    unittest.main()