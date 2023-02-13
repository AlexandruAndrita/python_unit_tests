import unittest
import ex2


class TestFileSelection(unittest.TestCase):

    def test_case0(self):
        fnames = ["file7.txt",  "file3.txt", "file2.txt",
          "file7.txt", "file1.txt", "file3.txt", "file4.png",
          "file4.png", "file5.txt", "file0.txt", "file7.dat"]
        files=[]
        self.assertEqual(ex2.select_files(fnames,files),None)
        self.assertEqual(files,['file0.txt', 'file1.txt', 'file2.txt', 'file3.txt', 'file5.txt', 'file7.txt'],
                         "Should be ['file0.txt', 'file1.txt', 'file2.txt', 'file3.txt', 'file5.txt', 'file7.txt']")

    def test_case_1(self):
        fnames = ["file7.png", "file7.dat", "file7.txt",
                  "file4.png", "file4.png", "file5.txt", "file0.txt", "file7.txt"]
        files=[]
        self.assertEqual(ex2.select_files(fnames,files),None)
        self.assertEqual(files,['file0.txt', 'file5.txt', 'file7.txt'],
                         "Should be ['file0.txt', 'file5.txt', 'file7.txt']")

    def test_case_2(self):
        fnames = ["file7.png", "file7.dat", "file7.dat",
                  "file4.png", "file4.png", "file5.tx", "file0.png", "file7.dat"]
        files=[]
        self.assertEqual(ex2.select_files(fnames,files),None)
        self.assertEqual(files,[], "Should be []")


if __name__=='__main__':
    unittest.main()