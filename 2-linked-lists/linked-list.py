class Node(object):
    def __init__(self, cargo=None, previous=None, next=None):
        self.cargo = cargo
        self.previous = previous
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList(object):
    def __init__(self):
        self.n = 0
        self.last = Node()
        self.first = self.last

    def append(self, cargo):
        self.last.next = Node()
        self.last.next.cargo = cargo
        self.last.next.previous = self.last
        self.last, self.previous = self.last.next, self.last
        if self.n == 0:
            self.first = self.last
        self.n += 1

    def front(self):
        if self.n == 0:
            return self.first
        else: 
            popped_cargo = self.first.cargo
            self.first = self.first.next
            self.n -= 1
            return popped_cargo

    def back(self):
        if self.n == 0:
            return self.last
        else:
            popped_cargo = self.last.cargo
            self.last = self.last.previous
            self.previous = self.previous.previous
            self.n -= 1
            return popped_cargo

    def size(self):
        return self.n

    def elements(self):
        node = self.first
        while node:
            yield node.cargo
            node = node.next

    
l = LinkedList()
l.append("thing")
l.append("cat")
l.append("bird")
for cargo in l.elements():
    print cargo