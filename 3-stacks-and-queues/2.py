from structures import Node, Stack

class MinNode(Node):
    def __init__(self, cargo=None, next=None, min=None):
        super(MinNode, self).__init__(cargo, next)
        self.min = None

class MinStack(Stack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.min = None

    def push(self, item):
        top = MinNode(item)
        if not self.top or item < self.top.min:
            top.min = item
        else:
            top.min = self.top.min
        top.next = self.top
        self.top = top
        self.min = self.top.min

if __name__ == '__main__':
    m = MinStack()
    for i in range(10):
        m.push(i)
        m.push(-i)
        print m.min
