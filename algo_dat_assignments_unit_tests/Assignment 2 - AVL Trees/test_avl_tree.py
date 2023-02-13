import unittest
import avl_tree


class Test_AVL_tree(unittest.TestCase):

    def test_insertion(self):
        tree = avl_tree.AVLTree()
        tree.insert(5,"5")
        tree.insert(7,"7")
        tree.insert(8,"8")
        tree.insert(4,"4")
        tree.insert(6,"6")
        tree.insert(-1,"-1")
        tree.insert(10,"10")

        self.assertEqual(tree.get_tree_root().key,5)
        self.assertEqual(tree.root.left.key,4)
        self.assertEqual(tree.root.left.left.key,-1)
        self.assertEqual(tree.root.right.key,7)
        self.assertEqual(tree.root.right.left.key,6)
        self.assertEqual(tree.root.right.right.key,8)
        self.assertEqual(tree.root.right.right.right.key,10)

        self.assertEqual(tree.root.left.right,None)
        self.assertEqual(tree.root.left.left.left,None)
        self.assertEqual(tree.root.left.left.right,None)
        self.assertEqual(tree.root.right.left.left,None)
        self.assertEqual(tree.root.right.left.right,None)
        self.assertEqual(tree.root.right.right.left,None)
        self.assertEqual(tree.root.right.right.right.left,None)
        self.assertEqual(tree.root.right.right.right.right,None)

    def test_tree_height(self):
        tree = avl_tree.AVLTree()
        self.assertEqual(tree.get_tree_height(),-1)

        tree.insert(5, "5")
        self.assertEqual(tree.get_tree_height(),0)

        tree.insert(7, "7")
        self.assertEqual(tree.get_tree_height(),1)

        tree.insert(8, "8")
        self.assertEqual(tree.get_tree_height(),1)

        tree.insert(4, "4")
        self.assertEqual(tree.get_tree_height(),2)

        tree.insert(6, "6")
        self.assertEqual(tree.get_tree_height(),2)

        tree.insert(-1, "-1")
        self.assertEqual(tree.get_tree_height(),2)

        tree.insert(10, "10")
        self.assertEqual(tree.get_tree_height(),3)

    def test_tree_size(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        self.assertEqual(tree.get_tree_size(), 1)

        tree.insert(7, "7")
        self.assertEqual(tree.get_tree_size(), 2)

        tree.insert(8, "8")
        self.assertEqual(tree.get_tree_size(), 3)

        tree.insert(4, "4")
        self.assertEqual(tree.get_tree_size(), 4)

        tree.insert(6, "6")
        self.assertEqual(tree.get_tree_size(), 5)

        tree.insert(-1, "-1")
        self.assertEqual(tree.get_tree_size(), 6)

        tree.insert(10, "10")
        self.assertEqual(tree.get_tree_size(), 7)

    def test_array(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        array=tree.to_array()
        array_solution=[5, 4, -1, 7, 6, 8, 10]
        self.assertEqual(len(array),len(array_solution))

        i=0
        while i<len(array):
            self.assertEqual(array[i],array_solution[i])
            i+=1

    def test_find_key(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        self.assertEqual(tree.find_by_key(5),5)
        self.assertEqual(tree.find_by_key(6),6)
        self.assertEqual(tree.find_by_key(9),None)
        self.assertEqual(tree.find_by_key(10),10)

    def test_removal_no_children(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        tree.remove_by_key(10)
        self.assertEqual(tree.root.key,5)
        self.assertEqual(tree.root.left.key,4)
        self.assertEqual(tree.root.right.key,7)
        self.assertEqual(tree.root.left.left.key,-1)
        self.assertEqual(tree.root.right.left.key,6)
        self.assertEqual(tree.root.right.right.key,8)

    def test_removal_one_child(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        tree.remove_by_key(8)
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 4)
        self.assertEqual(tree.root.right.key, 7)
        self.assertEqual(tree.root.left.left.key, -1)
        self.assertEqual(tree.root.right.left.key, 6)
        self.assertEqual(tree.root.right.right.key, 10)

    def test_removal_two_children(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        tree.remove_by_key(7)
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 4)
        self.assertEqual(tree.root.right.key, 8)
        self.assertEqual(tree.root.left.left.key, -1)
        self.assertEqual(tree.root.right.left.key, 6)
        self.assertEqual(tree.root.right.right.key, 10)

    def test_remove_root(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        tree.remove_by_key(tree.get_tree_root().key)
        self.assertEqual(tree.root.key, 6)
        self.assertEqual(tree.root.left.key, 4)
        self.assertEqual(tree.root.right.key, 8)
        self.assertEqual(tree.root.left.left.key, -1)
        self.assertEqual(tree.root.right.left.key, 7)
        self.assertEqual(tree.root.right.right.key, 10)

    def test_remove_non_existing_key(self):
        tree = avl_tree.AVLTree()
        tree.insert(5, "5")
        tree.insert(7, "7")
        tree.insert(8, "8")
        tree.insert(4, "4")
        tree.insert(6, "6")
        tree.insert(-1, "-1")
        tree.insert(10, "10")

        with self.assertRaises(ValueError):
            tree.remove_by_key(None)

if __name__=='__main__':
    unittest.main()