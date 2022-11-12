import unittest
import ex3


class TestCharactersCount(unittest.TestCase):

    def test_case0(self):
        string="This 12 IS an ExamPLE SENTEnce."
        dictionary=dict()
        self.assertEqual(ex3.count_characters(string,dictionary),None)
        self.assertEqual(dictionary,{'t': 2, 'h': 1, 'i': 2, 's': 3, ' ': 5, '1': 1, '2': 1, 'a': 2, 'n': 3,
                                    'e': 5, 'x': 1, 'm': 1, 'p': 1, 'l': 1, 'c': 1, '.': 1},
                         """Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, ' ': 5, '1': 1, '2': 1, 'a': 2, 'n': 3,
                                    'e': 5, 'x': 1, 'm': 1, 'p': 1, 'l': 1, 'c': 1, '.': 1} """)

    def test_case1(self):
        string="another example 1,2,3"
        dictionay=dict()
        self.assertEqual(ex3.count_characters(string,dictionay),None)
        self.assertEqual(dictionay,{'a': 2, 'n': 1, 'o': 1, 't': 1, 'h': 1, 'e': 3, 'r': 1, ' ': 2, 'x': 1, 'm': 1, 'p': 1, 'l': 1, '1': 1, ',': 2, '2': 1, '3': 1},
                                    """Should be {'a': 2, 'n': 1, 'o': 1, 't': 1, 'h': 1, 'e': 3, 'r': 1, ' ': 2, 'x': 1, 'm': 1, 'p': 1, 'l': 1, '1': 1, ',': 2, '2': 1, '3': 1}""")