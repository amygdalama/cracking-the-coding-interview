class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

class Stack(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            item = self.top.cargo
            self.top = self.top.next
            return item

    def push(self, item):
        top = Node(item)
        top.next = self.top
        self.top = top

    def peek(self):
        return self.top.cargo

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        if self.last:
            self.last.next = Node(item)
            self.last = self.last.next
        else:
            self.last = Node(item)
            self.first = self.last

    def dequeue(self):
        if self.first:
            item = self.first.cargo
            self.first = self.first.next
            if not self.first:
                self.last = None
            return item

if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)
    assert s.peek() == 9
    for i in range(10):
        assert s.pop() == 9-i
    assert s.pop() == None
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    for i in range(10):
        assert q.dequeue() == i