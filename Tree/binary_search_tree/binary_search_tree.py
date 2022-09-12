# Binary Search Tree

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self) -> str:
        return repr(self.data)

    def add_left_node(self,node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right_node(self,node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root,node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node

        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
        
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left_node(node)
    else:
        last_node.add_right_node(node)
    return root

def create_bst():
    root = TreeNode(10)

    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root,node)
    return root

def bst_search(node,key):
    while node is not None:
        if node.data == key:
            return node
        elif key < node.data:
            node = node.left
        else:
            node = node.right
    return node

def in_order(node,l):
    if node.left:
        in_order(node.left,l)
    l.append(node.data)
    if node.right:
        in_order(node.right,l)


if __name__ == "__main__":
    root = create_bst()
    print('Root node:',root)
    l = []
    in_order(root,l)
    print('In Order Traversal BST:',l)
    print('Bindary Search Tree Search:', bst_search(root,21))