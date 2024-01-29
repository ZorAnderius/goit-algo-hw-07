from AVLNode import AVLNode

def get_height(node: AVLNode) -> int:
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def min_value_node(node: AVLNode) -> AVLNode:
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def max_value_node(node: AVLNode) -> AVLNode:
    current = node
    while current.right is not None:
        current = current.right
    return current.key

def left_rotate(z: AVLNode) -> AVLNode:
    y = z.right
    T2 = y.left
    
    y.left = z
    z.right = T2
    
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    
    return y

def right_rotate(y: AVLNode) -> AVLNode:
    x = y.left
    T3 = x.right
    
    x.right = y
    y.left = T3
    
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    
    return x

def insert(root: AVLNode, key: int) -> AVLNode:
    if not root:
        return AVLNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    balance = get_balance(root)
    
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    
    return root

def delete_node(root: AVLNode, key: int) -> AVLNode or None:
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def total_tree_value(root: AVLNode, sum: int = 0):
    if root:
        sum = total_tree_value(root.left, sum) 
        sum = total_tree_value(root.right, sum)
        sum += root.key
    return sum