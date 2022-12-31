import ex2
import unittest


class TestRegex(unittest.TestCase):

    def test_recognize_id(self):
        test_string="""This is an ID 01234567 this12345678 is not (leading "s"), nei12345678ther 
                    (leading "i" and trailing "t" letters) is 12345678this (trailing "t"). but this 
                    k22222222 is and also this K33333333, but again, k12345678is not valid (trailing "i") 
                    and neither is K123456789 (too many digits) or 1234 (too few digits)."""

        result_list=[1234567, 22222222, 33333333]
        self.assertEqual(ex2.extract_matr_ids(test_string),result_list)

    def test_empty_list(self):
        test_string="""Invalid examples are id=d1234 (leading "d") or
                    id=12 (too few digits) or id=x12345678 (leading "x") or id=123456789 (too many
                    digits) or ID=1234 ("ID" is not equal to "id")."""

        result_list=[]
        self.assertEqual(ex2.extract_matr_ids(test_string),result_list)

    def test_second_definition(self):
        test_string="""id=11111xyz is valid again but id=111111111xyz not. However, id=12345678abc is correct"""
        result_list=[11111, 12345678]
        self.assertEqual(ex2.extract_matr_ids(test_string),result_list)


if __name__=='__main__':
    unittest.main()