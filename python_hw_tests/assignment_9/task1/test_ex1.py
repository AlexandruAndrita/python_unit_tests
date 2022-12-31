import os
import unittest


class TestRegexFileSplitting(unittest.TestCase):

    def test_file_creation(self):
        os.system('python ex1.py -i ex1_data.txt --patterns d(..d) \d{3} ab12.c "d[^ ]+"')

        self.assertEqual(os.path.isfile("ex1_data.txt_0.txt"),True)
        self.assertEqual(os.path.isfile("ex1_data.txt_1.txt"),True)
        self.assertEqual(os.path.isfile("ex1_data.txt_2.txt"),True)
        self.assertEqual(os.path.isfile("ex1_data.txt_3.txt"),True)

        self.assertEqual(os.path.isfile("ex1_data.txt_4.txt"),False)

    def test_file_content(self):
        os.system('python ex1.py -i ex1_data.txt --patterns d(..d) \d{3} ab12.c "d[^ ]+" -s AAA')

        with open("ex1_data.txt_0.txt","r") as file:
            content=file.read()
            expected_content="deedAAAde dAAA"
            self.assertEqual(expected_content,content)

        with open("ex1_data.txt_1.txt","r") as file:
            content=file.read()
            expected_content="780AAA222AAA341AAA445AAA100AAA"
            self.assertEqual(expected_content,content)

        with open("ex1_data.txt_2.txt","r") as file:
            content=file.read()
            expected_content=""
            self.assertEqual(expected_content,content)

        with open("ex1_data.txt_3.txt","r") as file:
            content=file.read()
            expected_content="d23g780nbAAAdeedAAAdeAAAddd32AAA"
            self.assertEqual(expected_content,content)


if __name__=='__main__':
    unittest.main()