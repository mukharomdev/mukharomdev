import unittest
from learnpython import data_structure
from learnpython import design_pattern
from learnpython import decorator


avltree = data_structure.avl_tree

tree_saya = avltree.AVL_Tree()
root = None

root = tree_saya.insert(root, 10)
root = tree_saya.insert(root, 20)
root = tree_saya.insert(root, 30)
root = tree_saya.insert(root, 40)
root = tree_saya.insert(root, 50)
root = tree_saya.insert(root, 25)




if __name__ == "__main__":
	print("lintasan preorder dari pohon avl yang dibangun adalah ")
	tree_saya.preOrder(root)
	print()

	unittest.main()