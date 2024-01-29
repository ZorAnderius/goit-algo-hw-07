from AVL_tree import insert

root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)