import unittest
import ex1


class TestDigits(unittest.TestCase):

    def test_case0(self):
        my_string="This 12 IS an ExamPLE SENTEnce."
        lowercase, uppercase, other, unique = [], [], [], set()
        self.assertEqual(ex1.return_characters(my_string,lowercase,uppercase,other,unique),None)
        self.assertEqual(lowercase, ['h', 'i', 's', 'a', 'n', 'x', 'a', 'm', 'n', 'c', 'e'],
                         "Should be ['h', 'i', 's', 'a', 'n', 'x', 'a', 'm', 'n', 'c', 'e']")
        self.assertEqual(uppercase,  ['T', 'I', 'S', 'E', 'P', 'L', 'E', 'S', 'E', 'N', 'T', 'E'],
                         "Should be ['T', 'I', 'S', 'E', 'P', 'L', 'E', 'S', 'E', 'N', 'T', 'E']")
        self.assertEqual(other, [' ', '1', '2', ' ', ' ', ' ', ' ', '.'],
                         "Should be [' ', '1', '2', ' ', ' ', ' ', ' ', '.']")
        self.assertEqual(unique, {'e', 'n', 'i', 'N', '2', 'c', 'E', 'h', 'a', 'I', 'x', '.', 'S',
                                    's', 'm', 'L', 'T', ' ', '1', 'P'},
                         """Should be {'e', 'n', 'i', 'N', '2', 'c', 'E', 'h', 'a', 'I', 'x', '.', 'S',
                                    's', 'm', 'L', 'T', ' ', '1', 'P' } """)

    def test_case_1(self):
        my_string="less characters 23333"
        lowercase, uppercase, other, unique = [], [], [], set()
        self.assertEqual(ex1.return_characters(my_string, lowercase, uppercase, other, unique), None)
        self.assertEqual(lowercase, ['l', 'e', 's', 's', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's'],
                         "Should be ['l', 'e', 's', 's', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's']")
        self.assertEqual(uppercase, [], "Should be []")
        self.assertEqual(other, [' ', ' ', '2', '3', '3', '3', '3'], "Should be [' ', ' ', '2', '3', '3', '3', '3']")
        self.assertEqual(unique, {'r', 'a', 's', 'e', 't', '2', 'l', 'c', 'h', ' ', '3'},
                         """Should be {'r', 'a', 's', 'e', 't', '2', 'l', 'c', 'h', ' ', '3'}""")


if __name__ == '__main__':
    unittest.main()
