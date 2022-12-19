import ex3
import unittest


class TestAggregator(unittest.TestCase):

    def test_sum_int(self):
        int_agg=ex3.Aggregator(agg_type=int)
        int_agg(1,2,3)
        int_agg(4,"string",5.1,90)
        self.assertEqual(int_agg(),100)

    def test_sum_stings(self):
        int_agg=ex3.Aggregator(agg_type=str,ignore_errors=False)
        int_agg("this"," ","is a test")
        self.assertEqual(int_agg(),"this is a test")

    def test_exception(self):
        int_agg=ex3.Aggregator(agg_type=str,ignore_errors=False)
        int_agg("test","string")
        with self.assertRaises(TypeError):
            int_agg(1)

    def test_None_case(self):
        int_agg=ex3.Aggregator(agg_type=str,ignore_errors=False)
        self.assertEqual(int_agg(),None)

if __name__=='__main__':
    unittest.main()