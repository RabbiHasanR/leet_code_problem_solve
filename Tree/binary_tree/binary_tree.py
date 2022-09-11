# create binary tree

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.data)

    def add_right_node(self,node):
        self.right = node
        if node is not None:
            node.parent = self
    
    def add_left_node(self,node):
        self.left = node
        if node is not None:
            node.parent = self

def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left_node(seven)
    two.add_right_node(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left_node(one)
    seven.add_right_node(six)
    five = Node(5)
    ten = Node(10)
    six.add_left_node(five)
    six.add_right_node(ten)
    eight = Node(8)
    nine.add_right_node(eight)
    three = Node(3)
    four = Node(4)
    eight.add_left_node(three)
    eight.add_right_node(four)
    return two


# binary tree te pre order tree traverse ar khetre prothome root node visit kora hoy. pore left sub tree pre order 
# poddotite traverse kora hoy. pore right sub tree pre order poddotite traverse kora hoy

def pre_order(node):
    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


# binary tree te post order tree traverse ar khetre prothome left subtree traverse korte hoy post order poddotite
# pore right subtree traverse korte hoy post order poddotite. tarpor root node traverse korte hoy
def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)


# binary tree te in order tree traverse ar khetre prothome left subtree traverse korte hoy in order poddotitie
# pore root node visit korte hoy and pore right subtree traverse korte hoy in order poddotite
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

if __name__ == "__main__":
    root = create_tree()
    print("Root Node:",root)
    print('Pre Order Tree Traverse:')
    pre_order(root)
    print("Post Order Tree Traverse:")
    post_order(root)
    print("In Order Tree Traverse:")
    in_order(root)
        