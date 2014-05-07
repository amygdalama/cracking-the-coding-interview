class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

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