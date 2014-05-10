from queue import Queue

class BinaryTree(object):
    def __init__(self, root_object):
        self.data = root_object
        self.left = None
        self.right = None
        self.visited = False

    def insert_left(self, new_node):
        if self.left:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t
        else:
            self.left = BinaryTree(new_node)

    def insert_right(self, new_node):
        if self.right:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t
        else:
            self.right = BinaryTree(new_node)

class BinarySearchTree(object):
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None
        self.visited = False

    def insert(self, value):
        if self.data == None:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

def build_tree():
    r = BinaryTree('a')
    r.insert_left('b')
    r.left.insert_right('d')
    r.insert_right('c')
    r.right.insert_left('e')
    r.right.insert_right('f')
    return r

def visit(root):
    print root.data

def depth_first_search(root):
    if root:
        visit(root)
        root.visited = True
        adjacent = (root.left, root.right)
        for n in adjacent:
            if n and not n.visited:
                depth_first_search(n)
    else:
        return

def breadth_first_search(root):
    q = Queue()
    root.visited = True
    visit(root)
    q.enqueue(root)     # add root to end of queue
    while q.first:      # while q is nonempty
        r = q.dequeue()
        adjacent = (r.left, r.right)
        for n in adjacent:
            if n and not n.visited:
                visit(n)
                n.visited = True
                q.enqueue(n)
    
def in_order_traversal(tree):
    if tree:
        in_order_traversal(tree.left)
        print tree.data
        in_order_traversal(tree.right)

def post_order_traversal(tree):
    if tree:
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)
        print tree.data

def pre_order_traversal(tree):
    if tree:
        print tree.data
        pre_order_traversal(tree.left)
        pre_order_traversal(tree.right)

if __name__ == '__main__':
    t = BinarySearchTree()
    t.insert(1)
    t.insert(4)
    t.insert(5)
    t.insert(3)
    t.insert(17)
    t.insert(0)
    t.insert(15)
    pre_order_traversal(t)