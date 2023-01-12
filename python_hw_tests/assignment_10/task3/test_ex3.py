import unittest
import numpy as np
import ex3


class TestRandomizedDictionaries(unittest.TestCase):

    def test_id(self):
        result_dict=ex3.create_data([{"id": "classA", "n": 10, "a": 0, "b": 1.5}],0)
        self.assertEqual("classA" in result_dict.keys(),True)

    def test_shape(self):
        result_dict=ex3.create_data([{"id": "classB", "n": 20, "a": 3, "b": 4}],0)
        self.assertEqual(len(result_dict["classB"]),20)

        result_dict=ex3.create_data([{"id": "classC", "n": (5, 10), "a": 0, "b": 10}],0)
        self.assertEqual(result_dict["classC"].shape,(5,10))

    def test_bounds(self):
        result_dict=ex3.create_data([{"id": "classC", "n": (5, 10), "a": 0, "b": 10}],0)
        max_value=np.amax(result_dict["classC"])
        min_value=np.amin(result_dict["classC"])
        self.assertEqual(max_value<10,True)
        self.assertEqual(min_value>=0,True)


if __name__=='__main__':
    unittest.main()