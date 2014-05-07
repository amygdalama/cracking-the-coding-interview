from queue import Queue

class BinaryTree(object):
    def __init__(self, root_object):
        self.key = root_object
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

def build_tree():
    r = BinaryTree('a')
    r.insert_left('b')
    r.left.insert_right('d')
    r.insert_right('c')
    r.right.insert_left('e')
    r.right.insert_right('f')
    return r

def visit(root):
    print root.key

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
    

if __name__ == '__main__':
    r = build_tree()
    breadth_first_search(r)